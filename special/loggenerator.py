import argparse
import uuid
from datetime import date, datetime

import random
from rdflib import Graph
from rdflib.namespace import XSD, RDF
from rdflib.term import URIRef, BNode, Literal

from special.exceptions import PolicyAspectCannotBeViolatedException
from special.policy import Policy
from special.vocab import has_data_subject, has_policy, data_classes, \
    purpose_classes, recipient_classes, location_classes, processing_classes, \
    has_data, has_purpose, has_recipient, has_storage, has_processing, \
    subclasses, data_subject, log_entry_content, transaction_time, Log_Entry, \
    violation_on

NS = 'http://www.example.com/'
DEBUG = True


def user_uri(user_id):
    return URIRef(NS + 'users/%s' % str(user_id))


def policy_uri(policy_id):
    return URIRef(NS + 'policy/%s' % str(policy_id))


def log_entries_uri(log_entries_id):
    return URIRef(NS + 'logEntries/%s' % str(log_entries_id))


def log_entry_uri(log_entry_content_id):
    return URIRef(NS + 'logEntryContents/%s' % str(log_entry_content_id))


def random_consent(user_id):
    """
    Example consent:

    <http://www.example.com/policy/1ab67399-d656-425d-8718-82f26fc098c7>
    <http://purl.org/dc/terms/created> "2018-08-13T15:46:31.067+02:00"^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
    <http://www.specialprivacy.eu/langs/usage-policy#hasDataSubject> <http://www.example.com/users/705b7308-e333-4a8d-93d2-36cecc7d31a6> ;
    <http://www.specialprivacy.eu/vocabs/policy#simplePolicy> [
        <http://www.specialprivacy.eu/langs/usage-policy#hasData> <http://www.specialprivacy.eu/vocabs/data#Demographic> ;
        <http://www.specialprivacy.eu/langs/usage-policy#hasPurpose> <http://www.specialprivacy.eu/vocabs/purposes#Admin> ;
        <http://www.specialprivacy.eu/langs/usage-policy#hasRecipient> <http://www.specialprivacy.eu/vocabs/recipients#OtherRecipient> ;
        <http://www.specialprivacy.eu/langs/usage-policy#hasStorage> <http://www.specialprivacy.eu/langs/usage-policy#AnyLocation> ;
        <http://www.specialprivacy.eu/langs/usage=policy#hasProcessing> <http://www.specialprivacy.eu/vocabs/processing#Copy>
    ], [
        <http://www.specialprivacy.eu/langs/usage-policy#hasData> <http://www.specialprivacy.eu/vocabs/data#PhysicalActivity> ;
        <http://www.specialprivacy.eu/langs/usage-policy#hasPurpose> <http://www.specialprivacy.eu/vocabs/purposes#Telemarketing> ;
        <http://www.specialprivacy.eu/langs/usage-policy#hasRecipient> <http://www.specialprivacy.eu/vocabs/recipients#Delivery> ;
        <http://www.specialprivacy.eu/langs/usage-policy#hasStorage> <http://www.specialprivacy.eu/langs/usage-policy#AnyLocation> ;
        <http://www.specialprivacy.eu/langs/usage=policy#hasProcessing> <http://www.specialprivacy.eu/vocabs/processing#Move>
    ] ;
    a <http://www.specialprivacy.eu/vocabs/policy#Consent> .
    """
    user_resource = user_uri(user_id)
    policy_resource = policy_uri(uuid.uuid4())
    g = Graph()

    num_user_policies = 1  # max([1, round(abs(random.gauss(1, 1.5)))])

    policies = []
    g.add((policy_resource, has_data_subject, user_resource))

    for i in range(num_user_policies):
        policy_bnode = BNode()
        g.add((policy_resource, has_policy, policy_bnode))
        # data
        data_cls = random.choice(data_classes)
        g.add((policy_bnode, has_data, data_cls))

        # purpose
        purpose_cls = random.choice(purpose_classes)
        g.add((policy_bnode, has_purpose, purpose_cls))

        # recipient
        recipient_cls = random.choice(recipient_classes)
        g.add((policy_bnode, has_recipient, recipient_cls))

        # storage
        storage_cls = random.choice(location_classes)
        g.add((policy_bnode, has_storage, storage_cls))

        # processing
        processing_cls = random.choice(processing_classes)
        g.add((policy_bnode, has_processing, processing_cls))

        policies.append(Policy(
            data_cls, purpose_cls, recipient_cls, storage_cls, processing_cls))

    # print(g.serialize(None, 'turtle').decode('utf-8'))
    return g, policies


def _generate_policy_triple(policy_aspect, policies, log_entry_content_res):
    policy = random.choice(policies)
    policy_cls = policy.get(policy_aspect)
    picked_subclass = random.choice(subclasses[policy_cls])

    return log_entry_content_res, policy_aspect, picked_subclass


def _generate_policy_violating_triple(
        policy_aspect, policies, log_entry_content_res):
    policy = random.choice(policies)
    policy_cls = policy.get(policy_aspect)

    all_classes_for_aspect = {
        has_data: data_classes,
        has_purpose: purpose_classes,
        has_recipient: recipient_classes,
        has_storage: location_classes,
        has_processing: processing_classes
    }

    all_classes = all_classes_for_aspect[policy_aspect].copy()
    picked_cls = None
    while all_classes:
        picked_cls = random.choice(all_classes)
        all_classes.remove(picked_cls)
        if picked_cls not in subclasses[policy_cls]:
            break

    if picked_cls is None:
        raise PolicyAspectCannotBeViolatedException()
    return log_entry_content_res, policy_aspect, picked_cls


def rnd_transaction_time():
    h = random.randint(0, 23)
    m = random.randint(0, 59)
    s = random.randint(0, 59)
    today = date.today()
    d = datetime(today.year, today.month, today.day, h, m, s)
    return Literal(str(d.isoformat()), None, XSD.dateTime)


def create_violating_log_entry(policies, user_id):
    g = Graph()
    policy_aspects = {
        has_data, has_purpose, has_recipient, has_storage, has_processing}
    violated_aspects = random.choices(list(policy_aspects))
    non_violated_aspects = policy_aspects.difference(violated_aspects)

    log_entries_res = log_entries_uri(uuid.uuid4())
    log_entry_content_res = log_entry_uri(uuid.uuid4())

    g.add((log_entries_res, data_subject, user_uri(user_id)))
    g.add((log_entries_res, log_entry_content, log_entry_content_res))
    g.add((log_entries_res, transaction_time, rnd_transaction_time()))
    g.add((log_entries_res, RDF.type, Log_Entry))

    for v in violated_aspects:
        g.add(_generate_policy_violating_triple(
            v, policies, log_entry_content_res))
        if DEBUG:
            g.add((log_entry_content_res, violation_on, v))

    for n in non_violated_aspects:
        g.add(_generate_policy_triple(n, policies, log_entry_content_res))

    return g


def create_log_entry(policies, user_id):
    g = Graph()
    policy_aspects = {
        has_data, has_purpose, has_recipient, has_storage, has_processing}

    log_entries_res = log_entries_uri(uuid.uuid4())
    log_entry_content_res = log_entry_uri(uuid.uuid4())

    g.add((log_entries_res, data_subject, user_uri(user_id)))
    g.add((log_entries_res, log_entry_content, log_entry_content_res))
    g.add((log_entries_res, transaction_time, rnd_transaction_time()))
    g.add((log_entries_res, RDF.type, Log_Entry))

    for n in policy_aspects:
        g.add(_generate_policy_triple(n, policies, log_entry_content_res))

    return g


def main(num_users, log_size, percentage_of_violations, consent_out_file_path,
         log_out_file_path):
    log_all = Graph()
    consent_all = Graph()

    for i in range(num_users):
        user_id = uuid.uuid4()
        consent_rdf, policies = random_consent(user_id)
        consent_all += consent_rdf
        user_log = Graph()
        violations_counts = 0
        target_num_violation = int(log_size * percentage_of_violations / 100)

        for i in range(log_size):
            if (violations_counts < target_num_violation) and \
                    (random.random() <= percentage_of_violations / 100):
                while True:
                    try:
                        user_log += \
                            create_violating_log_entry(policies, user_id)
                        break
                    except PolicyAspectCannotBeViolatedException:
                        pass
                violations_counts += 1
            else:
                user_log += create_log_entry(policies, user_id)

        log_all += user_log
        # print(user_log.serialize(None, 'turtle').decode('utf-8'))
        print('********************************************************')
        print('Number of violating entries for user %s: %i' %
              (user_id, violations_counts))
        print('********************************************************')

    log_all.serialize(log_out_file_path, 'ntriples')
    consent_all.serialize(consent_out_file_path, 'turtle')

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('num_users')
    argparser.add_argument('log_size')
    argparser.add_argument('percentage_of_violations_per_user')
    argparser.add_argument('consent_output_file')
    argparser.add_argument('log_output_file')

    args = argparser.parse_args()

    main(
        int(args.num_users), int(args.log_size),
        int(args.percentage_of_violations_per_user),
        args.consent_output_file, args.log_output_file)

