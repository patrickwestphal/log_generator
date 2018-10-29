import argparse
import uuid
from datetime import date, datetime

import random
from rdflib import Graph
from rdflib.namespace import XSD, RDF
from rdflib.term import URIRef, BNode, Literal

from special.exceptions import PolicyCannotBeViolatedException, \
    PolicyAspectCannotBeViolatedException, ParticularPolicyCannotBeViolatedException
from special.policy import Policy
from special.vocab import has_data_subject, has_policy, data_classes, \
    purpose_classes, recipient_classes, location_classes, processing_classes, \
    has_data, has_purpose, has_recipient, has_storage, has_processing, \
    subclasses, data_subject, log_entry_content, transaction_time, Log_Entry, \
    violation_on, aspect_classes

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


def _truncated_discrete_gauss(mu, sigma, start=1, end=10):
    val = round(random.gauss(mu, sigma))
    while not (start <= val <= end):
        val = round(random.gauss(mu, sigma))

    return val


def random_consent(user_id, num_user_policies=1, num_policy_aspects=None):
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
    # normal distribution parameters for choosing the number of policy aspect
    # entries
    mu = 5
    sigma = 4

    def rnd_choice(classes):
        max_ = min(10, len(classes))
        num = _truncated_discrete_gauss(mu, sigma, end=max_)
        return random.sample(data_classes, num)

    user_resource = user_uri(user_id)
    policy_resource = policy_uri(uuid.uuid4())
    g = Graph()

    policies = []
    g.add((policy_resource, has_data_subject, user_resource))

    for i in range(num_user_policies):
        policy_bnode = BNode()
        g.add((policy_resource, has_policy, policy_bnode))
        # data
        if num_policy_aspects is None:
            data_cls_choices = rnd_choice(data_classes)
        else:
            num = min(num_policy_aspects, len(data_classes))
            data_cls_choices = random.sample(data_classes, num)
        for data_cls in data_cls_choices:
            g.add((policy_bnode, has_data, data_cls))

        # purpose
        if num_policy_aspects is None:
            purpose_cls_choices = rnd_choice(purpose_classes)
        else:
            num = min(num_policy_aspects, len(purpose_classes))
            purpose_cls_choices = random.sample(purpose_classes, num)
        for purpose_cls in purpose_cls_choices:
            g.add((policy_bnode, has_purpose, purpose_cls))

        # recipient
        if num_policy_aspects is None:
            recipient_cls_choices = rnd_choice(recipient_classes)
        else:
            num = min(num_policy_aspects, len(recipient_classes))
            recipient_cls_choices = random.sample(recipient_classes, num)
        for recipient_cls in recipient_cls_choices:
            g.add((policy_bnode, has_recipient, recipient_cls))

        # storage
        if num_policy_aspects is None:
            storage_cls_choices = rnd_choice(location_classes)
        else:
            num = min(num_policy_aspects, len(location_classes))
            storage_cls_choices = random.sample(location_classes, num)
        for storage_cls in storage_cls_choices:
            g.add((policy_bnode, has_storage, storage_cls))

        # processing
        if num_policy_aspects is None:
            processing_cls_choices = rnd_choice(processing_classes)
        else:
            num = min(num_policy_aspects, len(processing_classes))
            processing_cls_choices = random.sample(processing_classes, num)
        for processing_cls in processing_cls_choices:
            g.add((policy_bnode, has_processing, processing_cls))

        policies.append(Policy(
            data_cls_choices, purpose_cls_choices, recipient_cls_choices,
            storage_cls_choices, processing_cls_choices))

    # print(g.serialize(None, 'turtle').decode('utf-8'))
    return g, policies


def _generate_policy_triple(policy_aspect, policies, log_entry_content_res):
    policy = random.choice(policies)
    policy_classes = policy.get(policy_aspect)
    policies_subclasses = []
    for policy_cls in policy_classes:
        policies_subclasses += subclasses[policy_cls]
    picked_subclass = random.choice(policies_subclasses)

    return log_entry_content_res, policy_aspect, picked_subclass


def _generate_policy_violating_triple(
        policy_aspect, policies, log_entry_content_res):

    for policy in policies:
        policy_classes = policy.get(policy_aspect)

        all_classes = aspect_classes[policy_aspect].copy()
        picked_cls = None
        policies_subclasses = []
        for policy_cls in policy_classes:
            policies_subclasses += subclasses[policy_cls]

        while all_classes:
            picked_cls = random.choice(all_classes)
            all_classes.remove(picked_cls)
            if picked_cls not in policies_subclasses:
                break
            else:
                picked_cls = None

        if picked_cls is not None:
            return log_entry_content_res, policy_aspect, picked_cls

    raise PolicyAspectCannotBeViolatedException()


def rnd_transaction_time():
    h = random.randint(0, 23)
    m = random.randint(0, 59)
    s = random.randint(0, 59)
    today = date.today()
    d = datetime(today.year, today.month, today.day, h, m, s)
    return Literal(str(d.isoformat()), None, XSD.dateTime)


def create_violating_log_entry(policies, user_id):
    g = Graph()
    tmp = {
        has_data, has_purpose, has_recipient, has_storage, has_processing}

    # Filter out those aspects that cannot be violated since they already
    # allow everything
    policy_aspects = set()
    for aspect in tmp:
        num_aspect_entries = min(map(len, [p.get(aspect) for p in policies]))
        if num_aspect_entries < len(aspect_classes[aspect]):
            policy_aspects.add(aspect)

    if len(policy_aspects) == 0:
        raise PolicyCannotBeViolatedException()

    violated_aspects = list(policy_aspects)
    random.shuffle(violated_aspects)
    non_violated_aspects = tmp.difference(violated_aspects)

    log_entries_res = log_entries_uri(uuid.uuid4())
    log_entry_content_res = log_entry_uri(uuid.uuid4())

    g.add((log_entries_res, data_subject, user_uri(user_id)))
    g.add((log_entries_res, log_entry_content, log_entry_content_res))
    g.add((log_entries_res, transaction_time, rnd_transaction_time()))
    g.add((log_entries_res, RDF.type, Log_Entry))

    successful = False
    for v in violated_aspects:
        try:
            g.add(_generate_policy_violating_triple(
                v, policies, log_entry_content_res))
            if DEBUG:
                g.add((log_entry_content_res, violation_on, v))
            successful = True
            break
        except PolicyAspectCannotBeViolatedException:
            continue

    if not successful:
        raise ParticularPolicyCannotBeViolatedException()

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
         log_out_file_path, num_policy_aspects=None, num_user_policies=None):
    log_all = Graph()
    consent_all = Graph()

    for u in range(num_users):
        while True:
            try:
                user_id = uuid.uuid4()
                consent_rdf, policies = \
                    random_consent(
                        user_id, num_user_policies=num_user_policies,
                        num_policy_aspects=num_policy_aspects)
                consent_all += consent_rdf
                user_log = Graph()
                violations_counts = 0
                target_num_violation = int(log_size * percentage_of_violations / 100)

                for s in range(log_size):
                    if (violations_counts < target_num_violation) and \
                            (random.random() <= percentage_of_violations / 100):
                        num_trials = 0
                        while True:
                            num_trials += 1
                            try:
                                user_log += \
                                    create_violating_log_entry(policies, user_id)
                                break
                            except PolicyAspectCannotBeViolatedException:
                                pass
                            except PolicyCannotBeViolatedException:
                                raise RuntimeError(
                                    'Creating a violating policy not possible with current settings')
                        violations_counts += 1
                    else:
                        user_log += create_log_entry(policies, user_id)

                log_all += user_log
                # print(user_log.serialize(None, 'turtle').decode('utf-8'))
                print('********************************************************')
                print('Number of violating entries for user %s: %i' %
                      (user_id, violations_counts))
                print('********************************************************')
                break
            except ParticularPolicyCannotBeViolatedException:
                continue

    log_all.serialize(log_out_file_path, 'ntriples')
    consent_all.serialize(consent_out_file_path, 'turtle')

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('num_users', type=int)
    argparser.add_argument('log_size', type=int)
    argparser.add_argument('percentage_of_violations_per_user', type=int)
    argparser.add_argument('consent_output_file')
    argparser.add_argument('log_output_file')
    argparser.add_argument('--num_policy_aspects', type=int)
    argparser.add_argument('--num_user_policies', type=int)

    args = argparser.parse_args()
    main(
        args.num_users, args.log_size,
        args.percentage_of_violations_per_user,
        args.consent_output_file, args.log_output_file, args.num_policy_aspects,
        args.num_user_policies)

