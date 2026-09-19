"""
Curated Offline Exercise Bank & Random Generator for English Buddy Bot.

Features:
- Exactly 108 distinct, pedagogically categorized exercises (6 tracks x 3 CEFR levels x 6 exercises).
- Sub-millisecond O(1) in-memory retrieval (uses under 100 KB RAM; zero performance impact).
- Consecutive duplicate suppression with exclude_id tracking.
- Contextual offline feedback generation when AI service is unconfigured or offline.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

import config

EXERCISE_BANK: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
    # =========================================================================
    # 1. 💬 DAILY CONVERSATION (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # =========================================================================
    config.MODE_DAILY_CONVERSATION: {
        config.LEVEL_BEGINNER: [
            {
                "id": "conv_beg_01",
                "badge": "💬 Fast Food Counter",
                "prompt": (
                    "<b>🍔 Scenario:</b> You are at a burger counter.\n\n"
                    "<b>Cashier:</b> <i>\"Hello! What can I get for you today? Meal or just the sandwich?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Reply with your order (food, drink, and if you want it for dine-in or takeaway)!"
                ),
            },
            {
                "id": "conv_beg_02",
                "badge": "💬 Asking for Directions",
                "prompt": (
                    "<b>🗺️ Scenario:</b> You are looking for the central train station.\n\n"
                    "<b>Local Passerby:</b> <i>\"Excuse me, you look a bit lost. Can I help you find something?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Ask politely how to get to the train station on foot!"
                ),
            },
            {
                "id": "conv_beg_03",
                "badge": "💬 Checking in at a Hotel",
                "prompt": (
                    "<b>🏨 Scenario:</b> You arrive at the hotel reception desk after a long flight.\n\n"
                    "<b>Receptionist:</b> <i>\"Good evening! Welcome to The Grand Hotel. Checking in tonight?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Greet the receptionist, state that you have a reservation under your name, and ask about breakfast hours!"
                ),
            },
            {
                "id": "conv_beg_04",
                "badge": "💬 Grocery Shopping",
                "prompt": (
                    "<b>🍎 Scenario:</b> You cannot find eggs in the supermarket.\n\n"
                    "<b>Staff Member:</b> <i>\"Hi there, need help finding anything in aisle four?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Ask where the fresh eggs and dairy products are located!"
                ),
            },
            {
                "id": "conv_beg_05",
                "badge": "💬 Rideshare / Taxi",
                "prompt": (
                    "<b>🚕 Scenario:</b> You get into a taxi outside the airport.\n\n"
                    "<b>Driver:</b> <i>\"Afternoon! Where are we heading today?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> State your destination hotel and ask approximately how long the trip will take!"
                ),
            },
            {
                "id": "conv_beg_06",
                "badge": "💬 Introducing Yourself",
                "prompt": (
                    "<b>👋 Scenario:</b> A new neighbor moves in next door.\n\n"
                    "<b>Neighbor:</b> <i>\"Hi! I just moved into apartment 3B today. I'm Alex.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Introduce yourself warmly, welcome them to the building, and offer help if needed!"
                ),
            },
        ],
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "conv_int_01",
                "badge": "💬 Returning a Defective Item",
                "prompt": (
                    "<b>🛍️ Scenario:</b> The headphones you bought yesterday have a crackling left speaker.\n\n"
                    "<b>Store Associate:</b> <i>\"Hi there! How can I assist you at Customer Service today?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Explain the defect politely, mention you have the receipt, and ask for a replacement or refund!"
                ),
            },
            {
                "id": "conv_int_02",
                "badge": "💬 Weekend Plans with a Colleague",
                "prompt": (
                    "<b>☕ Scenario:</b> It's Friday afternoon by the office coffee machine.\n\n"
                    "<b>Colleague:</b> <i>\"Finally Friday! Are you doing anything exciting or just taking it easy this weekend?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Share two activities you have planned and ask about their weekend plans!"
                ),
            },
            {
                "id": "conv_int_03",
                "badge": "💬 Negotiating a Project Deadline",
                "prompt": (
                    "<b>📊 Scenario:</b> Your project workload is higher than anticipated.\n\n"
                    "<b>Manager:</b> <i>\"Can we still lock in the final design report for this Monday morning?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Explain why Monday is tight, propose Wednesday instead, and emphasize maintaining quality!"
                ),
            },
            {
                "id": "conv_int_04",
                "badge": "💬 Apartment Viewing",
                "prompt": (
                    "<b>🔑 Scenario:</b> You are viewing a rental apartment with the landlord.\n\n"
                    "<b>Landlord:</b> <i>\"The rent is $1,200 monthly. Any specific questions before we wrap up the tour?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Inquire whether utilities are included and ask about the pet policy!"
                ),
            },
            {
                "id": "conv_int_05",
                "badge": "💬 Doctor's Appointment",
                "prompt": (
                    "<b>🩺 Scenario:</b> You have been feeling unwell for three days.\n\n"
                    "<b>Doctor:</b> <i>\"Hello. What symptoms have you been experiencing recently?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Describe having a persistent headache, fatigue, and ask if a prescription is needed!"
                ),
            },
            {
                "id": "conv_int_06",
                "badge": "💬 Flight Delay Rescheduling",
                "prompt": (
                    "<b>✈️ Scenario:</b> Your connecting flight was cancelled due to bad weather.\n\n"
                    "<b>Airline Agent:</b> <i>\"We apologize for the inconvenience. Let me see what other flights we have open.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Express understanding while asking if you can be placed on the earliest morning flight with hotel vouchers!"
                ),
            },
        ],
        config.LEVEL_ADVANCED: [
            {
                "id": "conv_adv_01",
                "badge": "💬 Diplomatic Disagreement",
                "prompt": (
                    "<b>💼 Scenario:</b> A teammate suggests skipping end-to-end security audits to meet a launch date.\n\n"
                    "<b>Team Lead:</b> <i>\"It seems risky, but does anyone strongly object to shipping without full audits?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Express diplomatic disagreement using professional hedging (e.g., <i>'While I appreciate the urgency...'</i>) and articulate the compliance risks!"
                ),
            },
            {
                "id": "conv_adv_02",
                "badge": "💬 De-escalating an Irate Client",
                "prompt": (
                    "<b>📞 Scenario:</b> A high-value corporate client complains about a delivery milestone.\n\n"
                    "<b>Client:</b> <i>\"This timeline is completely unacceptable! We never signed off on a two-week delay!\"</i>\n\n"
                    "👉 <b>Your Turn:</b> De-escalate empathetically without accepting undue blame, and steer them toward a concrete compromise!"
                ),
            },
            {
                "id": "conv_adv_03",
                "badge": "💬 Performance Review & Promotion",
                "prompt": (
                    "<b>📈 Scenario:</b> You are in your annual performance review discussing promotion.\n\n"
                    "<b>Executive:</b> <i>\"You've done solid work this year. Where do you see your contribution expanding next quarter?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Confidently outline your measurable accomplishments, pitch your readiness for senior leadership, and request the title change!"
                ),
            },
            {
                "id": "conv_adv_04",
                "badge": "💬 Cross-Cultural Negotiation",
                "prompt": (
                    "<b>🤝 Scenario:</b> An international partner hesitates on exclusivity terms.\n\n"
                    "<b>Partner:</b> <i>\"In our market, exclusive contracts are viewed with substantial skepticism.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Bridge the cultural gap gracefully, validating their business culture while proposing a phased milestone-based commitment!"
                ),
            },
            {
                "id": "conv_adv_05",
                "badge": "💬 Public Relations Crisis",
                "prompt": (
                    "<b>🎙️ Scenario:</b> A journalist questions you about an unexpected server outage affecting users.\n\n"
                    "<b>Journalist:</b> <i>\"Are user credentials compromised, and why did it take three hours to notify customers?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Deliver a poised, reassuring statement emphasizing transparent investigation, zero data breaches, and concrete remediations!"
                ),
            },
            {
                "id": "conv_adv_06",
                "badge": "💬 Venture Capital Pitch",
                "prompt": (
                    "<b>💡 Scenario:</b> An investor challenges your startup's competitive barrier.\n\n"
                    "<b>Investor:</b> <i>\"What prevents a tech giant from cloning your solution within six months?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Defend your competitive moat persuasively, highlighting proprietary datasets, network effects, and agility!"
                ),
            },
        ],
    },
    # =========================================================================
    # 2. 📚 VOCABULARY (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # =========================================================================
    config.MODE_VOCABULARY: {
        config.LEVEL_BEGINNER: [
            {
                "id": "voc_beg_01",
                "badge": "📚 Word: Convenient",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Convenient</code> <i>/kənˈviː.ni.ənt/</i> (adjective)\n\n"
                    "<b>Meaning:</b> Fitting in well with a person's needs, activities, or easy to use.\n"
                    "<b>Example:</b> <i>\"The metro station is very convenient because it's near my home.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Write a sentence about an app or service that is <b>convenient</b> for you!"
                ),
            },
            {
                "id": "voc_beg_02",
                "badge": "📚 Word: Recommend",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Recommend</code> <i>/ˌrek.əˈmend/</i> (verb)\n\n"
                    "<b>Meaning:</b> To suggest something as good or suitable for a purpose.\n"
                    "<b>Example:</b> <i>\"Can you recommend a good café in town?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Reply by <b>recommending</b> your favorite movie or book in one sentence!"
                ),
            },
            {
                "id": "voc_beg_03",
                "badge": "📚 Word: Affordable",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Affordable</code> <i>/əˈfɔː.də.bəl/</i> (adjective)\n\n"
                    "<b>Meaning:</b> Reasonably priced; not too expensive.\n"
                    "<b>Example:</b> <i>\"They offer delicious meals at very affordable prices.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Write a sentence using <b>affordable</b> to describe something you bought!"
                ),
            },
            {
                "id": "voc_beg_04",
                "badge": "📚 Word: Delicious",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Delicious</code> <i>/dɪˈlɪʃ.əs/</i> (adjective)\n\n"
                    "<b>Meaning:</b> Having a very pleasant taste or smell.\n"
                    "<b>Example:</b> <i>\"This homemade apple pie is absolutely delicious.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Mention your favorite food and explain why it is <b>delicious</b>!"
                ),
            },
            {
                "id": "voc_beg_05",
                "badge": "📚 Word: Necessary",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Necessary</code> <i>/ˈnes.ə.ser.i/</i> (adjective)\n\n"
                    "<b>Meaning:</b> Needed to be done, achieved, or present; essential.\n"
                    "<b>Example:</b> <i>\"A passport is necessary for international travel.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> What is one tool or habit that is <b>necessary</b> for your daily work?"
                ),
            },
            {
                "id": "voc_beg_06",
                "badge": "📚 Word: Immediately",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Immediately</code> <i>/ɪˈmiː.di.ət.li/</i> (adverb)\n\n"
                    "<b>Meaning:</b> At once; without any delay.\n"
                    "<b>Example:</b> <i>\"When the alarm rang, she immediately woke up.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Create a sentence describing an action you take <b>immediately</b> in the morning!"
                ),
            },
        ],
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "voc_int_01",
                "badge": "📚 Phrasal Verb: Figure Out",
                "prompt": (
                    "🌟 <b>Phrasal Verb:</b> <code>Figure out</code>\n\n"
                    "<b>Meaning:</b> To solve a problem or understand something after thinking.\n"
                    "<b>Example:</b> <i>\"We spent hours trying to figure out why the program crashed.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Describe a riddle or situation you had to <b>figure out</b> recently!"
                ),
            },
            {
                "id": "voc_int_02",
                "badge": "📚 Word: Resilient",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Resilient</code> <i>/rɪˈzɪl.i.ənt/</i> (adjective)\n\n"
                    "<b>Meaning:</b> Able to recover quickly from difficult conditions or setbacks.\n"
                    "<b>Example:</b> <i>\"The team remained resilient despite falling behind in the first half.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Use <b>resilient</b> to describe an inspiring person or company!"
                ),
            },
            {
                "id": "voc_int_03",
                "badge": "📚 Phrasal Verb: Call Off",
                "prompt": (
                    "🌟 <b>Phrasal Verb:</b> <code>Call off</code>\n\n"
                    "<b>Meaning:</b> To cancel an event, match, or agreement.\n"
                    "<b>Example:</b> <i>\"They had to call off the outdoor festival due to heavy thunderstorm warnings.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Write a sentence using <b>call off</b> about an event or meeting!"
                ),
            },
            {
                "id": "voc_int_04",
                "badge": "📚 Word: Procrastinate",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Procrastinate</code> <i>/prəˈkræs.tɪ.neɪt/</i> (verb)\n\n"
                    "<b>Meaning:</b> To delay or postpone action; put off doing something.\n"
                    "<b>Example:</b> <i>\"I always procrastinate when it comes to cleaning the garage.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> What chore do you tend to <b>procrastinate</b> on, and why?"
                ),
            },
            {
                "id": "voc_int_05",
                "badge": "📚 Word: Reluctant",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Reluctant</code> <i>/rɪˈlʌk.tənt/</i> (adjective)\n\n"
                    "<b>Meaning:</b> Unwilling and hesitant; disinclined.\n"
                    "<b>Example:</b> <i>\"He was reluctant to commit without seeing the final contract.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Describe a time you felt <b>reluctant</b> to try something new!"
                ),
            },
            {
                "id": "voc_int_06",
                "badge": "📚 Phrasal Verb: Bring Up",
                "prompt": (
                    "🌟 <b>Phrasal Verb:</b> <code>Bring up</code>\n\n"
                    "<b>Meaning:</b> To introduce a topic into a conversation or meeting.\n"
                    "<b>Example:</b> <i>\"I didn't want to bring up the budget issues during the celebration.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Send a sentence about an important topic you plan to <b>bring up</b> soon!"
                ),
            },
        ],
        config.LEVEL_ADVANCED: [
            {
                "id": "voc_adv_01",
                "badge": "📚 Word: Equivocal",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Equivocal</code> <i>/ɪˈkwɪv.ə.kəl/</i> (adjective)\n\n"
                    "<b>Meaning:</b> Open to more than one interpretation; deliberately ambiguous.\n"
                    "<b>Example:</b> <i>\"The spokesperson's equivocal remarks sparked intense speculation among analysts.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Construct a sentence contrasting an <b>equivocal</b> answer with an unambiguous commitment!"
                ),
            },
            {
                "id": "voc_adv_02",
                "badge": "📚 Collocation: Paradigm Shift",
                "prompt": (
                    "🌟 <b>Collocation:</b> <code>Paradigm shift</code> (noun phrase)\n\n"
                    "<b>Meaning:</b> A fundamental change in approach, mindset, or underlying assumptions.\n"
                    "<b>Example:</b> <i>\"Remote collaboration tools catalyzed a paradigm shift in corporate culture.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Name an industry that has undergone a <b>paradigm shift</b> and explain why!"
                ),
            },
            {
                "id": "voc_adv_03",
                "badge": "📚 Word: Ubiquitous",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Ubiquitous</code> <i>/juːˈbɪk.wɪ.təs/</i> (adjective)\n\n"
                    "<b>Meaning:</b> Present, appearing, or found everywhere simultaneously.\n"
                    "<b>Example:</b> <i>\"Smartphones have become ubiquitous across every demographic over the past decade.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Use <b>ubiquitous</b> to describe a modern technology or cultural trend!"
                ),
            },
            {
                "id": "voc_adv_04",
                "badge": "📚 Word: Ephemeral",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Ephemeral</code> <i>/ɪˈfem.ər.əl/</i> (adjective)\n\n"
                    "<b>Meaning:</b> Lasting for a very short time; transitory; fleeting.\n"
                    "<b>Example:</b> <i>\"Fame on social media is often ephemeral, fading as quickly as it emerges.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Describe a natural phenomenon or emotion that is purely <b>ephemeral</b>!"
                ),
            },
            {
                "id": "voc_adv_05",
                "badge": "📚 Word: Pragmatic",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Pragmatic</code> <i>/præɡˈmæt.ɪk/</i> (adjective)\n\n"
                    "<b>Meaning:</b> Dealing with things sensibly and realistically based on practical rather than theoretical considerations.\n"
                    "<b>Example:</b> <i>\"We chose a pragmatic architecture that prioritized uptime over untested features.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Use <b>pragmatic</b> to describe an effective decision-making style!"
                ),
            },
            {
                "id": "voc_adv_06",
                "badge": "📚 Word: Circumlocution",
                "prompt": (
                    "🌟 <b>Word:</b> <code>Circumlocution</code> <i>/ˌsɜː.kəm.ləˈkjuː.ʃən/</i> (noun)\n\n"
                    "<b>Meaning:</b> The use of many words where fewer would do, especially in a deliberate attempt to be vague or evasive.\n"
                    "<b>Example:</b> <i>\"His response was a masterclass in political circumlocution that answered nothing.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Formulate a sentence criticizing excessive <b>circumlocution</b> in formal correspondence!"
                ),
            },
        ],
    },
    # =========================================================================
    # 3. ✏️ GRAMMAR (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # =========================================================================
    config.MODE_GRAMMAR: {
        config.LEVEL_BEGINNER: [
            {
                "id": "grm_beg_01",
                "badge": "✏️ Present Simple vs Continuous",
                "prompt": (
                    "🔍 <b>Spot the mistake:</b>\n\n"
                    "❌ <code>\"Look! It rains outside right now, so take an umbrella.\"</code>\n\n"
                    "👉 <b>Your Turn:</b> Send the corrected sentence and explain why <i>'is raining'</i> is required!"
                ),
            },
            {
                "id": "grm_beg_02",
                "badge": "✏️ Prepositions of Time (At / On / In)",
                "prompt": (
                    "🔍 <b>Fix the prepositions:</b>\n\n"
                    "❌ <code>\"Our flight departs in Monday at 9:00 in night.\"</code>\n\n"
                    "👉 <b>Your Turn:</b> Rewrite using correct prepositions for days, times, and night!"
                ),
            },
            {
                "id": "grm_beg_03",
                "badge": "✏️ Past Simple Irregular Verbs",
                "prompt": (
                    "🔍 <b>Find and correct the irregular past tense error:</b>\n\n"
                    "❌ <code>\"Yesterday she buyed three books and catched the express train home.\"</code>\n\n"
                    "👉 <b>Your Turn:</b> Send the corrected sentence with proper irregular forms!"
                ),
            },
            {
                "id": "grm_beg_04",
                "badge": "✏️ Comparative Adjectives",
                "prompt": (
                    "🔍 <b>Spot the adjective error:</b>\n\n"
                    "❌ <code>\"This new laptop is more cheap and more fast than my old one.\"</code>\n\n"
                    "👉 <b>Your Turn:</b> Rewrite with the correct comparative forms of <i>cheap</i> and <i>fast</i>!"
                ),
            },
            {
                "id": "grm_beg_05",
                "badge": "✏️ Countable vs Uncountable Nouns",
                "prompt": (
                    "🔍 <b>Correct the quantifier mistake:</b>\n\n"
                    "❌ <code>\"Can you give me a few advices? I don't have many informations about the exam.\"</code>\n\n"
                    "👉 <b>Your Turn:</b> Send the grammatically correct version for <i>advice</i> and <i>information</i>!"
                ),
            },
            {
                "id": "grm_beg_06",
                "badge": "✏️ Question Word Order",
                "prompt": (
                    "🔍 <b>Rearrange into a correct interrogative sentence:</b>\n\n"
                    "❌ <code>\"Where you did go for vacation last summer?\"</code>\n\n"
                    "👉 <b>Your Turn:</b> Send the properly ordered past tense question!"
                ),
            },
        ],
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "grm_int_01",
                "badge": "✏️ Second Conditional",
                "prompt": (
                    "🔍 <b>Complete the hypothetical conditional sentence:</b>\n\n"
                    "<i>\"If I _______ (have) more free time, I _______ (travel) across South America.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Fill in both blanks using correct Second Conditional forms and explain your choice!"
                ),
            },
            {
                "id": "grm_int_02",
                "badge": "✏️ Subject-Verb Agreement",
                "prompt": (
                    "🔍 <b>Identify and fix the agreement error:</b>\n\n"
                    "❌ <code>\"Everyone in our department have agreed to participate in the marathon.\"</code>\n\n"
                    "👉 <b>Your Turn:</b> Send the corrected version and state the rule for indefinite pronouns like <i>'everyone'</i>!"
                ),
            },
            {
                "id": "grm_int_03",
                "badge": "✏️ Present Perfect vs Past Simple",
                "prompt": (
                    "🔍 <b>Choose the correct tense and fix the error:</b>\n\n"
                    "❌ <code>\"I have finished that project two weeks ago, but my manager hasn't reviewed it yet.\"</code>\n\n"
                    "👉 <b>Your Turn:</b> Correct the sentence and explain why a specific time marker changes the tense!"
                ),
            },
            {
                "id": "grm_int_04",
                "badge": "✏️ Passive Voice in Reporting",
                "prompt": (
                    "🔍 <b>Convert from Active to Passive voice:</b>\n\n"
                    "Active: <i>\"The research committee published the climate findings yesterday.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Rewrite the sentence in the passive voice, emphasizing the findings!"
                ),
            },
            {
                "id": "grm_int_05",
                "badge": "✏️ Gerund vs Infinitive",
                "prompt": (
                    "🔍 <b>Fill in the blanks with the correct verb form (gerund or infinitive):</b>\n\n"
                    "<i>\"She stopped _______ (smoke) five years ago, but on her drive home she stopped _______ (buy) some groceries.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Supply both forms and explain the difference in meaning!"
                ),
            },
            {
                "id": "grm_int_06",
                "badge": "✏️ Defining vs Non-Defining Relative Clauses",
                "prompt": (
                    "🔍 <b>Add commas where necessary:</b>\n\n"
                    "Sentence: <i>\"My brother who lives in Tokyo is coming to visit next week.\"</i> (Note: You only have one brother).\n\n"
                    "👉 <b>Your Turn:</b> Punctuate correctly and explain whether this is defining or non-defining!"
                ),
            },
        ],
        config.LEVEL_ADVANCED: [
            {
                "id": "grm_adv_01",
                "badge": "✏️ Inversion for Emphasis",
                "prompt": (
                    "🔍 <b>Transform this sentence into an inverted structure:</b>\n\n"
                    "Standard: <i>\"I have rarely witnessed such dedication from an engineering team.\"</i>\n"
                    "Start with: <b>\"Rarely...\"</b>\n\n"
                    "👉 <b>Your Turn:</b> Complete the inverted sentence with proper auxiliary-subject word order!"
                ),
            },
            {
                "id": "grm_adv_02",
                "badge": "✏️ Mixed Conditionals",
                "prompt": (
                    "🔍 <b>Construct a Mixed Conditional (Past Action -> Present Result):</b>\n\n"
                    "Situation: You did not accept the overseas job offer last year (past), so you do not live in London today (present).\n\n"
                    "👉 <b>Your Turn:</b> Combine these into a single mixed conditional sentence!"
                ),
            },
            {
                "id": "grm_adv_03",
                "badge": "✏️ Subjunctive Mood",
                "prompt": (
                    "🔍 <b>Fix the subjunctive verb form:</b>\n\n"
                    "❌ <code>\"The board insisted that the chief architect resigns immediately following the audit.\"</code>\n\n"
                    "👉 <b>Your Turn:</b> Correct the sentence using the formal mandate subjunctive form!"
                ),
            },
            {
                "id": "grm_adv_04",
                "badge": "✏️ Cleft Sentences for Focus",
                "prompt": (
                    "🔍 <b>Reframe using a 'What-cleft' sentence:</b>\n\n"
                    "Original: <i>\"We desperately need a reliable data pipeline to scale our models.\"</i>\n"
                    "Start with: <b>\"What we desperately need...\"</b>\n\n"
                    "👉 <b>Your Turn:</b> Formulate the complete cleft sentence to emphasize the requirement!"
                ),
            },
            {
                "id": "grm_adv_05",
                "badge": "✏️ Participle Clauses for Conciseness",
                "prompt": (
                    "🔍 <b>Combine these two sentences using a perfect participle clause:</b>\n\n"
                    "Sentence A: <i>\"She had completed the exhaustive clinical trials.\"</i>\n"
                    "Sentence B: <i>\"She submitted the breakthrough pharmaceutical report to regulators.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Merge them beginning with <b>'Having...'</b>!"
                ),
            },
            {
                "id": "grm_adv_06",
                "badge": "✏️ Modals of Past Deduction",
                "prompt": (
                    "🔍 <b>Choose between 'must have', 'can't have', or 'should have':</b>\n\n"
                    "Scenario: The keys were on the kitchen table five minutes ago, and nobody entered the house.\n"
                    "Sentence: <i>\"They _______ (vanish) into thin air!\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Fill in the past deduction modal and justify your logical certainty!"
                ),
            },
        ],
    },
    # =========================================================================
    # 4. 📖 READING (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # =========================================================================
    config.MODE_READING: {
        config.LEVEL_BEGINNER: [
            {
                "id": "rdg_beg_01",
                "badge": "📖 The Sunday Market",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Every Sunday morning, Sarah visits the open-air market near the harbor. She buys fresh sourdough bread, sweet strawberries, and local honey directly from farmers. She prefers buying here rather than supermarkets because the food is fresher and she loves chatting with the vendors.\"</i>\n\n"
                    "❓ <b>Question:</b> Name two reasons why Sarah prefers the market over supermarkets.\n\n"
                    "👉 <b>Your Turn:</b> Answer in 1–2 complete English sentences!"
                ),
            },
            {
                "id": "rdg_beg_02",
                "badge": "📖 The Adopted Puppy",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Tom adopted an energetic golden puppy named Toby from the animal shelter. At first, Toby was shy and hid under the sofa. But after a warm bowl of food and a squeaky toy, Toby began wagging his tail and following Tom everywhere around the house.\"</i>\n\n"
                    "❓ <b>Question:</b> How did Toby's behavior change after getting food and a toy?\n\n"
                    "👉 <b>Your Turn:</b> Reply with your answer!"
                ),
            },
            {
                "id": "rdg_beg_03",
                "badge": "📖 The City Library",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"The central city library is more than a quiet room with books. On the second floor, visitors can borrow laptops, attend weekly language exchange clubs, or practice digital photography in a free studio. It is open seven days a week to all residents.\"</i>\n\n"
                    "❓ <b>Question:</b> Mention two free activities visitors can do on the second floor.\n\n"
                    "👉 <b>Your Turn:</b> Send your answer below!"
                ),
            },
            {
                "id": "rdg_beg_04",
                "badge": "📖 Morning Bicycle Commute",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Elena rides her bicycle to work every morning. Her commute takes twenty-five minutes through a scenic park. She says cycling helps her wake up naturally without relying on multiple cups of strong espresso.\"</i>\n\n"
                    "❓ <b>Question:</b> Why does Elena choose to cycle through the park each morning?\n\n"
                    "👉 <b>Your Turn:</b> Write your response!"
                ),
            },
            {
                "id": "rdg_beg_05",
                "badge": "📖 Cooking Traditional Soup",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Marco's grandmother taught him that the secret to great chicken soup is simmering the broth gently for at least four hours. Boiling it too fast makes the stock cloudy and causes the vegetables to lose their vibrant flavor.\"</i>\n\n"
                    "❓ <b>Question:</b> What happens to the soup if you boil it too quickly?\n\n"
                    "👉 <b>Your Turn:</b> Reply in complete sentences!"
                ),
            },
            {
                "id": "rdg_beg_06",
                "badge": "📖 The Backyard Greenhouse",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"In his small backyard greenhouse, Liam grows cherry tomatoes and basil all winter. The glass roof traps radiant heat from the sun, maintaining an indoor temperature ten degrees warmer than the freezing outdoor air.\"</i>\n\n"
                    "❓ <b>Question:</b> How does the greenhouse maintain a warm temperature during winter?\n\n"
                    "👉 <b>Your Turn:</b> Send your answer!"
                ),
            },
        ],
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "rdg_int_01",
                "badge": "📖 The Pomodoro Technique",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Developed by Francesco Cirillo in the late 1980s, the Pomodoro Technique utilizes a timer to divide work into 25-minute intervals, punctuated by 5-minute rest breaks. Neuroscientists suggest that these frequent pauses prevent mental fatigue and sustain dopamine levels, countering the urge to multitask.\"</i>\n\n"
                    "❓ <b>Question:</b> According to neuroscientists, how do brief breaks benefit productivity?\n\n"
                    "👉 <b>Your Turn:</b> Summarize the benefit in your own words!"
                ),
            },
            {
                "id": "rdg_int_02",
                "badge": "📖 Urban Heat Islands",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Urban centers frequently experience temperatures 2 to 5 degrees Celsius higher than neighboring countryside—a condition called the Urban Heat Island effect. Concrete and asphalt absorb solar radiation by day and release it gradually at night. Rooftop vegetation helps reflect sunlight and cool ambient air.\"</i>\n\n"
                    "❓ <b>Question:</b> What causes cities to retain warmth overnight compared to rural areas?\n\n"
                    "👉 <b>Your Turn:</b> Answer based on the text!"
                ),
            },
            {
                "id": "rdg_int_03",
                "badge": "📖 The Discovery of Coffee",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Legend holds that Ethiopian goat herder Kaldi first discovered coffee around 850 AD. He noticed his herd became unusually energetic and refused to sleep after nibbling bright red berries from an unfamiliar shrub. Local monks subsequently brewed the berries into a decoction to sustain wakefulness during lengthy evening prayers.\"</i>\n\n"
                    "❓ <b>Question:</b> What first alerted Kaldi to the stimulating properties of the berries?\n\n"
                    "👉 <b>Your Turn:</b> Explain the discovery briefly!"
                ),
            },
            {
                "id": "rdg_int_04",
                "badge": "📖 Sleep Cycles & Memory",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"During Rapid Eye Movement (REM) sleep, the human brain replays neural sequences recorded throughout waking hours. Researchers at Harvard demonstrated that individuals who enjoy uninterrupted REM cycles score significantly higher on complex problem-solving assessments compared to sleep-deprived subjects.\"</i>\n\n"
                    "❓ <b>Question:</b> What crucial cognitive function occurs in the brain during REM sleep?\n\n"
                    "👉 <b>Your Turn:</b> Reply with your analysis!"
                ),
            },
            {
                "id": "rdg_int_05",
                "badge": "📖 Electric Vehicles in Winter",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Sub-zero temperatures diminish lithium-ion battery range by slowing chemical reactions and requiring substantial energy to heat the cabin. Modern automotive engineers mitigate this penalty by integrating heat pump exchangers that repurpose waste heat from the electric motor.\"</i>\n\n"
                    "❓ <b>Question:</b> How do modern electric vehicles offset winter battery range degradation?\n\n"
                    "👉 <b>Your Turn:</b> Send your answer!"
                ),
            },
            {
                "id": "rdg_int_06",
                "badge": "📖 The Psychology of Clutter",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"A crowded visual field competes for neural resources, elevating cortisol levels and impairing working memory. In a study involving 200 remote professionals, decluttering workspaces correlated with a measurable 28% drop in perceived daily stress.\"</i>\n\n"
                    "❓ <b>Question:</b> Why does a cluttered physical environment impair cognitive performance?\n\n"
                    "👉 <b>Your Turn:</b> State the psychological explanation!"
                ),
            },
        ],
        config.LEVEL_ADVANCED: [
            {
                "id": "rdg_adv_01",
                "badge": "📖 Cognitive Offloading",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Cognitive offloading—relying on digital algorithms and external memory aids to reduce mental exertion—sparks fierce scientific debate. Proponents argue that delegating rote computation liberates neural capacity for imaginative synthesis. Conversely, cognitive psychologists warn that chronic offloading atrophies intrinsic navigational mapping and deep analytical recall.\"</i>\n\n"
                    "❓ <b>Question:</b> Contrast the primary argument supporting cognitive offloading with the hazard identified by psychologists.\n\n"
                    "👉 <b>Your Turn:</b> Synthesize both perspectives critically!"
                ),
            },
            {
                "id": "rdg_adv_02",
                "badge": "📖 Deep-Sea Mining Dilemma",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Polymetallic nodules resting on the abyssal plains harbor dense concentrations of cobalt and nickel—elements indispensable for renewable battery manufacturing. Nonetheless, marine biologists caution that sediment plumes generated by robotic extraction may asphyxiate fragile benthic fauna adapted to millenia of undisturbed stability.\"</i>\n\n"
                    "❓ <b>Question:</b> What fundamental ecological paradox characterizes the deep-sea mining debate?\n\n"
                    "👉 <b>Your Turn:</b> Articulate the conflict between green technology and marine preservation!"
                ),
            },
            {
                "id": "rdg_adv_03",
                "badge": "📖 Algorithmic Bias in Hiring",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Automated candidate screening systems trained on historical promotion metrics often inadvertently codify legacy demographic disparities. When historical training corpora disproportionately feature homogeneous managerial cohorts, predictive models penalize unconventional career trajectories, masking systemic discrimination under an aura of mathematical objectivity.\"</i>\n\n"
                    "❓ <b>Question:</b> How does reliance on historical corporate data perpetuate recruitment bias?\n\n"
                    "👉 <b>Your Turn:</b> Formulate your analytical critique!"
                ),
            },
            {
                "id": "rdg_adv_04",
                "badge": "📖 Biomimicry in Aviation",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Aeronautical engineers studying humpback whale flippers discovered that scalloped leading edges (tubercles) channel airflow into localized vortices, delaying stall angles by eight degrees while cutting aerodynamic drag by 32%. Adapting these biological geometries to turbine blades yields unprecedented fuel efficiencies.\"</i>\n\n"
                    "❓ <b>Question:</b> In what technical manner do whale tubercles improve aerodynamic performance?\n\n"
                    "👉 <b>Your Turn:</b> Summarize the biomechanical principle!"
                ),
            },
            {
                "id": "rdg_adv_05",
                "badge": "📖 The Architecture of Silence",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"Acoustic ecologists argue that anthropogenic ambient noise constitutes a pervasive pollutant, inducing chronic sympathetic nervous activation. Urban architects in Scandinavia increasingly incorporate acoustic baffle gardens—terraced moss walls and resonant water features—engineered to dissipate industrial frequencies into calming pink noise.\"</i>\n\n"
                    "❓ <b>Question:</b> How do acoustic baffle gardens transform harsh urban soundscapes?\n\n"
                    "👉 <b>Your Turn:</b> Send your interpretation!"
                ),
            },
            {
                "id": "rdg_adv_06",
                "badge": "📖 The Economics of Attention",
                "prompt": (
                    "📄 <b>Passage:</b>\n"
                    "<i>\"In an information-abundant economy, human attention becomes the paramount scarce resource. Herbert Simon noted that a wealth of information creates a poverty of attention. Digital platforms engineer variable reward loops, trading enduring reflective cognition for transient micro-engagements monetized via algorithmic programmatic advertising.\"</i>\n\n"
                    "❓ <b>Question:</b> According to Herbert Simon, what is the direct consequence of excessive information availability?\n\n"
                    "👉 <b>Your Turn:</b> Explain the economic principle in your own words!"
                ),
            },
        ],
    },
    # =========================================================================
    # 5. 🗣️ SPEAKING (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # =========================================================================
    config.MODE_SPEAKING: {
        config.LEVEL_BEGINNER: [
            {
                "id": "spk_beg_01",
                "badge": "🗣️ Minimal Pairs: /b/ vs /v/",
                "prompt": (
                    "🎙️ <b>Pronunciation Drill: Minimal Pairs</b>\n\n"
                    "Say these pairs aloud three times:\n"
                    "• <b>Berry</b> vs <b>Very</b>\n"
                    "• <b>Boat</b> vs <b>Vote</b>\n"
                    "• <b>Best</b> vs <b>Vest</b>\n\n"
                    "💡 <b>Tip:</b> For /b/, close both lips firmly. For /v/, gently touch your top teeth to your lower lip.\n\n"
                    "👉 <b>Your Turn:</b> Practice aloud and send a sentence containing both <i>'very'</i> and <i>'berry'</i>!"
                ),
            },
            {
                "id": "spk_beg_02",
                "badge": "🗣️ Minimal Pairs: /θ/ ('th') vs /s/",
                "prompt": (
                    "🎙️ <b>Pronunciation Drill: 'Th' Sounds</b>\n\n"
                    "Practice saying these pairs aloud:\n"
                    "• <b>Think</b> vs <b>Sink</b>\n"
                    "• <b>Thing</b> vs <b>Sing</b>\n"
                    "• <b>Theme</b> vs <b>Seem</b>\n\n"
                    "💡 <b>Tip:</b> Put the tip of your tongue slightly between your front teeth for 'th'.\n\n"
                    "👉 <b>Your Turn:</b> Practice aloud and type a sentence using <i>'think'</i> and <i>'sink'</i>!"
                ),
            },
            {
                "id": "spk_beg_03",
                "badge": "🗣️ Ordering Breakfast",
                "prompt": (
                    "🎙️ <b>Speaking Simulation:</b>\n\n"
                    "Order two fried eggs, whole-wheat toast, and black coffee with sugar.\n\n"
                    "💡 <b>Goal:</b> Speak in full sentences (<i>\"I'd like to have...\"</i>, <i>\"Could I please get...?\"</i>).\n\n"
                    "👉 <b>Your Turn:</b> Send a voice note or type out your exact breakfast order!"
                ),
            },
            {
                "id": "spk_beg_04",
                "badge": "🗣️ Spelling Over the Phone",
                "prompt": (
                    "🎙️ <b>Clarity Drill:</b>\n\n"
                    "Imagine spelling your email address over a poor telephone connection:\n"
                    "<i>\"john.smith92@email.com\"</i>\n\n"
                    "💡 <b>Tip:</b> Use phonetic markers (e.g., <i>'J as in January, S as in Sugar, dot, at sign'</i>).\n\n"
                    "👉 <b>Your Turn:</b> Type how you clearly spell out your username or email!"
                ),
            },
            {
                "id": "spk_beg_05",
                "badge": "🗣️ 30-Second Hobby Introduction",
                "prompt": (
                    "🎙️ <b>Fluency Prompt:</b>\n\n"
                    "Answer: <i>\"What is your favorite hobby and why do you enjoy it?\"</i>\n\n"
                    "💡 <b>Challenge:</b> Speak smoothly without long pauses using words like <i>'because'</i> and <i>'also'</i>.\n\n"
                    "👉 <b>Your Turn:</b> Send your 30-second response (voice message or text)!"
                ),
            },
            {
                "id": "spk_beg_06",
                "badge": "🗣️ Describing Your Hometown",
                "prompt": (
                    "🎙️ <b>Fluency Prompt:</b>\n\n"
                    "Describe where you grew up: Is it quiet or bustling? What is the weather like?\n\n"
                    "👉 <b>Your Turn:</b> Share 2–3 descriptive sentences about your hometown!"
                ),
            },
        ],
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "spk_int_01",
                "badge": "🗣️ Tongue Twister & Linked Sounds",
                "prompt": (
                    "🎙️ <b>Articulation Challenge:</b>\n\n"
                    "<i>\"She sells seashells on the seashore, and the shells she sells are seashore shells for sure.\"</i>\n\n"
                    "🎯 <b>Focus:</b> Clean switching between /s/ and /ʃ/ ('sh') sounds.\n\n"
                    "👉 <b>Your Turn:</b> Repeat 3 times at increasing speeds and write how it felt!"
                ),
            },
            {
                "id": "spk_int_02",
                "badge": "🗣️ 60-Second Impromptu Speech",
                "prompt": (
                    "🎙️ <b>Speaking Challenge:</b>\n\n"
                    "<b>Topic:</b> <i>\"If you could master any musical instrument overnight, which one would you choose and why?\"</i>\n\n"
                    "💡 <b>Goal:</b> Use transition phrases (<i>\"To begin with...\", \"Furthermore...\"</i>).\n\n"
                    "👉 <b>Your Turn:</b> Send your answer (voice or text) detailing your reasons!"
                ),
            },
            {
                "id": "spk_int_03",
                "badge": "🗣️ Expressing Polite Disagreement",
                "prompt": (
                    "🎙️ <b>Diplomatic Speech:</b>\n\n"
                    "A friend says: <i>\"Watching movies with subtitles is completely pointless!\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Disagree politely using softening phrases like <i>'I see your point, but...'</i> or <i>'I look at it a bit differently because...'</i>!"
                ),
            },
            {
                "id": "spk_int_04",
                "badge": "🗣️ Linking Words in Connected Speech",
                "prompt": (
                    "🎙️ <b>Connected Speech Drill:</b>\n\n"
                    "Practice linking consonant-to-vowel:\n"
                    "• <i>\"Hold on\"</i> -> sounds like <b>\"Hol-don\"</b>\n"
                    "• <i>\"Turn off\"</i> -> sounds like <b>\"Tur-noff\"</b>\n"
                    "• <i>\"Pick it up\"</i> -> sounds like <b>\"Pi-ki-tup\"</b>\n\n"
                    "👉 <b>Your Turn:</b> Say these aloud smoothly, then create a sentence linking two verbs!"
                ),
            },
            {
                "id": "spk_int_05",
                "badge": "🗣️ Explaining a Recipe Aloud",
                "prompt": (
                    "🎙️ <b>Instructional Speech:</b>\n\n"
                    "Explain step-by-step how to prepare your favorite simple meal or hot drink.\n\n"
                    "💡 <b>Focus:</b> Sequence markers (<i>'First', 'After that', 'Meanwhile', 'Finally'</i>).\n\n"
                    "👉 <b>Your Turn:</b> Send your instructional steps!"
                ),
            },
            {
                "id": "spk_int_06",
                "badge": "🗣️ Intonation in Questions",
                "prompt": (
                    "🎙️ <b>Intonation Lab:</b>\n\n"
                    "• Yes/No questions <b>rise</b> at the end: <i>\"Are you coming to the party? ↗\"</i>\n"
                    "• Wh- questions <b>fall</b> at the end: <i>\"Where did you leave the keys? ↘\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Practice both intonations aloud and send one example of each!"
                ),
            },
        ],
        config.LEVEL_ADVANCED: [
            {
                "id": "spk_adv_01",
                "badge": "🗣️ Contrastive Stress Shifts",
                "prompt": (
                    "🎙️ <b>Vocal Stress Challenge:</b>\n\n"
                    "Emphasize a different bold word to shift meaning:\n"
                    "1. <i>\"<b>I</b> didn't say she stole my money.\"</i> (Someone else did)\n"
                    "2. <i>\"I <b>DIDN'T</b> say she stole my money.\"</i> (Strong denial)\n"
                    "3. <i>\"I didn't say <b>SHE</b> stole my money.\"</i> (Someone else stole it)\n"
                    "4. <i>\"I didn't say she stole my <b>MONEY</b>.\"</i> (She stole something else)\n\n"
                    "👉 <b>Your Turn:</b> Practice how stress changes English meaning and send your observations!"
                ),
            },
            {
                "id": "spk_adv_02",
                "badge": "🗣️ 45-Second Debate Argument",
                "prompt": (
                    "🎙️ <b>Persuasive Rhetoric:</b>\n\n"
                    "<b>Motion:</b> <i>\"Should companies enforce a strict 4-day workweek?\"</i>\n\n"
                    "💡 <b>Challenge:</b> Deliver a crisp opening statement featuring an impactful hook and strong conclusion.\n\n"
                    "👉 <b>Your Turn:</b> Send your persuasive argument!"
                ),
            },
            {
                "id": "spk_adv_03",
                "badge": "🗣️ Rapid Articulation: Red Lorry, Yellow Lorry",
                "prompt": (
                    "🎙️ <b>Advanced Enunciation:</b>\n\n"
                    "Repeat 5 times consecutively without hesitation:\n"
                    "<i>\"Red lorry, yellow lorry, red lorry, yellow lorry.\"</i>\n\n"
                    "🎯 <b>Focus:</b> Clean distinction between /r/ and /l/ liquid consonants.\n\n"
                    "👉 <b>Your Turn:</b> Try this rapid tongue twister and report your speed!"
                ),
            },
            {
                "id": "spk_adv_04",
                "badge": "🗣️ Strategic Pauses & Executive Presence",
                "prompt": (
                    "🎙️ <b>Executive Communication:</b>\n\n"
                    "Practice delivering this announcement with deliberate 1-second pauses at the slashes:\n"
                    "<i>\"Our Q3 projections exceeded expectations / not by chance / but through disciplined engineering / and relentless customer focus.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Practice dramatic pacing and send a reflection on how pauses alter authority!"
                ),
            },
            {
                "id": "spk_adv_05",
                "badge": "🗣️ Metaphorical Storytelling",
                "prompt": (
                    "🎙️ <b>Elevated Fluency:</b>\n\n"
                    "Explain the concept of 'technical debt' or 'burnout' using an everyday metaphor (e.g., credit card interest, marathon pacing, or car maintenance).\n\n"
                    "👉 <b>Your Turn:</b> Send your metaphorical explanation in 3–4 sentences!"
                ),
            },
            {
                "id": "spk_adv_06",
                "badge": "🗣️ Nuanced Hedging in High-Stakes Speech",
                "prompt": (
                    "🎙️ <b>Diplomatic Phrasing:</b>\n\n"
                    "Turn this blunt statement into a polished executive observation:\n"
                    "Blunt: <i>\"This software architecture is terrible and will fail under heavy load.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Rephrase using sophisticated diplomatic hedging!"
                ),
            },
        ],
    },
    # =========================================================================
    # 6. 🎮 ENGLISH CHALLENGE (18 exercises: 6 Beginner, 6 Intermediate, 6 Advanced)
    # =========================================================================
    config.MODE_CHALLENGE: {
        config.LEVEL_BEGINNER: [
            {
                "id": "chg_beg_01",
                "badge": "🎮 Word Unscramble: Morning Routine",
                "prompt": (
                    "🧩 <b>Level 1: Unscramble the Word</b>\n\n"
                    "Scrambled: <code>[ K - F - B - A - E - R - A - S - T ]</code>\n"
                    "Hint: The first meal of the morning! 🍳\n\n"
                    "👉 <b>Your Turn:</b> Reply with the unscrambled English word!"
                ),
            },
            {
                "id": "chg_beg_02",
                "badge": "🎮 Odd One Out: Food Categories",
                "prompt": (
                    "🧩 <b>Spot the odd word out:</b>\n\n"
                    "<code>[ Apple, Banana, Carrot, Strawberry, Peach ]</code>\n\n"
                    "👉 <b>Your Turn:</b> Which item doesn't belong and why?"
                ),
            },
            {
                "id": "chg_beg_03",
                "badge": "🎮 Opposite Match",
                "prompt": (
                    "🧩 <b>Find the exact opposites:</b>\n\n"
                    "1. <b>Ancient</b> -> ?\n"
                    "2. <b>Generous</b> -> ?\n"
                    "3. <b>Courageous</b> -> ?\n\n"
                    "👉 <b>Your Turn:</b> Reply with antonyms for all three words!"
                ),
            },
            {
                "id": "chg_beg_04",
                "badge": "🎮 Missing Vowels Riddle",
                "prompt": (
                    "🧩 <b>Fill in the missing vowels (A, E, I, O, U):</b>\n\n"
                    "<code>[ B _ T T _ R F L Y ]</code> 🦋\n"
                    "Hint: A colorful insect with delicate wings!\n\n"
                    "👉 <b>Your Turn:</b> Send the completed word!"
                ),
            },
            {
                "id": "chg_beg_05",
                "badge": "🎮 Category Sprint",
                "prompt": (
                    "🧩 <b>Fast Vocabulary Challenge:</b>\n\n"
                    "Name <b>5 things found in a kitchen</b> that start with different letters!\n\n"
                    "👉 <b>Your Turn:</b> List your five kitchen items below!"
                ),
            },
            {
                "id": "chg_beg_06",
                "badge": "🎮 Rhyme Match",
                "prompt": (
                    "🧩 <b>Rhyming Riddle:</b>\n\n"
                    "I rhyme with <b>'LIGHT'</b>, I happen during sleep, and stars appear when I arrive. What am I?\n\n"
                    "👉 <b>Your Turn:</b> Send your answer!"
                ),
            },
        ],
        config.LEVEL_INTERMEDIATE: [
            {
                "id": "chg_int_01",
                "badge": "🎮 Idiom Riddle: Missing Animals",
                "prompt": (
                    "🧩 <b>Complete the Famous Idioms:</b>\n\n"
                    "1. <i>\"To kill two _______ with one stone.\"</i>\n"
                    "2. <i>\"Let the _______ out of the bag.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Name the two missing animals and explain the meaning of either idiom!"
                ),
            },
            {
                "id": "chg_int_02",
                "badge": "🎮 Sentence Scramble: Idiom",
                "prompt": (
                    "🧩 <b>Unscramble the words into a natural English idiom:</b>\n\n"
                    "Words: <code>[ bite / bullet / have / the / we / to / will ]</code>\n\n"
                    "👉 <b>Your Turn:</b> Rearrange the words and explain what this idiom means!"
                ),
            },
            {
                "id": "chg_int_03",
                "badge": "🎮 Guess the Mystery Profession",
                "prompt": (
                    "🧩 <b>Mystery Profession Riddle:</b>\n\n"
                    "<i>\"I spend my days checking blueprints, calculating structural load thresholds, and ensuring bridges withstand seismic tremors. Without my calculations, skyscrapers could not stand.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> What is my profession?"
                ),
            },
            {
                "id": "chg_int_04",
                "badge": "🎮 Phrasal Verb Swap",
                "prompt": (
                    "🧩 <b>Replace the formal verb with an everyday phrasal verb:</b>\n\n"
                    "Formal: <i>\"The committee decided to <b>extinguish</b> the bonfire.\"</i>\n"
                    "Formal: <i>\"They had to <b>postpone</b> the quarterly summit.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Supply the two phrasal verbs (Hint: both end in <i>'out'</i> or <i>'off'</i>)!"
                ),
            },
            {
                "id": "chg_int_05",
                "badge": "🎮 Preposition Trap",
                "prompt": (
                    "🧩 <b>Fill in the correct prepositions:</b>\n\n"
                    "1. <i>\"She is proficient _______ data analysis.\"</i>\n"
                    "2. <i>\"He apologized _______ his abrupt departure.\"</i>\n"
                    "3. <i>\"We congratulated them _______ winning the championship.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Send the 3 correct prepositions in order!"
                ),
            },
            {
                "id": "chg_int_06",
                "badge": "🎮 Fix the Malapropism",
                "prompt": (
                    "🧩 <b>Correct the misused word:</b>\n\n"
                    "❌ <code>\"He gave an illusion to Shakespeare in his opening speech.\"</code>\n"
                    "Hint: It sounds like illusion, but means an indirect reference!\n\n"
                    "👉 <b>Your Turn:</b> Send the correct word and its spelling!"
                ),
            },
        ],
        config.LEVEL_ADVANCED: [
            {
                "id": "chg_adv_01",
                "badge": "🎮 Synonym Intensity Gradient",
                "prompt": (
                    "🧩 <b>Intensity Gradient Challenge:</b>\n\n"
                    "Arrange these synonyms in ascending order of intensity (from mildest to most extreme):\n"
                    "<code>[ Furious, Annoyed, Livid, Irritated, Enraged ]</code>\n\n"
                    "👉 <b>Your Turn:</b> Order the list from 1 (mildest) to 5 (most severe)!"
                ),
            },
            {
                "id": "chg_adv_02",
                "badge": "🎮 Etymology & Latin Roots",
                "prompt": (
                    "🧩 <b>Root Word Challenge:</b>\n\n"
                    "The Latin root <b>'VERT / VERS'</b> means <i>'to turn'</i>.\n"
                    "Identify words meaning:\n"
                    "1. To turn away one's eyes: <b>A_______</b>\n"
                    "2. To turn something completely upside down or inside out: <b>I_______</b>\n"
                    "3. Capable of turning to many different tasks: <b>V_______</b>\n\n"
                    "👉 <b>Your Turn:</b> Name all three words!"
                ),
            },
            {
                "id": "chg_adv_03",
                "badge": "🎮 Spot the Dangling Modifier",
                "prompt": (
                    "🧩 <b>Grammar Precision:</b>\n\n"
                    "❌ <code>\"Walking into the conference hall, the PowerPoint presentation was already concluding.\"</code>\n\n"
                    "👉 <b>Your Turn:</b> Explain why this sentence has a dangling modifier and provide the corrected version!"
                ),
            },
            {
                "id": "chg_adv_04",
                "badge": "🎮 Register Mismatch Correction",
                "prompt": (
                    "🧩 <b>Stylistic Elevation:</b>\n\n"
                    "Elevate this casual email sentence for an academic peer-reviewed journal:\n"
                    "Casual: <i>\"Lots of folks think this theory is totally bogus because the numbers are all messed up.\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Rewrite using formal academic vocabulary and tone!"
                ),
            },
            {
                "id": "chg_adv_05",
                "badge": "🎮 The Oxymoron Challenge",
                "prompt": (
                    "🧩 <b>Literary Device Riddle:</b>\n\n"
                    "An oxymoron combines two contradictory terms (e.g., <i>'deafening silence'</i>).\n"
                    "Formulate three original, evocative oxymorons describing modern life or technology!\n\n"
                    "👉 <b>Your Turn:</b> Share your 3 creative oxymorons!"
                ),
            },
            {
                "id": "chg_adv_06",
                "badge": "🎮 Lateral Thinking Riddle",
                "prompt": (
                    "🧩 <b>Linguistic Riddle:</b>\n\n"
                    "<i>\"What English word begins with 'T', ends with 'T', and is filled with 'T'?\"</i>\n\n"
                    "👉 <b>Your Turn:</b> Solve the riddle and send your answer!"
                ),
            },
        ],
    },
}


def get_offline_exercise(
    mode: str,
    level: str = config.DEFAULT_LEVEL,
    exclude_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Selects a randomized exercise from the curated offline bank.
    Ensures that, whenever possible, the returned exercise differs from exclude_id
    so consecutive taps never repeat the exact same challenge.
    """
    level_dict = EXERCISE_BANK.get(mode, {}).get(level)
    if not level_dict:
        level_dict = EXERCISE_BANK.get(mode, {}).get(config.DEFAULT_LEVEL, [])

    if not level_dict:
        return {
            "id": "default_fallback",
            "title": config.LEARNING_MODES.get(mode, {}).get("title", "English Practice"),
            "badge": "Practice Exercise",
            "prompt": "Practice forming a natural English sentence related to this topic and reply below!",
        }

    candidates = [ex for ex in level_dict if ex.get("id") != exclude_id]
    chosen = random.choice(candidates if candidates else level_dict)

    mode_info = config.LEARNING_MODES.get(mode, {})
    return {
        "id": chosen.get("id"),
        "title": mode_info.get("title", "English Practice"),
        "badge": chosen.get("badge", "Practice Exercise"),
        "prompt": chosen.get("prompt", ""),
    }


def get_offline_feedback(mode: str, level: str, safe_user_text: str) -> str:
    """
    Returns encouraging, contextual feedback when the AI service is unavailable.
    """
    level_info = config.LEVEL_INFO.get(level, config.LEVEL_INFO[config.DEFAULT_LEVEL])
    badge = level_info["badge"]

    templates = [
        (
            f"✨ <b>English Buddy Feedback ({badge}):</b>\n\n"
            f"You wrote: <i>\"{safe_user_text}\"</i>\n\n"
            f"👏 <b>Great effort!</b> Your message is clear and expressive. "
            f"Consistency is key—try tapping <b>🔄 Next Exercise</b> to keep your momentum going!"
        ),
        (
            f"✨ <b>Coach Note ({badge}):</b>\n\n"
            f"Received: <i>\"{safe_user_text}\"</i>\n\n"
            f"💡 <b>Helpful Tip:</b> When practicing at the {level.capitalize()} level, focus on natural linking words "
            f"(e.g., <i>'furthermore', 'on the other hand', 'specifically'</i>). Keep up the great work!"
        ),
        (
            f"✨ <b>English Buddy Insight ({badge}):</b>\n\n"
            f"Your response: <i>\"{safe_user_text}\"</i>\n\n"
            f"🎯 Excellent practice! Try reading your answer aloud once more to train your tongue on natural intonation."
        ),
    ]

    return random.choice(templates)
