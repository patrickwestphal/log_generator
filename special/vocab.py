from rdflib.term import URIRef

has_data = URIRef('http://www.specialprivacy.eu/langs/usage-policy#hasData')
has_duration = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#hasDuration')
has_location = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#hasLocation')
has_processing = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#hasProcessing')
has_purpose = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#hasPurpose')
has_recipient = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#hasRecipient')
has_storage = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#hasStorage')

has_data_subject =\
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#hasDataSubject')
has_policy = URIRef('http://www.specialprivacy.eu/vocabs/policy#simplePolicy')

data_subject = URIRef('http://www.specialprivacy.eu/langs/splog#dataSubject')
log_entry_content = \
    URIRef('http://www.specialprivacy.eu/langs/splog#logEntryContent')
transaction_time = \
    URIRef('http://www.specialprivacy.eu/langs/splog#transactionTime')

violation_on = \
    URIRef('http://dl-learner-org/debug/violationOn')

# ----------- classes ---------------------------------------------------------
Log_Entry = URIRef('http://www.specialprivacy.eu/langs/splog#LogEntry')
Log_Entry_Content = \
    URIRef('http://www.specialprivacy.eu/langs/splog#LogEntryContent')

Any_Data = URIRef('http://www.specialprivacy.eu/langs/usage-policy#AnyData')
Activity = URIRef('http://www.specialprivacy.eu/vocabs/data#Activity')
Anonymized = URIRef('http://www.specialprivacy.eu/vocabs/data#Anonymized')
Audiovisual_Activity = \
    URIRef('http://www.specialprivacy.eu/vocabs/data#AudiovisualActivity')
Computer = URIRef('http://www.specialprivacy.eu/vocabs/data#Computer')
Content = URIRef('http://www.specialprivacy.eu/vocabs/data#Content')
Demographic = URIRef('http://www.specialprivacy.eu/vocabs/data#Demographic')
Derived = URIRef('http://www.specialprivacy.eu/vocabs/data#Derived')
Financial = URIRef('http://www.specialprivacy.eu/vocabs/data#Financial')
Government_Data = URIRef('http://www.specialprivacy.eu/vocabs/data#Government')
Health_Data = URIRef('http://www.specialprivacy.eu/vocabs/data#Health')
Interactive = URIRef('http://www.specialprivacy.eu/vocabs/data#Interactive')
Judical = URIRef('http://www.specialprivacy.eu/vocabs/data#Judicial')
Location = URIRef('http://www.specialprivacy.eu/vocabs/data#Location')
Navigation = URIRef('http://www.specialprivacy.eu/vocabs/data#Navigation')
Online = URIRef('http://www.specialprivacy.eu/vocabs/data#Online')
Online_Activity = \
    URIRef('http://www.specialprivacy.eu/vocabs/data#OnlineActivity')
Physical = URIRef('http://www.specialprivacy.eu/vocabs/data#Physical')
Physical_Activity = \
    URIRef('http://www.specialprivacy.eu/vocabs/data#PhysicalActivity')
Political = URIRef('http://www.specialprivacy.eu/vocabs/data#Political')
Preference = URIRef('http://www.specialprivacy.eu/vocabs/data#Preference')
Profile = URIRef('http://www.specialprivacy.eu/vocabs/data#Profile')
Purchase = URIRef('http://www.specialprivacy.eu/vocabs/data#Purchase')
Social = URIRef('http://www.specialprivacy.eu/vocabs/data#Social')
State_Data = URIRef('http://www.specialprivacy.eu/vocabs/data#State')
Statistical = URIRef('http://www.specialprivacy.eu/vocabs/data#Statistical')
TelecomActivity = \
    URIRef('http://www.specialprivacy.eu/vocabs/data#TelecomActivity')
Unique_ID = URIRef('http://www.specialprivacy.eu/vocabs/data#UniqueId')

data_classes = [
    Any_Data, Activity, Anonymized, Audiovisual_Activity, Computer,
    Demographic, Derived, Financial, Government_Data, Health_Data, Interactive,
    Judical, Location, Navigation, Online, Online_Activity, Physical,
    Physical_Activity, Political, Preference, Profile, Purchase, Social,
    State_Data, Statistical, TelecomActivity, Unique_ID]

# --
Any_Duration = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#AnyDuration')
Business_Practices = \
    URIRef('http://www.specialprivacy.eu/vocabs/duration#BusinessPractices')
Indefinitely = \
    URIRef('http://www.specialprivacy.eu/vocabs/duration#Indefinitely')
Legal_Requirement = \
    URIRef('http://www.specialprivacy.eu/vocabs/duration#LegalRequirement')
Stated_Purpose = \
    URIRef('http://www.specialprivacy.eu/vocabs/duration#StatedPurpose')

# --
Any_Location = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#AnyLocation')
# Our_Servers = \
#     URIRef('http://www.specialprivacy.eu/langs/usage-policy#OurServers')
Our_Servers = \
    URIRef('http://www.specialprivacy.eu/vocabs/locations#OurServers')
Controller_Servers = \
    URIRef('http://www.specialprivacy.eu/vocabs/locations#ControllerServers')
EU = URIRef('http://www.specialprivacy.eu/vocabs/locations#EU')
EU_Like = URIRef('http://www.specialprivacy.eu/vocabs/locations#EULike')
Processors_Servers = \
    URIRef('http://www.specialprivacy.eu/vocabs/locations#ProcessorServers')
Third_Countries = \
    URIRef('http://www.specialprivacy.eu/vocabs/locations#ThirdCountries')
Third_Party = URIRef('http://www.specialprivacy.eu/vocabs/locations#ThirdParty')

location_classes = [
    Any_Location, Our_Servers, Controller_Servers, EU, EU_Like,
    Processors_Servers, Third_Countries, Third_Party]

# --
Any_Processing = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#AnyProcessing')
Aggregate = URIRef('http://www.specialprivacy.eu/vocabs/processing#Aggregate')
Analyze = URIRef('http://www.specialprivacy.eu/vocabs/processing#Analyze')
Anonymize = URIRef('http://www.specialprivacy.eu/vocabs/processing#Anonymize')
Collect = URIRef('http://www.specialprivacy.eu/vocabs/processing#Collect')
Copy = URIRef('http://www.specialprivacy.eu/vocabs/processing#Copy')
Derive = URIRef('http://www.specialprivacy.eu/vocabs/processing#Derive')
Move = URIRef('http://www.specialprivacy.eu/vocabs/processing#Move')
Query = URIRef('http://www.specialprivacy.eu/vocabs/processing#Query')
Transfer = URIRef('http://www.specialprivacy.eu/vocabs/processing#Transfer')

processing_classes = [
    Any_Processing, Aggregate, Analyze, Anonymize, Collect, Copy, Derive, Move,
    Query, Transfer]

# --
Any_Purpose = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#AnyPurpose')
Account = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Account')
Admin = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Admin')
Any_Contact = URIRef('http://www.specialprivacy.eu/vocabs/purposes#AnyContact')
Arts = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Arts')
Aux_Purpose = URIRef('http://www.specialprivacy.eu/vocabs/purposes#AuxPurpose')
Browsing = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Browsing')
Charity = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Charity')
Communicate = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Communicate')
Current = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Current')
Custom = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Custom')
Delivery_Purpose = \
    URIRef('http://www.specialprivacy.eu/vocabs/purposes#Delivery')
Develop = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Develop')
Downloads = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Downloads')
Education = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Education')
Feedback = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Feedback')
Finmgt = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Finmgt')
Gambling = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Gambling')
Gaming = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Gaming')
Government_Purpose = \
    URIRef('http://www.specialprivacy.eu/vocabs/purposes#Government')
Health_Purpose = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Health')
Historical = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Historical')
Login = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Login')
Marketing = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Marketing')
News = URIRef('http://www.specialprivacy.eu/vocabs/purposes#News')
Other_Contact = \
    URIRef('http://www.specialprivacy.eu/vocabs/purposes#OtherContact')
Payment = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Payment')
Sales = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Sales')
Search = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Search')
State_Purpose = URIRef('http://www.specialprivacy.eu/vocabs/purposes#State')
Tailoring = URIRef('http://www.specialprivacy.eu/vocabs/purposes#Tailoring')
Telemarketing = \
    URIRef('http://www.specialprivacy.eu/vocabs/purposes#Telemarketing')

purpose_classes = [
    Any_Purpose, Account, Admin, Any_Contact, Arts, Aux_Purpose, Browsing,
    Charity, Communicate, Current, Custom, Delivery_Purpose, Develop,
    Downloads, Education, Feedback, Finmgt, Gambling, Gaming,
    Government_Purpose, Health_Purpose, Historical, Login, Marketing, News,
    Other_Contact, Payment, Sales, Search, State_Purpose, Tailoring,
    Telemarketing]

# --
Any_Recipient = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#AnyRecipient')
Delivery_Recipient = \
    URIRef('http://www.specialprivacy.eu/vocabs/recipients#Delivery')
Other_Recipient = \
    URIRef('http://www.specialprivacy.eu/vocabs/recipients#OtherRecipient')
Ours = URIRef('http://www.specialprivacy.eu/vocabs/recipients#Ours')
Public = URIRef('http://www.specialprivacy.eu/vocabs/recipients#Public')
Same = URIRef('http://www.specialprivacy.eu/vocabs/recipients#Same')
Unrelated = URIRef('http://www.specialprivacy.eu/vocabs/recipients#Unrelated')

recipient_classes = [
    Any_Recipient, Delivery_Recipient, Other_Recipient, Ours, Public, Same,
    Unrelated]

# --
Any_Storage = \
    URIRef('http://www.specialprivacy.eu/langs/usage-policy#AnyStorage')


subclasses = {
    Any_Data: [
        Any_Data, Activity, Anonymized, Audiovisual_Activity, Computer,
        Content, Demographic, Derived, Financial, Government_Data, Health_Data,
        Interactive, Judical, Location, Navigation, Online, Online_Activity,
        Physical, Physical_Activity, Political, Preference, Profile, Purchase,
        Social, State_Data, Statistical, TelecomActivity, Any_Data],
    Activity: [
        Activity, Audiovisual_Activity, Online_Activity, Physical_Activity,
        TelecomActivity],
    Anonymized: [Anonymized],
    Audiovisual_Activity: [Audiovisual_Activity],
    Computer: [Computer],
    Content: [Content],
    Demographic: [Demographic],
    Derived: [Derived, Profile, Statistical],
    Financial: [Financial],
    Government_Data: [Government_Data],
    Health_Data: [Health_Data],
    Interactive: [Interactive],
    Judical: [Judical],
    Location: [Location],
    Navigation: [Navigation],
    Online: [Online],
    Online_Activity: [Online_Activity],
    Physical: [Physical],
    Physical_Activity: [Physical_Activity],
    Political: [Political],
    Preference: [Preference],
    Profile: [Profile],
    Purchase: [Purchase],
    Social: [Social],
    State_Data: [State_Data],
    Statistical: [Statistical],
    TelecomActivity: [TelecomActivity],
    Unique_ID: [Unique_ID],
    #
    Any_Duration: [
        Any_Duration, Business_Practices, Indefinitely, Legal_Requirement,
        Stated_Purpose],
    Business_Practices: [Business_Practices],
    Indefinitely: [Indefinitely],
    Legal_Requirement: [Legal_Requirement],
    Stated_Purpose: [Stated_Purpose],
    #
    Any_Location: [
        Any_Location, EU, EU_Like, Our_Servers, Controller_Servers,
        Processors_Servers, Third_Countries, Third_Party],
    Our_Servers: [Our_Servers, Controller_Servers, Processors_Servers],
    Controller_Servers: [Controller_Servers],
    EU: [EU],
    EU_Like: [EU_Like],
    Processors_Servers: [Processors_Servers],
    Third_Countries: [Third_Countries],
    Third_Party: [Third_Party],
    #
    Any_Processing: [
        Any_Processing, Aggregate, Anonymize, Collect, Copy, Derive, Analyze,
        Move, Query, Transfer],
    Derive: [Derive, Analyze],
    Aggregate: [Aggregate],
    Analyze: [Analyze],
    Anonymize: [Anonymize],
    Collect: [Collect],
    Copy: [Copy],
    Move: [Move],
    Query: [Query],
    Transfer: [Transfer],
    #
    Any_Purpose: [
        Any_Purpose, Admin, Any_Contact, Aux_Purpose, Account, Current, Arts,
        Browsing, Charity, Communicate, Custom, Delivery_Purpose, Develop,
        Downloads, Education, Feedback, Finmgt, Gambling, Gaming,
        Government_Purpose, Health_Purpose, Historical, Login, Marketing, News,
        Other_Contact, Payment, Sales, Search, State_Purpose, Tailoring,
        Telemarketing],
    Aux_Purpose: [
        Aux_Purpose, Account, Custom, Delivery_Purpose, Feedback, Login,
        Marketing, Payment, State_Purpose],
    Current: [
        Current, Arts, Browsing, Charity, Communicate, Downloads, Education,
        Finmgt, Gambling, Gaming, Government_Purpose, Health_Purpose, News,
        Sales, Search],
    Account: [Account],
    Admin: [Admin],
    Any_Contact: [Any_Contact, Other_Contact, Telemarketing],
    Arts: [Arts],
    Browsing: [Browsing],
    Charity: [Charity],
    Communicate: [Communicate],
    Custom: [Custom],
    Delivery_Purpose: [Delivery_Purpose],
    Develop: [Develop],
    Downloads: [Downloads],
    Education: [Education],
    Feedback: [Feedback],
    Finmgt: [Finmgt],
    Gambling: [Gambling],
    Gaming: [Gaming],
    Government_Purpose: [Government_Purpose],
    Health_Purpose: [Health_Purpose],
    Historical: [Historical],
    Login: [Login],
    Marketing: [Marketing],
    News: [News],
    Other_Contact: [Other_Contact],
    Payment: [Payment],
    Sales: [Sales],
    Search: [Search],
    State_Purpose: [State_Purpose],
    Tailoring: [Tailoring],
    Telemarketing: [Telemarketing],
    #
    Any_Recipient: [
        Any_Recipient, Delivery_Recipient, Other_Recipient, Any_Recipient,
        Public, Same, Unrelated],
    Delivery_Recipient: [Delivery_Recipient],
    Other_Recipient: [Other_Recipient],
    Ours: [Ours],
    Public: [Public],
    Same: [Same],
    Unrelated: [Unrelated],
    #
    Any_Storage: [Any_Storage]
}