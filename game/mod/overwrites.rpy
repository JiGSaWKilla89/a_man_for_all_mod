#define config.label_overrides["episode07_017_psych_office"] = "episode07_017_psych_office_modded"#???

label episode07_017_psych_office_modded:

    window hide
    scene e007_017_000_opener_psychoffice_000 with fade
    pause
    $ quick_menu = True

    scene e007_017_001_psychoffice_enter_001 with dissolve
    window show
    play backgroundmusic "audio/music/kate_01.ogg"
    kat "Hello, [mc]! I'm so glad you could make it."
    pro "Hey, Dr. Garcia. I'm always willing to visit."

    scene e007_017_002_psychoffice_enter_002 with dissolve
    kat "Please have a seat. Make yourself comfortable."
    kat "I'm sure there's something on your mind."
    pro "There's been a lot lately."

    scene e007_017_003_psychoffice_greet_001 with dissolve
    kat "I only learned about the coffee shop recently. I'm sorry to hear what happened."
    pro "*sigh* Thanks."
    kat "I never could have imagined something like that would ever happen."

    scene e007_017_004_psychoffice_recover_001 with dissolve
    pro "It was the last thing any of us expected."
    pro "We were all having such a good time. The night was perfect."
    pro "Looking back on it, a part of me still doesn't believe it."

    scene e007_017_005_psychoffice_recover_002 with dissolve
    kat "That's a natural reaction."
    kat "Most of our everyday lives are ordinary. When something jarring happens, it can take us some time to process it."
    kat "The most important thing is that everybody is all right."
    pro "We're all okay. Billy's fine. My friend Harlow is fine."

    scene e007_017_006_psychoffice_recover_003 with dissolve
    kat "I'm glad. Sometimes people say they're fine when they're not though."
    kat "Don't be afraid to say what's on your mind. If there's anything at all bothering you, feel free to share it with me."

    menu:
        kat "You don't have to be concerned with privacy when you speak with me."

        "{kni_menu}Thank you.{/kni_menu}":
            $ kat_knight +=1

            pro "Thank you."
            pro "I think I'm processing it. It's just strange."

            scene e007_017_007_psychoffice_recover_004 with dissolve
            kat "Strange circumstances can always affect us differently."
            kat "It's important we keep our perspective and not let our emotions sway us in one direction or another."
            pro "I think I'm okay for now. Better than when it first happened."
            kat "That's good to hear."

        "{jok_menu}I always thought we lived in a parallel universe.{/jok_menu}":
            $ kat_joker +=1

            pro "I always thought we lived in a parallel universe."
            pro "I'm beginning to think that might be the case."

            scene e007_017_007_psychoffice_recover_004 with dissolve
            kat "Unfortunately, this is the world we live in."
            kat "Strange and awful things can happen even if we do everything we can to mitigate it."
            pro "*sigh* Yeah, it sucks that we're in a world where everything is screwed up now."
            pro "But I feel okay."
            kat "That's good to hear."

        "{smo_menu}Your company is enough to make everything okay.{/smo_menu}":
            $ kat_smooth +=1

            pro "Your company is enough to make everything okay."
            pro "Just seeing you again makes me smile."

            scene e007_017_007_psychoffice_recover_004 with dissolve
            kat "Yes..."
            kat "...While I don't think that aligns with the appropriateness we agreed on previously, I appreciate the sentiment."
            pro "It's nice being here. I appreciate you."
            kat "Yes... Of course..."

    kat "You said one of your friends was involved in the accident?"
    pro "Yeah. Harlow. She passed out from the smoke but she's okay."

    scene e007_017_008_psychoffice_harlow_001 with dissolve
    kat "And would you say her behavior has changed?"
    pro "I don't think so... She seems fine."
    pro "She came to school with me. We had lunch. Everything was fine."

    if harlow_pursue_004 == True:
        pro "She's special to me, so I'd do anything for her."
        kat "I see... It's good that she has someone like you in her life."

    scene e007_017_010_psychoffice_harlow_003 with dissolve
    kat "I'm sure you already feel this way but the most important thing is to just be there for her."
    kat "An accident like this can leave us feeling vulnerable even if it might not seem like it. Assurances can go a long way."
    pro "That shouldn't be a problem. I feel like I would do that regardless if there were an accident or not."
    kat "You said she was a student. Does she attend SCI?"
    pro "Yeah, she does."

    scene e007_017_011_psychoffice_harlow_004 with dissolve
    kat "I'd like to invite her to my office. If she's a student here, she's free to use my services for a counseling session."
    pro "Hmm... If you think it'll help."
    kat "I think it will. Even if she's completely fine, it can give her the assurances I spoke of."
    pro "That's a good idea. I'll mention it to her."

    scene e007_017_012_psychoffice_help_001 with dissolve
    kat "The situation with the coffee shop..."
    kat "...I don't know what I can do there but is there something I can do to help?"
    pro "I can't think of anything. The police are looking into it."
    pro "Billy's insurance should handle most of the repairs. Until the building is cleared, there's not much else to do."

    scene e007_017_013_psychoffice_help_002 with dissolve
    kat "It's always a shame when something like this happens. Especially to an honest business."
    kat "If there's anything I can do to assist you please let me know."
    pro "If I think of anything, I'll let you know."

    scene e007_017_014_psychoffice_thesis_001 with dissolve
    pro "Since I'm here, I guess I can talk about my thesis."
    pro "I just talked to Vanessa. She's setting up a meeting with her dad."
    pro "I think there's a chance he can help with distribution of my survey to different parts of the city."

    scene e007_017_015_psychoffice_vanessa_001 with dissolve
    kat "I'm delighted to hear that."
    kat "I knew you and Vanessa would work well together."

    menu:
        kat "I assume that you're more comfortable working with her."

        "{kni_menu}Our deal is working.{/kni_menu}":
            $ kat_knight +=1

            pro "Our deal is working."
            pro "So far I haven't had to do anything difficult for her and she's been going along with helping me."

            scene e007_017_016_psychoffice_vanessa_002 with dissolve
            kat "I'm not surprised."
            kat "I knew Vanessa would be willing despite how you might personally feel about one another."

        "{jok_menu}I put up with her.{/jok_menu}":
            $ kat_joker +=1

            pro "I put up with her."
            pro "Too bad she doesn't see how funny I am."

            scene e007_017_016_psychoffice_vanessa_002 with dissolve
            kat "*soft laugh* Humor is a very subjective thing."
            kat "The important thing is that you appear to have an amicable relationship with her."

        "{smo_menu}It's difficult for her.{/smo_menu}":
            $ kat_smooth +=1

            pro "It's difficult for her."
            pro "She gets distracted by how attracted she is to me. Then again, most women have that problem."

            scene e007_017_016_psychoffice_vanessa_002 with dissolve
            kat "*soft laugh* I found that the potential for romance is always a consideration for people your age."
            kat "I won't comment on your personal relationship since I don't know the particulars nor is it my business."
            pro "More for her than for me."
            kat "*chucking* I'll take your word for it."

    pro "You know Vanessa's dad. Is there anything I should know before I speak to him?"

    scene e007_017_017_psychoffice_vanessa_003 with dissolve
    kat "Hmm..."
    kat "I know him as a good person. He's been completely honest with me."
    kat "I'm sure he'd be more than willing to help you if you approach him with sincerity."
    pro "Nothing I should worry about then?"

    scene e007_017_018_psychoffice_vanessa_004 with dissolve
    kat "I don't believe so."
    kat "But you shouldn't assume he'll do anything you ask of him."
    kat "Businessmen are known for stretching their time thin."

    menu:

        kat "My best advice would be to respect him and his time."

        "{kni_menu}I appreciate any kind of opportunity.{/kni_menu}":
            $ kat_knight +=1

            pro "I appreciate any kind of opportunity."
            pro "I'll make sure to thank him for it."

            scene e007_017_019_psychoffice_vanessa_005 with dissolve
            kat "Don't praise him too much."
            kat "Businessmen can tell when flattery is insincere and it would be just as bad as insulting him."
            pro "Walk the tricky line then."

        "{jok_menu}I should come up with a routine.{/jok_menu}":
            $ kat_joker +=1

            pro "I should come up with a routine."
            pro "Hit him with a few zingers and I'll have him eating out of the palm of my hand."

            scene e007_017_019_psychoffice_vanessa_005 with dissolve
            kat "*laughing* I wouldn't advise that."
            pro "Everybody lets their guard down when they laugh."
            kat "True. Though I don't think that will be necessary in this case."

        "{smo_menu}I'll just turn on my charm.{/smo_menu}":
            $ kat_smooth +=1

            pro "I'll just turn on my charm."
            pro "My charisma doesn't just work on the ladies, you know?"

            scene e007_017_019_psychoffice_vanessa_005 with dissolve
            kat "I'm certain you're trying to be amusing but that won't be necessary."
            pro "I'm not trying. I just can't help it."
            kat "*soft laugh* Businessmen like him are used to speaking to all sorts of characters."
            kat "As I said, they don't appreciate insincerity."

    kat "Just speak to him honestly and earnestly. Push hard. But in the end, respect his decision."
    pro "I think I can do that."

    scene e007_017_020_psychoffice_relax_001 with dissolve
    kat "Don't push yourself too hard either."
    kat "I know your thesis is important but you have more than enough time to consider other things in your life."
    kat "Try to relax if you feel like you're being overwhelmed. Sometimes giving yourself space can help."
    pro "I guess you'd know a thing or two about being overwhelmed."

    scene e007_017_021_psychoffice_relax_002 with dissolve
    kat "*laughing* Yes, I've been in your shoes before."
    kat "And my work hasn't lightened up at all. If you need an authority on the importance of peace, I can speak on it."
    pro "Since I don't have to work for a while, I'll take some time to myself."

    scene e007_017_022_psychoffice_thank_001 with dissolve
    pro "Thanks, Dr. Garcia."
    pro "It feels so easy to talk to you and I always learn something new."
    pro "I appreciate today though. It feels like I needed this even though I didn't realize it."

    scene e007_017_023_psychoffice_friend_001 with dissolve
    kat "Of course! That's my job. Being there for my students is what I find the most fulfilling."

    menu:
        kat "It's a pleasant break from the monotony of paperwork and reminds me that what I do is important."

        "{kni_menu}The school is lucky to have you.{/kni_menu}":
            $ kat_knight +=1

            pro "The school is lucky to have you."
            pro "I couldn't have asked for a better dean."

            scene e007_017_024_psychoffice_friend_002 with dissolve
            kat "Thank you, [mc]."
            kat "It's always rewarding to see a student succeed. Not just in school but life as well."
            pro "I appreciate that."

        "{jok_menu}You're pretty cool.{/jok_menu}":
            $ kat_joker +=1

            pro "You're pretty cool."
            pro "I think some of the other professors here would be lame but you... you're not."

            scene e007_017_024_psychoffice_friend_002 with dissolve
            kat "Thank you, [mc], though I wouldn't speak ill of the other professors."
            kat "They work just as hard as I do and contribute to the school all the same."
            pro "I don't think they'd be as cool to talk to as you."

        "{smo_menu}It's great being around you.{/smo_menu}":
            $ kat_smooth +=1

            pro "It's great being around you."
            pro "You're the only professor worth hanging out with."

            scene e007_017_024_psychoffice_friend_002 with dissolve
            kat "Thank you, [mc]."
            kat "But I wouldn't describe our meetings as 'hanging out.' Remember that you're a student and I'm helping you."
            pro "It's hard to remember that all the time..."

    pro "Sometimes I feel like you're a friend as much as my dean."

    scene e007_017_025_psychoffice_friend_003 with dissolve
    kat "I'm sorry if I gave you that impression. Apparently I keep giving it to you."
    kat "But remember that we went over this. Please try to remain professional when we speak."
    pro "Right. It's just friendly conversation. I didn't mean anything by it."
    pro "I'm sorry."

    scene e007_017_026_psychoffice_friend_004 with dissolve
    kat "Again I apologize."
    kat "I try to create a comfortable environment for every person that comes into my office."
    kat "Admittedly, the circumstances of the psychology department have given me a more casual attitude to our meetings."

    scene e007_017_027_psychoffice_professional_001 with dissolve
    kat "But I want to reiterate that we're to remain professional."
    kat "You are a student and I'm your dean. My primary intention is to guide you on your academic journey."
    kat "There is no discussion on this."
    pro "I understand. I don't mind the reminder."

    scene e007_017_028_psychoffice_professional_002 with dissolve
    kat "Thank you."
    kat "Are there any other issues you wish to discuss with me?"
    pro "I can't think of anything right now. I guess I'll leave you to it."

    scene e007_017_029_psychoffice_handshake_001 with dissolve
    pro "Thanks for the meeting. I feel better."
    kat "It's always a pleasure."
    kat "Please tell your friend to contact me and we can schedule a meeting."
    kat "Don't put any pressure on her. I only want to help if she's willing."
    pro "I'll let her know."

    scene e007_017_030_psychoffice_handshake_002 with dissolve
    kat "And if there's anything you need, you know that you can always contact me."
    pro "Right..."

    $ two_choice = True
    menu:
        kat "Were there any last things you wanted to discuss?"

        "Yes...  It's important... (Potentially Pursue Kate)":
            $ two_choice = False
            $ kate_flirt_007 = True

            pro "Yes... It's important..."

            scene e007_017_032_psychoffice_flirt_001 with dissolve
            stop backgroundmusic fadeout 3.0
            kat "What is it?"
            pro "I just... I just want to talk to you."
            kat "About what?"
            pro "...Anything. Just to talk to you."

            scene e007_017_033_psychoffice_flirt_002 with dissolve
            kat "[mc]... We've already discussed this."
            kat "Whatever you might be feeling at the moment is irrelevant. You can't let your irrationality get the best of you."
            kat "These are just emotions. Please stay professional."
            pro "Addressing what I'm thinking is professional."

            scene e007_017_034_psychoffice_uncertain_001 with dissolve
            kat "*sigh* I knew this would happen. Despite my best efforts, the damage has been done."
            kat "I've been too casual in our relationship and I've manipulated you into thinking there's something there."
            pro "You haven't manipulated me. There {i}is{/i} something there. You can't deny that."

            scene e007_017_035_psychoffice_uncertain_002 with dissolve
            kat "There is... Something irrational or unreasonable..."

            if kate_flirt_kiss_006 == True:
                kat "That kiss was wrong."

            kat "None of this is right."
            kat "But there's another part of me that... that—"
            pro "That wonders if there's something worth exploring."

            scene e007_017_036_psychoffice_uncertain_003 with dissolve
            kat "Yes..."
            kat "I've never felt so irrational in my life. So much is happening I..."
            kat "...I try to reason with myself but this feeling is harder to shake. Even acknowledging such foolish notions fails to make them go away."

            scene e007_017_037_psychoffice_uncertain_004 with dissolve
            kat "I admit that I find some comfort in our conversations."
            kat "The thought of you being the last student I'll guide through graduation at SCI..."
            kat "...Personally guiding you... I get... romantic about the process. A sort of farewell to everything."
            kat "But I know there are other people in your life. Someone more appropriate."

            scene e007_017_038_psychoffice_uncertain_005 with dissolve

            if harlow_pursue_004 == True or erika_pursue_005 == True:
                pro "*sigh* There are other people I care about."
                pro "I care about a lot of people."
                pro "And I think that if you truly care about someone, things will work out."

            elif harlow_pursue_004 == False and erika_pursue_005 == False:
                pro "There's no one in my life like that right now."
                pro "You're the only woman I've given consideration at the moment."
                pro "I think that means something."

            scene e007_017_039_psychoffice_choice_001 with dissolve
            kat "Do you not care about your thesis? Do you not care about the conflict of interest?"
            kat "You'll have to work that much harder to dispel the notion that I favored you. You'll have to prove you did all of the work and you alone."
            kat "Are you willing to take that kind of risk?"

            scene e007_017_040_psychoffice_choice_002 with dissolve
            pro "Hmm... I see what the issue is..."
            pro "But why would I worry about something that wouldn't apply to me? I planned on doing all of the research myself regardless."
            pro "If I graduate, it won't be because you did me a favor. It won't be because you gave me special consideration."
            pro "I know my thesis will be good enough on its own merits."
            pro "The school can't punish either one of us for something that isn't banned or illegal."
            pro "We're adults. We have the right to make our own decisions."

            scene e007_017_041_psychoffice_choice_003 with dissolve
            $renpy.sound.play("audio/sounds/universal/heartbeat_001.ogg", loop=True)
            kat "Just because we have the right to make our own decisions doesn't mean we always choose the best one."
            kat "Sometimes we should deny something for our own good."
            kat "Think about you're doing... There's no harm in ending this now."
            kat "We can still be cordial."

            $ four_choice = True
            menu:
                kat "Consider everything before you do anything. That's all I ask."

                "Pursue Kate while still pursuing others":
                    $ four_choice = False
                    $ kate_sex_ever_000 = True
                    $ kate_office_sex_007 = True
                    $ kate_pursue_007 = True
                    scene e007_017_044_psychoffice_pursue_001 with dissolve
                    stop sound
                    pro "I know I can make things work."
                    pro "We're humans. I won't allow anybody to fault us for being honest with each other."
                    pro "If I have to, I'll do everything I can to make everybody understand that."

                    scene e007_017_045_psychoffice_pursue_002 with dissolve
                    kat "Are you sure you know what you're saying?"
                    kat "You're only making things more difficult for yourself."
                    pro "I can handle it. I know I can."

                    scene e007_017_044_psychoffice_pursue_001 with dissolve
                    stop sound
                    pro "I can't help myself."
                    pro "I know what I want. And I know you want it, too."
                    pro "Why deny ourselves?"

                    scene e007_017_045_psychoffice_pursue_002 with dissolve
                    kat "Sometimes we have to deny ourselves... for what's best..."
                    kat "But even though I know this isn't something I should be doing..."
                    kat "...I can't stop thinking about taking this chance."

                    jump episode07_017_psych_office_three_pursue

                "I know I can make things work. (Pursue Kate)":
                    $ four_choice = False
                    $ kate_sex_ever_000 = True
                    $ kate_office_sex_007 = True
                    $ kate_pursue_007 = True

                    ##### No longer pursuing solo romance with other women
                    ##### Solo romance flags for other women are turned off
                    $ erika_romance_solo = False
                    $ harlow_romance_solo = False
                    $ riley_romance_solo = False
                    $ vanessa_romance_solo = False

                    $ marisa_romance_solo = False
                    $ jordan_romance_solo = False
                    $ sophia_romance_solo = False

                    $ lorelei_romance_solo = False
                    $ grace_romance_solo = False
                    $ stranger_romance_solo = False

                    scene e007_017_044_psychoffice_pursue_001 with dissolve
                    stop sound
                    pro "I know I can make things work."
                    pro "We're humans. I won't allow anybody to fault us for being honest with each other."
                    pro "If I have to, I'll do everything I can to make everybody understand that."

                    scene e007_017_045_psychoffice_pursue_002 with dissolve
                    kat "Are you sure you know what you're saying?"
                    kat "You're only making things more difficult for yourself."
                    pro "I can handle it. I know I can."

                    jump episode07_017_psych_office_three_pursue

                "I can't help myself. (Pursue Kate)":
                    $ four_choice = False
                    $ kate_sex_ever_000 = True
                    $ kate_office_sex_007 = True
                    $ kate_pursue_007 = True

                    ##### No longer pursuing solo romance with other women
                    ##### Solo romance flags for other women are turned off
                    $ erika_romance_solo = False
                    $ harlow_romance_solo = False
                    $ riley_romance_solo = False
                    $ vanessa_romance_solo = False

                    $ marisa_romance_solo = False
                    $ jordan_romance_solo = False
                    $ sophia_romance_solo = False

                    $ lorelei_romance_solo = False
                    $ grace_romance_solo = False
                    $ stranger_romance_solo = False

                    scene e007_017_044_psychoffice_pursue_001 with dissolve
                    stop sound
                    pro "I can't help myself."
                    pro "I know what I want. And I know you want it, too."
                    pro "Why deny ourselves?"

                    scene e007_017_045_psychoffice_pursue_002 with dissolve
                    kat "Sometimes we have to deny ourselves... for what's best..."
                    kat "But even though I know this isn't something I should be doing..."
                    kat "...I can't stop thinking about taking this chance."

                    jump episode07_017_psych_office_three_pursue

                "Maybe denying ourselves is right. (Don't pursue Kate)":
                    $ four_choice = False
                    $ kate_office_pursue_decline_007 = True

                    scene e007_017_042_psychoffice_decline_001 with dissolve
                    stop sound
                    pro "Maybe denying ourselves is right."
                    pro "We can't lose ourselves to every desire."
                    kat "I'm glad you understand."

                    scene e007_017_043_psychoffice_decline_002 with dissolve
                    kat "If we gave in to every whim we had then our discipline would be lost."
                    kat "I think it's best that we let this pass."
                    kat "Speaking from years of experience and everything I've witnessed, I know any feelings now will likely be fleeting."
                    pro "I think you're right."
                    pro "I should go now."
                    kat "That would probably be for the best."

                    jump episode07_017_psych_office_two_friendly

                "I guess I'm not thinking straight. (Don't pursue Kate)":
                    $ four_choice = False
                    $ kate_office_pursue_decline_007 = True

                    scene e007_017_042_psychoffice_decline_001 with dissolve
                    stop sound
                    pro "I guess I'm not thinking straight."
                    pro "I'm sorry for putting you in an uncomfortable position."
                    kat "Any guilt should be mine. I was wrong for making you think a certain way."
                    pro "You didn't have anything to do with it. But at least we both seem to be thinking clearly now."

                    scene e007_017_043_psychoffice_decline_002 with dissolve
                    kat "That's why I enjoy doing what I do."
                    kat "Our instincts sometimes get the better of us. It might not feel like it now but this is for the best."
                    pro "Our relationship doesn't have to change or be awkward because of this."
                    kat "Of course not. Just because we choose to remain professional doesn't mean I appreciate you any less."
                    pro "Yeah... I'm happy with that."

                    jump episode07_017_psych_office_two_friendly

        "No, that was it.":
            $ two_choice = False

            pro "No, that was it."

            jump episode07_017_psych_office_two_friendly

#define config.label_overrides["episode05_025_viridian_meeting"] = "episode05_025_viridian_meeting_modded"#???

label episode05_025_viridian_meeting_modded:

    scene e005_025_001_viridianmeeting_enter_001 with fade
    window show
    play backgroundmusic "audio/music/viridian_003.ogg"
    ril "Okay. It's early in the night, so there may be more people coming in to talk to."
    ril "But every single person counts. All we need is one of them to share our vision and we've pulled it off."

    scene e005_025_002_viridianmeeting_enter_002 with dissolve
    pro "Seems empty... Is that a dance floor?"
    ril "Most people don't come to meetings like this to dance. At least, not until they get their business done."
    ril "Why? Feel like showing off some moves and cutting a rug?"
    pro "Would you believe it wouldn't be the first time this week?"

    scene e005_025_003_viridianmeeting_ready_001 with dissolve
    ril "I never know what to expect when you're involved, so I wouldn't be surprised."
    ril "You'll have to hold off on running to the dance floor until we get our deal."

    menu:
        ril "Maybe then you can show everybody how to move."

        "{kni_menu}If we get our deal, I'll celebrate.{/kni_menu}":
            $ ril_knight +=1

            pro "If we get our deal, I'll celebrate."
            pro "Not sure if dancing is the way to go though."

            scene e005_025_004_viridianmeeting_ready_002 with dissolve
            ril "We can worry about how to celebrate after."
            ril "Honestly, I'm so excited at the prospect of getting a deal, I might dance on the spot."
            pro "I wouldn't stop you. Billy would probably join in when we tell him."
            ril "*laughing* I hope so."

        "{jok_menu}Gotta use my young bones while I got'em.{/jok_menu}":
            $ ril_joker +=1

            pro "Gotta use my young bones while I got'em."

            scene e005_025_004_viridianmeeting_ready_002 with dissolve
            ril "Just make sure you don't show anybody up."
            ril "Some of these people have a lot of pride. They wouldn't be happy about someone upstaging them."
            pro "I'm just trying to have a good time. Move it or lose it."
            ril "*laughing*"

        "{smo_menu}You can dance with me.{/smo_menu}":
            $ ril_smooth +=1

            pro "You can dance with me."
            pro "This party could use a little life in it."

            scene e005_025_004_viridianmeeting_ready_002 with dissolve
            ril "Don't let anybody hear you say that. The people around here treat these Sharp meetings very seriously."
            pro "I'd take dancing with you {i}very{/i} seriously. You wouldn't be disappointed."
            ril "I don't think I would be. But I can't let a celebration make me lose my focus."
            pro "Use it as motivation."
            ril "*laughing* Maybe I will."

    scene e005_025_005_viridianmeeting_ready_003 with dissolve
    ril "I'm going to see if there's anybody available to talk to."
    pro "What should I do until then?"
    ril "Make yourself comfortable. Relax. Don't worry about trying to fit in with everybody else."
    pro "I'm not going to force anything. We're here to give an honest pitch."
    ril "Exactly."

    scene e005_025_006_viridianmeeting_ready_004 with dissolve
    ril "I think there's someone available on the other side of the room."
    ril "I'll go over there and make the initial pitch to see if he's willing to hearing more."
    ril "I'll come and get you once he's open to listening."
    pro "I can do that."

    scene e005_025_007_viridianmeeting_separate_001 with dissolve
    ril "I'll try not to keep you waiting too long."
    pro "Take your time. Do what you gotta do. Whatever it takes."
    ril "I'll be right back."

    scene e005_025_008_viridianmeeting_separate_002 with dissolve
    pro "(Riley's younger than everybody here but she looks like she fits in with all of these suits.)"
    pro "(She has the maturity of someone a lot older.)"
    pro "(I shouldn't be surprised the class president knows how to carry herself.)"

    scene e005_025_009_viridianmeeting_separate_003 with dissolve
    pro "(It's a good thing Billy isn't here. He'd probably be harassing all of these people as soon as he stepped in.)"
    pro "(Gotta play it cool and not seem too eager with these people. I've got the whole night ahead of me.)"

    scene e005_025_010_viridianmeeting_separate_004 with dissolve
    voi "Would you like some champagne, sir?"
    pro "Huh?"

    scene e005_025_011_viridianmeeting_serve_001 with dissolve
    fls005 "Champagne. Would you like one, sir?"
    pro "Champagne..."
    pro "(She looks familiar... That same girl I saw at the PGs and the one dancing with Marisa.)"

    scene e005_025_012_viridianmeeting_serve_002 with dissolve
    fls005 "Sir?"
    pro "(Funny. She has a completely different tone from the first time I talked to her.)"
    pro "(She seems a lot more polite now than the blunt way she was talking to me before.)"
    fls005 "Sir, are you all right?"

    scene e005_025_013_viridianmeeting_familiar_001 with dissolve
    pro "I've seen you around before, haven't I?"
    pro "You were dancing at this same hotel a week ago. I know it was you."

    scene e005_025_014_viridianmeeting_familiar_002 with dissolve
    fls005 "Dancing? I'm sorry, servers aren't allowed to dance during our shifts."
    pro "No, I mean in the other conference room. You were in your underwear."
    fls005 "I'm sorry, you must have me mistaken with someone else. We only have one standard uniform."
    pro "You weren't a server... I'm pretty sure it was you."

    scene e005_025_015_viridianmeeting_familiar_003 with dissolve
    fls005 "I'm only a server. That's the only thing I do at this hotel."
    fls005 "Again, I believe you have me mistaken for someone else, {i}sir{/i}."
    pro "(She seems a little upset. Better not push her too much.)"
    pro "Yeah... Maybe it was someone else... Sorry."

    scene e005_025_016_viridianmeeting_familiar_004 with dissolve
    fls005 "Not a problem, sir."
    fls005 "I'm afraid I can't stay here and chat for long. I have to serve the other guests."
    fls005 "Would you like some champagne?"

    scene e005_025_017_viridianmeeting_curious_001 with dissolve
    pro "Sure, I'll take a glass."

    $ two_choice = True
    menu:
        pro "(Seems like she calmed down a little.)"

        "(Make a joke about the situation.)":
            $ two_choice = False

            pro "I guess I've just been seeing your face everywhere."
            pro "I tend to do that a lot. People in this town look familiar for whatever reason."

            scene e005_025_018_viridianmeeting_curious_002 with dissolve
            fls005 "You don't have to explain yourself, sir."
            fls005 "Do you need anything else?"


        "(Compliment her.)":
            $ two_choice = False
            $ stranger_compliment_005 = True

            pro "I guess I've just been seeing your face everywhere."
            pro "*chuckling* You're so pretty I haven't forgotten your face."
            pro "Maybe you {i}should{/i} be a dancer."

            scene e005_025_018_viridianmeeting_curious_002 with dissolve
            fls005 "That's a very strange thing to say to someone."
            pro "Can't say you're not pretty and lie to you. Are servers not allowed to take compliments?"
            fls005 "...Will that be all, sir?"
            pro "*sigh* Heh."

    pro "Hmmm... Maybe you can help me out. You're a server here."
    pro "Any tips on doing business with these folks?"

    scene e005_025_019_viridianmeeting_caution_001 with dissolve
    fls005 "I'm not in any position to give you any advice on dealing with these people."
    pro "Because you're just a server."
    fls005 "I'm just a server."
    pro "You know, your tie could be pushed up a little more. You'd think a server would be told that..."
    fls005 "...Is there anything else?"
    pro "Thanks for the conversation."
    fls005 "Enjoy your evening, sir. And good luck in your dealings."
    pro "Thanks."

    scene e005_025_020_viridianmeeting_caution_002 with dissolve
    pro "(That's gotta be her.)"
    pro "(If you're spending time around the PGs and pole dancing, I guess you have a reason to keep it a secret.)"
    pro "(Should just let her be.)"

    scene e005_025_021_viridianmeeting_interrupt_001 with dissolve
    dan "What the hell is this? Are they just letting anybody in here?"
    dan "Or are you here to serve champagne?"
    dan "I wouldn't be surprised. I know that coffee shop is down in the dumps."

    scene e005_025_022_viridianmeeting_interrupt_002 with dissolve
    pro "Still mad Billy shoved the offer up your ass?"
    pro "I get it. I'd be pissed, too, if I missed out on a business like that."
    dan "You won't be making smart-ass comments like that once that shop is done."

    scene e005_025_023_viridianmeeting_interrupt_003 with dissolve
    pro "The shop won't be done for a long time."
    pro "There's a reason Sharp was offering so much to Billy. Even he knows who has the best coffee in Sol City."

    scene e005_025_024_viridianmeeting_insult_001 with dissolve
    dan "Ha! Don't make me laugh. That's just a minor inconvenience."
    dan "Sharp already has more property in Midtown than anybody else. Once he starts building, anybody going against him is going down."
    dan "Construction has already started on a new coffee shop. All of your customers are going to flock to it once it opens."
    pro "Once it opens, it's only a matter of time until it closes. Sharp has money but he doesn't have the stature in Midtown that Billy does, you bum."

    scene e005_025_025_viridianmeeting_insult_002 with dissolve
    dan "Watch how you talk to me."
    pro "What for? There's no offer you can give to Billy that'll make him sell. You can't bully him. You can't intimidate him."
    dan "You have no idea who you're messing with."
    pro "You need to start coming up with better insults. You're just saying the same thing over and over."

    scene e005_025_026_viridianmeeting_luck_001 with dissolve
    dan "I just like rubbing it in."
    dan "Billy is going to look back on this moment and regret he didn't take the offer. I can't wait to see him on his knees, begging for whatever money he can get."
    pro "He won't be begging for money once I secure a deal for him. There's more money in Sol City outside of Sharp."

    scene e005_025_027_viridianmeeting_luck_002 with dissolve
    dan "What? Do you really think you can get a deal? You can't be serious."
    pro "It's big business. Even Sharp himself wouldn't waste time opening up a coffee shop if he couldn't make a profit."
    dan "The difference is nobody is going to order that pitiful swill you're peddling as coffee."
    pro "Sharp can spend all the money in the world and he won't be able to make a brew like Billy."

    scene e005_025_028_viridianmeeting_luck_003 with dissolve
    dan "Maybe I should just have you kicked out of here?"
    dan "Who even invited you here?"
    pro "Aren't you just an intern?"
    dan "An intern for Sharp. Get it right."

    scene e005_025_029_viridianmeeting_luck_004 with dissolve
    ril "And I'm an intern, too. I invited him. You don't have any power to kick him out."
    dan "I doubt that. One look at this bum and they'll see he doesn't belong here."
    ril "Give it a rest."

    scene e005_025_030_viridianmeeting_warn_001 with dissolve
    ril "Keep whatever threats you have to yourself."
    ril "Billy already made his decision. He doesn't have to deal with you now. You've got no business with the shop."
    dan "I'm just trying to be a nice guy and remind you all about the opportunity you just missed out on."

    scene e005_025_031_viridianmeeting_warn_002 with dissolve
    ril "You're an intern, Daniel. Maybe you should take a step back from carrying water for Sharp and focus on trying to graduate."
    ril "Sharp will buy and sell you like anybody else. You're not in any position to talk."
    dan "Not when he sees how valuable a commodity I am."

    scene e005_025_032_viridianmeeting_warn_003 with dissolve
    dan "Sharp didn't become the man he is without being the savviest businessman in Sol City."
    dan "I'm smart enough to join the winning team. It's a shame you weren't smart enough to realize it."
    ril "I think we've heard enough."

    scene e005_025_033_viridianmeeting_warn_004 with dissolve
    dan "Just one last word of warning to you."
    dan "Billy got one last offer from Sharp and he turned it down. That's it."
    dan "There's nothing that can be done to save that shop. You made your bed. Sleep in it."
    pro "Tell Sharp not to come crying to us when whatever place he opens can't compete with Billy's."

    scene e005_025_034_viridianmeeting_warn_005 with dissolve
    dan "We'll see about that. Somehow I don't think that'll happen."
    dan "Sharp never loses. If he wants to own all of Midtown, nothing is going to stop him."
    dan "You've been warned."

    scene e005_025_035_viridianmeeting_focus_001 with dissolve
    pro "I can't believe you and that guy are in the same major."
    ril "That's pretty much where the similarities end."
    ril "Daniel's the stereotypical business major who thinks he knows everything about making money."

    scene e005_025_036_viridianmeeting_focus_002 with dissolve
    ril "But I'm not interested in talking about Daniel right now."
    ril "I found someone willing to listen to our pitch."
    pro "Great! Anything I should know?"

    scene e005_025_037_viridianmeeting_focus_003 with dissolve
    ril "I've prepped him a little bit but I'll go into more detail."
    ril "He doesn't need to know the specifics. He only needs a general business plan. Even though there's money involved, this is still subjective."
    pro "And what do I do?"
    ril "Just tell him the truth. The coffee is great. The service is great. The business is a landmark. You know all of this first-hand."
    pro "Got it."
    ril "Let's not keep him waiting."

    scene e005_025_038_viridianmeeting_pitch_001 with fade
    ril "...You already know coffee is a big business. The numbers have been available for decades."
    ril "Midtown is at the heart of the business district. More people live there than anywhere else."
    ril "Even if they commute to work in another part of town, they still have to get a cup of coffee."

    scene e005_025_039_viridianmeeting_pitch_002 with dissolve
    ril "Before they head to work, they need something. There's no pick-me-up better than the caffeine a latte provides."
    ril "And there's no better latte than at Billy Love's. It's the best espresso I've ever had."
    ril "A great product. That's the foundation of any good business."

    scene e005_025_040_viridianmeeting_pitch_003 with dissolve
    ril "With your investment, we'd be able to build on that foundation, literally and figuratively."
    ril "The first step would be to remodel and update the place. Giving Billy's a more refined look to appeal to modern sensibilities will only drive up consumer demand."
    ril "The existing customer base can only increase from that capital investment."

    scene e005_025_041_viridianmeeting_pitch_004 with dissolve
    ril "That growth can later be used to continue expanding the business."
    ril "More capital. Advertising. Personnel. Billy's has a piece of the market share in Midtown. That share can expand exponentially once everybody in Sol City knows about it."
    ril "Your ROI will share that exponential growth. You can keep your investment as long as you want, reaping the benefits of seeing the initial potential."
    ril "This is an opportunity that doesn't come along very often."

    scene e005_025_042_viridianmeeting_idea_001 with dissolve
    ril "My colleague [mc] here has first-hand experience with the business itself."
    ril "He knows how good the coffee is and he's seen how satisfied all of the customers are."
    ril "And he knows there's limitless room for improvement."

    scene e005_025_043_viridianmeeting_idea_002 with dissolve
    ril "Go on, [mc]. Tell him why Billy's has such a bright future in Midtown."
    pro "Right."
    pro "(Riley already said so much and she put it so eloquently.)"
    pro "(I can offer my own perspective on what Billy's is like. All I have to do is be honest.)"

    $ two_choice = True
    menu:
        pro "(What do I say?)"

        "{dip_menu}Midtown is loyal to Billy's.{/dip_menu}":
            $ mc_diplomat +=1
            $ two_choice = False
            play sound "audio/sounds/universal/diplomatconfirm.ogg"

            scene e005_025_044_viridianmeeting_idea_003 with dissolve
            pro "Midtown is loyal to Billy's."
            pro "He's been around for nearly 20 years now. You can't build that kind of business and still be standing without some loyalty."
            pro "With an investment, that loyalty can be expanded. It's good coffee and good service that makes you feel like you're at home."
            pro "You can't get that anywhere else."

            scene e005_025_045_viridianmeeting_idea_004 with dissolve
            ril "Putting a price tag on something like this is impossible."
            ril "You can't build something like this. This comes from years of experience, loyalty, and dedication."
            ril "That's why this is a golden opportunity for you. How often do you get a chance to be a part of a staple business, right in the heart of Midtown?"
            ril "What do you think?"

        "{reb_menu}Billy's will crush the competition.{/reb_menu}":
            $ mc_rebel +=1
            $ two_choice = False
            play sound "audio/sounds/universal/rebelconfirm.ogg"

            scene e005_025_044_viridianmeeting_idea_003 with dissolve
            pro "Billy's will crush the competition."
            pro "You can get coffee anywhere else but whatever fancy chain you might be thinking of doesn't compare to Billy's."
            pro "And that's just the product. The service blows everybody else's out of the water."
            pro "Going to Billy's, you get a real, authentic experience that isn't just trying to sell you a cup of coffee or make a buck. You can't get that anywhere else."

            scene e005_025_045_viridianmeeting_idea_004 with dissolve
            ril "The competition has tried. The competition has failed."
            ril "Over the years, Billy's has proven that they're number one in Midtown when it comes to coffee. At this point, there is no competition."
            ril "This is an opportunity for you now to get in on this at the ground floor as Billy inevitably expands across Midtown and throughout Sol City."
            ril "What do you think?"

    scene e005_025_046_viridianmeeting_interest_001 with dissolve
    fbm005 "You two have a lot of passion about the business. And I have to admit that your idea is intriguing."
    fbm005 "But there's no indication that the coffee market in Midtown isn't up for grabs."
    fbm005 "With Sharp buying so much property, he's bound to go into the market and he has enough money to compete."
    fbm005 "It just wouldn't be a sound investment for me to try and compete with him."

    scene e005_025_047_viridianmeeting_interest_002 with dissolve
    fbm005 "But I admire your enthusiasm. I remember when I was your age and had some great ideas."
    fbm005 "I can't say I can offer you anything for this coffee shop of yours but I'm willing to listen to anything else."
    fbm005 "Otherwise, I'm afraid we're done here."

    scene e005_025_048_viridianmeeting_interest_003 with dissolve
    ril "No... I'm afraid that's the only offer we have on the table right now."
    ril "Billy's is the primary project we're focused on."
    ril "But if you're declining, I guess we're done here."
    pro "It's all right for now."

    scene e005_025_049_viridianmeeting_interest_004 with dissolve
    pro "Let's not waste any more of his time. There are a lot of other people here who are willing to hear our pitch."
    ril "Yeah... I'm sure there are."
    pro "Let's go find'em and see if we can make a deal."

    scene e005_025_050_viridianmeeting_reject_001 with fade
    pro "(So Riley and I go to every person we see, trying to convince them to see the value in Billy's...)"
    ccb005 "I'm sorry but the market is just oversaturated."
    ccb005 "As much of a staple as coffee is, you're still competing with other drink and food markets like smoothie and tea shops."
    ccb005 "I'm afraid I'll have to decline."

    scene e005_025_051_viridianmeeting_reject_002 with dissolve
    pro "(...We try our hardest, telling them they have as much to gain as we do...)"
    sbm005 "An old coffee shop? That's intriguing but I don't see the ROI in that."
    sbm005 "A loyal customer base can change on a dime if there's another option."
    sbm005 "That's just too shaky of a project for me to even consider."

    scene e005_025_052_viridianmeeting_reject_003 with dissolve
    pro "(...But the answer is always the same.)"
    ylbm005 "There's no way you can get me to invest in Midtown right now."
    ylbm005 "It's the worst kept secret in Sol City that Sharp is moving in and scooping up property."
    ylbm005 "The guy's got bottomless pockets. I'd rather be his partner than compete against him."

    scene e005_025_053_viridianmeeting_upset_001 with fade
    ril "*sigh* I should've known better. Everybody is too afraid of Sharp and not willing to take a risk."
    ril "It's a standard numbers game. Regardless of what it is, Billy's is just another small business to them."
    pro "Feels like we talked to a lot of people and they're all giving the same answer."

    scene e005_025_054_viridianmeeting_upset_002 with dissolve
    ril "Nobody here has any guts. Midtown might as well be a ghost town with Sharp moving in."

    menu:
        ril "At this point, we'd have to convince them to not worry about Sharp instead of pitching the shop."

        "{kni_menu}There are still others we haven't talked to.{/kni_menu}":
            $ ril_knight +=1

            pro "There are still others we haven't talked to."
            pro "We have plenty of opportunities left tonight."

            scene e005_025_055_viridianmeeting_upset_003 with dissolve
            ril "Oh, I know. It's just frustrating talking to all of the people we've already spoken to."
            ril "They're like robots, all of them working for Sharp."

        "{jok_menu}I could spike the champagne.{/jok_menu}":
            $ ril_joker +=1

            pro "I could spike the champagne."
            pro "Maybe that'll convince them to take our deal."

            scene e005_025_055_viridianmeeting_upset_003 with dissolve
            ril "That's tempting. But they're drunk off of whatever Sharp's giving them, so I don't think that'd be enough."
            pro "I could spike the champagne a lot."
            ril "*laughing* I don't think you have to go that far. I think we should just take a break before we start pitching again."

        "{smo_menu}Maybe we should use our good looks to our advantage.{/smo_menu}":
            $ ril_smooth +=1

            pro "Maybe we should use our good looks to our advantage."
            pro "It's not often you see a couple of young, hot-looking people like us."

            scene e005_025_055_viridianmeeting_upset_003 with dissolve
            ril "*laughing* There's an idea. I wouldn't want to resort to that yet though."
            pro "It might be our only option."
            ril "Honestly, even that wouldn't be enough to convince them. They're terrified of Sharp."

    pro "I've never seen you this frustrated before. It feels like everything you've ever done has come easy to you."

    scene e005_025_056_viridianmeeting_school_001 with dissolve
    ril "Huh? What do you mean by that?"
    pro "I mean you did so much in high school. Class president. Captain of the women's basketball team. Straight-A student."
    ril "I don't know if any of that came easy to me but you're right about me being frustrated."

    menu:
        ril "Maybe I should have faced more adversity so high school could have toughened me up more for moments like this."

        "{kni_menu}I think you're doing fine.{/kni_menu}":
            $ ril_knight +=1

            pro "I think you're doing fine."
            pro "This is a different crowd of people."

            scene e005_025_057_viridianmeeting_school_002 with dissolve
            ril "I'm not so sure about that. High school was all about the drama and gossip."
            ril "It's the same thing here, except most of it involves a lot more money."
            pro "Never looked at it that way."

        "{jok_menu}I don't think they offered classes on this.{/jok_menu}":
            $ ril_joker +=1

            pro "I don't think they offered classes on this."
            pro "Terrified businessmen unwilling to take a risk aren't something someone normally has to deal with."

            scene e005_025_057_viridianmeeting_school_002 with dissolve
            ril "True. But I can say that for a lot of the things I experienced in high school."
            ril "Now that I think about it, dealing with all of the drama and gossip was harder than any of the classes I took."
            pro "Now {i}that's{/i} something that could frustrate someone."

        "{smo_menu}I feel the same way.{/smo_menu}":
            $ ril_smooth +=1

            pro "I feel the same way."
            pro "A couple of the smartest people back in high school and it wasn't much of a challenge for us, was it?"

            scene e005_025_057_viridianmeeting_school_002 with dissolve
            ril "*laughing* I think we're the only people from Los Setos who got into SCI, so I think you might have a point there."
            pro "We're just two peas in a pod."
            ril "We ran with different crowds though but I guess we do have that in common. I don't think you had to deal with all of the gossip I had to deal with though."
            pro "No, I stayed out of all of that."

    pro "How did you deal with all of the drama in high school?"

    scene e005_025_058_viridianmeeting_school_003 with dissolve
    ril "Honestly, I have no idea."
    ril "I just did whatever I felt at the time and things just kind of worked themselves out."
    pro "That's surprising. You were the most popular girl in school."
    pro "I think your name came up more than a few times in some gossip..."

    scene e005_025_059_viridianmeeting_popular_001 with dissolve
    ril "Is that right?"

    menu:
        ril "And exactly what kind of gossip did my name come up in?"

        "{kni_menu}That you were the friendliest person at school.{/kni_menu}":
            $ ril_knight +=1

            pro "That you were the friendliest person at school."

            scene e005_025_060_viridianmeeting_popular_002 with dissolve
            ril "That's it?"
            pro "That's it."
            ril "That's pretty tame. And I suppose that's not the worst thing I've heard about me."
            pro "I think the only people who had something negative to say about you were the assholes."
            ril "And there were plenty of them to go around."

        "{jok_menu}It involved a paper bag, fire, and a dog...{/jok_menu}":
            $ ril_joker +=1

            pro "It involved a paper bag, fire, and a dog..."

            scene e005_025_060_viridianmeeting_popular_002 with dissolve
            ril "Ha! That's a first. Never heard that one."
            ril "I like the ones that obviously weren't true."
            pro "Are you sure it wasn't?"
            ril "*laughing* Trust me. I didn't have time to waste on practical jokes. But there were some assholes at our school who weren't above that."
            pro "That's for sure."

        "{smo_menu}That you wanted to talk to me but were too shy.{/smo_menu}":
            $ ril_smooth +=1

            pro "That you wanted to talk to me but were too shy."
            pro "I guess I can't blame you."

            scene e005_025_060_viridianmeeting_popular_002 with dissolve
            ril "*soft laugh* Now I {i}know{/i} that's a lie."
            ril "I was never shy about introducing myself to people."
            pro "I guess I was the exception."
            ril "Maybe you were... if I'd seen you around. I guess there was too big of a crowd around me."
            pro "Maybe that's it."

    scene e005_025_061_viridianmeeting_popular_003 with dissolve
    ril "The truth is, as 'popular' as I was, it was only natural people were going to talk about me."
    ril "I was always friendly with everybody I met. I wasn't trying to be popular, it just sort of happened."
    ril "And with popularity comes all of the talking."
    pro "Maybe you should use some of that right now, Miss Popular."

    scene e005_025_062_viridianmeeting_challenge_001 with dissolve
    ril "'Miss Popular'?"
    pro "Sure. Say... I've always wondered just how popular you were... What do you say we put that to the test now?"
    ril "What do you mean?"
    pro "How about we go around the room. We make our pitches by ourselves. Whoever gets a deal wins."

    scene e005_025_063_viridianmeeting_challenge_002 with dissolve
    ril "Like a contest?"
    pro "Sure. How about it?"
    ril "A personal challenge... That could make this interesting."
    ril "But there has to be more to it than the pride of winning. There has to be something at stake."
    pro "I couldn't agree more."

    scene e005_025_064_viridianmeeting_challenge_003 with dissolve
    pro "How about the person who gets the deal gets treated to lunch on the other person?"
    pro "If forcing you to get me a burger isn't enough motivation for you, I don't know what will."
    pro "What do you think?"

    scene e005_025_065_viridianmeeting_challenge_004 with dissolve
    ril "The loser having to take the winner out to lunch."
    ril "Are you sure you can afford it? I know Billy isn't paying you much."
    pro "Ouch. Good thing I won't be paying."
    ril "All right, [mc]. You're on."

    scene e005_025_066_viridianmeeting_bet_001 with dissolve
    ril "I know you're a psych major but this is the business world. It's a little different dealing with these people."
    pro "You might know what it's like to be popular but I can read these people. I just need some time to figure them out."

    $ two_choice = True
    menu:
        ril "We'll see about that."

        "You've just gotta buy me a burger. (Friendly)":
            $ two_choice = False

            pro "You've just gotta buy me a burger."
            pro "No need to stress over something like that. I'm not too picky."
            ril "Pride before the fall."

        "I'm expecting you to take me somewhere special. (Flirt)":
            $ two_choice = False
            $ riley_viridian_date_bet_005 = True

            pro "I'm expecting you to take me somewhere special."

            scene e005_025_067_viridianmeeting_bet_002_flirt_001 with dissolve
            ril "Special? For just a meal?"
            pro "This isn't just a meal. It's about time you took me out somewhere nice."
            ril "You're going to regret saying that."
            pro "Why's that?"
            ril "Because now I expect {i}you{/i} to take me out somewhere special."

            scene e005_025_068_viridianmeeting_bet_003_flirt_002 with dissolve
            pro "Start saving up your money. I'm gonna find a nice place to celebrate this deal I'm about to get."
            ril "It'll be a celebration for the both of us, that's true. It's only right the man pays."
            pro "But not this time."
            ril "*laughing*"

    scene e005_025_069_viridianmeeting_bet_004 with dissolve
    ril "Good luck, [mc]."
    pro "You're the one who needs it, Riley. I'm getting a deal first."
    ril "*soft laugh* We'll see about that."

    scene e005_025_070_viridianmeeting_bet_005 with dissolve
    pro "(Good to see Riley's in a better mood.)"
    pro "(But it's not gonna last long unless one of us gets a deal.)"
    pro "(Can't let her do all of the work on this. Better not relax.)"

    scene e005_025_071_viridianmeeting_greetkate_001 with dissolve
    pro "Kate?"
    kat "Hello, [mc]. I'm surprised to see you here."
    pro "Same here. What are you doing here?"

    scene e005_025_072_viridianmeeting_greetkate_002 with dissolve
    kat "I'm here with Tobias. He thought it would be a good idea if I accompanied him and spoke to the people here."
    kat "There's a chance the psychology department could stay at SCI if there's a donation to help funding."
    pro "This seems like the perfect place to find it."

    scene e005_025_073_viridianmeeting_greetkate_003 with dissolve
    kat "Tobias, you remember [mc]."
    tob "How could I forget the lone psychology major?"
    tob "What an interesting coincidence to run into him."
    kat "Isn't it?"

    scene e005_025_074_viridianmeeting_plans_001 with dissolve
    kat "Might I ask what you're doing here? Is this for school?"
    pro "No, it's not for school but now that you mention it... I suppose these people would be interesting candidates for my thesis."
    kat "Interesting indeed. It takes a certain kind of mindset to do business in this part of town."
    kat "There's no doubt the sensibilities you'd find here would vary greatly from other parts in Sol City."
    pro "I'll keep that in mind but like I said, I'm here for someone else on business."

    scene e005_025_075_viridianmeeting_plans_002 with dissolve
    kat "Of course. I know how important your thesis is to you but it's not something you have to be working on constantly."
    kat "Focus on what business you have and I'm sure your thesis will come along quite well."
    kat "Is there any way I could help you?"
    pro "Help me?"
    kat "Sure. My help isn't exclusive to helping you graduate. If there's a way I can assist you, I'm willing."
    pro "Actually, I'm having trouble closing the deal. Any chance you can give me some insight on talking with these people?"

    scene e005_025_076_viridianmeeting_plans_003 with dissolve
    kat "You're trying to secure a deal. I'm assuming it's something financially significant."
    pro "That's right."
    kat "I won't ask for the specifics but I'm going to assume it's a considerable amount of money."
    kat "My advice for you would be to speak openly and honestly. The people here can see right through a lie."

    menu:
        kat "Once you no longer have to deal with the surface, the subtext can be your priority."

        "{kni_menu}That's good advice.{/kni_menu}":
            $ kat_knight +=1

            pro "That's good advice."
            pro "Is it that simple though?"

            scene e005_025_077_viridianmeeting_plans_004 with dissolve
            kat "Reading someone is never that simple. But a grasp on your conversation is good enough, regardless of how firm it is."
            kat "You can dictate the terms of your negotiations if you look at everything in generalities. Approach your conversations just like that."
            pro "Yeah... I see what you're saying."

        "{jok_menu}But then there's more subtext to deal with.{/jok_menu}":
            $ kat_joker +=1

            pro "But then there's more subtext to deal with."
            pro "Layers and layers of gamesmanship like a lasagna."

            scene e005_025_077_viridianmeeting_plans_004 with dissolve
            kat "That's true. You'll just have to stay on your toes to deal with it."
            pro "Or have a really big fork."
            kat "*laughing* Or have a really big fork. Though I don't know what that would be in this case."

        "{smo_menu}And then I can use my wit and charm.{/smo_menu}":
            $ kat_smooth +=1

            pro "And then I can use my wit and charm."
            pro "That should seal the deal with no problem."

            scene e005_025_077_viridianmeeting_plans_004 with dissolve
            kat "That kind of confidence is good but it can easily be perceived as arrogance."
            pro "Then I'll just have to turn the charm on even more, don't you think?"
            kat "Under these circumstances, it may be a risk. However, that wouldn't be entirely impossible to pull off."

    scene e005_025_078_viridianmeeting_business_001 with dissolve
    kat "Tobias, you've been dealing with these people for years. Maybe there's some advice you can give him."
    tob "I'm not certain there is after what you said. An accomplished psychologist like you knows better than anybody what it takes to deal with these types."
    tob "But maybe I can add to that."

    scene e005_025_079_viridianmeeting_tips_001 with dissolve
    tob "What Kate said is correct. These people have been through enough negotiations and talked enough to see through any BS."
    tob "And they know that it's all about making a dollar. The bottom line is more important than anything else."
    tob "But there is one other thing you should consider."

    scene e005_025_080_viridianmeeting_tips_002 with dissolve
    tob "These people have pride. To make it in Viridian means you earned it."
    tob "You don't get to be rich without knowing what you're doing. Ego gets involved very quickly."
    tob "Bruise someone's ego and that can change things no matter how much money they can make or how tempting an offer can be."
    pro "Be aware of their egos. Got it."

    scene e005_025_081_viridianmeeting_leave_001 with dissolve
    tob "That's all of the advice I have to give."
    tob "I'm going to the bar to get settled in. Please join me, Kate."
    kat "I'll be right with you."

    scene e005_025_082_viridianmeeting_leave_002 with dissolve
    kat "It's been nice running into you. But if there's nothing else I can assist you with, I'll have to excuse myself."
    pro "No problem. You've got business to take care of. Good luck getting a deal."
    kat "And the same to you."

    scene e005_025_083_viridianmeeting_search_001 with dissolve
    pro "(Didn't expect that. Nice running into her.)"
    pro "(Even Tobias gave me some decent advice.)"
    pro "(Better not get distracted though.)"

    scene e005_025_084_viridianmeeting_search_002 with dissolve
    pro "(Who do I talk to though? There's so many of them and they all look the same. Not sure which ones I already talked to.)"
    pro "(Better just go down the line and talk to every single one. Gotta take chances on this.)"

    scene e005_025_085_viridianmeeting_search_003 with dissolve
    pro "(That guy over there looks like he's just finishing up a conversation.)"
    pro "(Better pounce on him while I've still got the chance.)"
    pro "(Do I come up with a better pitch this time? Nah. Can't think too much.)"

    scene e005_025_086_viridianmeeting_greetblake_001 with dissolve
    pro "(Here goes nothing.)"
    pro "Excuse me, sir. Do you have a minute to speak?"

    scene e005_025_087_viridianmeeting_greetblake_002 with dissolve
    pro "I was wondering if..."
    bla "Huh?"
    pro "Oh..."

    scene e005_025_088_viridianmeeting_greetblake_003 with dissolve
    bla "[mc]. Didn't expect to see you here."
    pro "I... didn't expect to see you here either."
    bla "What are you doing here? Working?"

    scene e005_025_089_viridianmeeting_explain_001 with dissolve
    pro "I guess you can say that. I'm here on business like everybody else."
    pro "(No chance I can try to make a deal with this guy. Better just play along.)"
    pro "How about you?"

    scene e005_025_090_viridianmeeting_explain_002 with dissolve
    bla "I'm here for the same reason as everybody else."
    bla "I'm always looking to invest. This is the best place in the city to do that."
    pro "Looks like I'm in the right spot."

    scene e005_025_091_viridianmeeting_explain_003 with dissolve
    bla "Is that so? I'm guessing you're not willing to divulge that information to me."
    pro "Considering how you know me, uh, that's probably not a good idea."
    bla "If you're thinking people will judge you because you're accompanying a dancer to Viridian, there are a lot worse people in this room. Nobody would bat an eye at you if they knew."
    pro "And they all have more money than me. I'll keep my side jobs to myself. For now, at least."

    scene e005_025_092_viridianmeeting_explain_004 with dissolve
    bla "Smart. Sensible. That's more than I can say for most people here."
    bla "But you're not in a position any different from everybody else in that meeting."
    bla "We're all enjoying the view. You're just getting paid for it."
    pro "I'm not ashamed of anything I do. There's just no reason for me to put it out there."
    bla "Understandable. Speaking of which..."

    scene e005_025_093_viridianmeeting_marisa_001 with dissolve
    bla "Have you spoken to our lovely friend Marisa recently?"
    pro "I haven't spoken to her since I was with her working."
    bla "I see. There may be another opportunity for her to dance coming up."
    pro "I'll let her know when I get the chance."

    scene e005_025_094_viridianmeeting_marisa_002 with dissolve
    bla "I have to ask. This is a personal question and you don't have to answer but I'm curious."
    bla "You and Marisa..."

    $ two_choice = True
    menu:
        bla "...Are you two just business partners?"

        "Marisa's cool but it's just business.":
            $ two_choice = False

            pro "Marisa's cool but it's just business."
            pro "She's nothing more than a friend, if that."
            bla "I see..."

            if marisa_kiss_viridian_005 == False:
                scene e005_025_095_viridianmeeting_marisa_003 with dissolve
                bla "My natural curiosity was just getting the better of me."
                bla "When I see a beautiful woman like Marisa, I can only assume everybody who sees her is attracted to her."
                pro "She's pretty but it's work. That's all I'm concerned with."
                bla "Apparently."

            if marisa_kiss_viridian_005 == True:
                scene e005_025_095_viridianmeeting_marisa_003 with dissolve
                bla "I do find it interesting though."
                pro "Huh?"
                bla "You say it's only business but you shared quite an intimate moment with her the last time I saw you two."
                bla "Business partners don't usually kiss if it's just business."
                pro "Maybe you should mind your own business."

                scene e005_025_096_viridianmeeting_marisa_004 with dissolve
                bla "You're right. It was wrong of me to ask that question."
                bla "Marisa's an employee and I suppose my natural curiosity got the better of me."
                pro "You don't need to worry about me or Marisa. She does what you pay her to do."
                bla "Yes... Yes, she does. And that's just fine with me."

        "That's not any of your business.":
            $ two_choice = False

            pro "That's not any of your business."

            scene e005_025_095_viridianmeeting_marisa_003 with dissolve
            bla "And I would never intrude even if it were."
            bla "I'm only curious."

            if marisa_kiss_viridian_005 == False:
                bla "I can't help but get a certain vibe when I see you two together."
                pro "And it's still none of your business."

                scene e005_025_096_viridianmeeting_marisa_004 with dissolve
                bla "Right. My mistake for trying to read into it."
                bla "I'm just curious, is all. Marisa is such a splendid woman, she has many admirers."
                bla "I assumed you would be one of them."
                pro "You can assume what you want. You only need to know that we're working together."
                bla "Yes. Of course."

            if marisa_kiss_viridian_005 == True:
                bla "You two shared a moment that was quite public."
                bla "You don't kiss someone who's just your business partner."
                pro "Do you have a problem with it?"

                scene e005_025_096_viridianmeeting_marisa_004 with dissolve
                bla "Not at all. Just my natural curiosity."
                pro "Just because we kissed doesn't mean you had to watch."
                bla "You misunderstand me. Marisa is a working employee. It truly is my natural curiosity about your relationship."
                bla "But I suppose your relationship is yours and yours alone."
                pro "That's right."
                bla "I'll drop the subject."

    scene e005_025_097_viridianmeeting_advice_001 with dissolve
    bla "Since you're here on business, let me offer you some advice."
    bla "The people here are looking for something. They're not just looking for a deal or to grow their portfolio."
    bla "They want something. They need something. But sometimes they don't know what that is until they see it."
    bla "Sometimes you just have to show it to them."

    scene e005_025_098_viridianmeeting_advice_002 with dissolve
    pro "Right..."
    pro "And how about you? Are you one of those people? Are you looking for something but don't know what it is?"
    bla "Absolutely."

    scene e005_025_099_viridianmeeting_advice_003 with dissolve
    bla "I wouldn't be giving you that advice if it didn't apply to me."
    bla "Keep that in mind, [mc]. They think differently around here."
    bla "But everybody can get figured out eventually. They always do."

    scene e005_025_100_viridianmeeting_advice_004 with dissolve
    pro "*sigh*"
    pro "(Keep running into people I know. Haven't been able to give any pitches.)"
    pro "(My conversations with Blake are always strange but I can't think about that right now.)"
    pro "(Time to go to work.)"

    scene black
    with fade
    pro "(I go down the line, trying to talk to as many people as I can.)"
    pro "(I tell them they have a chance to make money. I tell them it's a once-in-a-lifetime business opportunity.)"
    pro "(I even try to appeal to their ego and give them a chance to one-up Sharp...)"

    scene e005_025_101_viridianmeeting_frustrated_001 with fade
    pro "(...But the result is inevitably the same. For both of us.)"
    ril "Damn."
    pro "No good, huh?"

    scene e005_025_102_viridianmeeting_frustrated_002 with dissolve
    ril "They're barely listening."
    ril "They're mindless zombies, all parroting the same lines about not wanting to touch Midtown."

    menu:
        ril "Maybe it wasn't such a good idea to come here."

        "{kni_menu}It was a good idea.{/kni_menu}":
            $ ril_knight +=1

            scene e005_025_103_viridianmeeting_frustrated_003 with dissolve
            pro "It was a good idea."
            pro "Your heart was in the right place."
            pro "It's not your fault these people look at things the way they do."

            scene e005_025_104_viridianmeeting_frustrated_004 with dissolve
            ril "You're right. But that doesn't make it any less frustrating."
            ril "It's like talking to a brick wall sometimes."
            pro "Maybe we should take another break before we try again."

        "{jok_menu}I had a great time.{/jok_menu}":
            $ ril_joker +=1

            scene e005_025_103_viridianmeeting_frustrated_003 with dissolve
            pro "I had a great time."
            pro "Talking to a bunch of guys in suits like this will make me appreciate the regular people more."

            scene e005_025_104_viridianmeeting_frustrated_004 with dissolve
            ril "It does make you look at the more down-to-earth people in a different light."
            ril "But I guess I can't hold it against these people. They're in it for the money."
            pro "And it's up to us to make'em see the light. We've got a chance."

        "{smo_menu}I've enjoyed spending time with you.{/smo_menu}":
            $ ril_smooth +=1

            scene e005_025_103_viridianmeeting_frustrated_003 with dissolve
            pro "I've enjoyed spending time with you."
            pro "Maybe everybody else isn't so fun to talk to but I like talking to you."

            scene e005_025_104_viridianmeeting_frustrated_004 with dissolve
            ril "And I've had a good time talking to you."
            ril "We could have had this conversation anywhere else though."
            pro "Then we should focus and keep on working if that's the case."

    scene e005_025_105_viridianmeeting_frustrated_005 with dissolve
    ril "You're still up for this?"
    pro "Why not? I told Billy I'd get him a deal, so I'm gonna get him a deal."
    pro "You're not backing out now, are you?"
    ril "No. But I'm sure you're frustrated, too. I don't want you to beat yourself up over my idea."
    pro "You know, back in high school, there were times when studying felt endless."
    pro "Sometimes I thought I would never get through all my reading or finish my essay."
    pro "But it always got done because I just did it."

    scene e005_025_106_viridianmeeting_highschool_001 with dissolve
    ril "You know what? I was the same way in high school."
    ril "Part of the reason I did so well is because everybody else thought it was overwhelming."
    ril "I thought I could make myself stand out if I did something others struggled with."
    pro "I know the feeling. It makes the accomplishment just a little more special."

    scene e005_025_107_viridianmeeting_highschool_002 with dissolve
    ril "Right? Sometimes teachers would give us assignments knowing they couldn't be done."
    ril "But I did'em anyway. Not because I wanted a good grade or because I was trying to get into SCI."

    menu:
        ril "*laughing* Doing work to satisfy my ego..."

        "{kni_menu}Whatever motivation works for you.{/kni_menu}":
            $ ril_knight +=1

            pro "Whatever motivation works for you."
            pro "As long as you're not hurting anybody and the job gets done, it's a good strategy."

            scene e005_025_108_viridianmeeting_highschool_003 with dissolve
            ril "A good strategy is a strategy that works. I'm guessing you were similar to me in some aspects."
            pro "There's a sense of pride that comes with accomplishment. It's only natural."
            ril "It can be addicting."
            pro "I can see that."

        "{jok_menu}I never thought you'd be one to have a big head.{/jok_menu}":
            $ ril_joker +=1

            pro "I never thought you'd be one to have a big head."
            pro "Is that why you were so popular, too?"

            scene e005_025_108_viridianmeeting_highschool_003 with dissolve
            ril "Careful now. I never treated people like they were an assignment."
            pro "But have you ever treated an assignment like it was a person?"
            ril "I don't think I have. That'd just be weird."
            pro "But it would be effective, wouldn't it? Anything to get the job done."
            ril "*laughing* I'll have to think about that next time I have to write a paper."

        "{smo_menu}Doing work to impress yourself...{/smo_menu}":
            $ ril_smooth +=1

            pro "Doing work to impress yourself..."
            pro "So many people were into you that you were even into yourself."

            scene e005_025_108_viridianmeeting_highschool_003 with dissolve
            ril "*laughing* Why do I get the feeling I'm not the only one who was completely into myself?"
            pro "Now that you mention it, I {i}am{/i} pretty amazing."
            ril "I don't think it took just now for you to tell yourself that."
            pro "It never hurts to hear a reminder."
            ril "*laughing* There it is."

    scene e005_025_109_viridianmeeting_bust_001 with dissolve
    ril "We've been here for a bit now. I'd hate for the night to be a waste."
    pro "It's not a waste if we can get a deal."
    ril "Right. But maybe we should take a break for a bit."
    pro "It wouldn't hurt to enjoy the festivities. I've only had one glass of champagne."

    scene e005_025_110_viridianmeeting_bust_002 with dissolve
    ril "And I haven't had any. I'm sure Billy would encourage us to have a drink at least."
    pro "That's an understatement. If Billy were here, he'd be telling us to drink and forget about trying to make a deal."
    ril "Which is why we should keep trying at least."
    pro "We won't stop until they kick us out."

    scene e005_025_111_viridianmeeting_bust_003 with dissolve
    ril "Let's hope it doesn't come to that."
    ril "I'll tell you what, why don't you wait here and I'll get us a couple of glasses."

    menu:
        ril "Maybe you can formulate a plan while you're waiting."

        "{kni_menu}I'm sure I can come up with something.{/kni_menu}":
            $ ril_knight +=1

            scene e005_025_112_viridianmeeting_bust_004 with dissolve
            pro "I'm sure I can come up with something."
            pro "Maybe we're just looking at this from the wrong angle."

            scene e005_025_113_viridianmeeting_drinks_001 with dissolve
            ril "That's possible. Some champagne might help us see things differently."
            pro "If not, at least it tastes good."
            ril "Right? But I'm sure we'll come up with something."
            ril "Wait here. I'll be right back."

        "{jok_menu}Spiking the champagne is the way to go.{/jok_menu}":
            $ ril_joker +=1

            scene e005_025_112_viridianmeeting_bust_004 with dissolve
            pro "Spiking the champagne is the way to go."
            pro "It's foolproof."

            scene e005_025_113_viridianmeeting_drinks_001 with dissolve
            ril "A foolproof way to land us in jail."
            pro "Only if we get caught."
            ril "*chuckling* Keep thinking. I'll be right back."

        "{smo_menu}Maybe we should just chat the night away.{/smo_menu}":
            $ ril_smooth +=1

            scene e005_025_112_viridianmeeting_bust_004 with dissolve
            pro "Maybe we should just chat the night away."
            pro "I think you and I are the only ones who can give one another good company."

            scene e005_025_113_viridianmeeting_drinks_001 with dissolve
            ril "That's tempting. But we shouldn't let good company distract us from what we need to do."
            pro "Champagne. Good company. What more do you need?"
            ril "*chuckling* Stay focused. I'll be right back."

    scene e005_025_114_viridianmeeting_drinks_002 with dissolve
    pro "*sigh*"
    pro "(Riley's almost as determined as I am to get a deal. I'd hate to leave without one.)"
    pro "(If nothing else, I should try to calm her down. It's obvious she's still frustrated.)"

    scene e005_025_115_viridianmeeting_lastchance_001 with dissolve
    pro "(Maybe there's someone I can talk to while she's getting a drink.)"
    pro "(That guy over there...)"

    scene e005_025_116_viridianmeeting_lastchance_002 with dissolve
    pro "(Looks bored, just standing there by himself.)"
    pro "(Don't think I talked to him.)"
    pro "(Maybe I should try a different approach with him.)"

    scene e005_025_117_viridianmeeting_lastchance_003 with dissolve
    pro "(What kind of approach? Professional? Casual?)"
    pro "(Just gotta be honest. The truth will have to be good enough. It has to be.)"

    scene e005_025_118_viridianmeeting_again_001 with dissolve
    pro "Hello, sir. Do you think I could have a minute of your time?"
    olbm005 "Huh?"
    pro "I was wondering if—"

    scene e005_025_119_viridianmeeting_again_002 with dissolve
    pro "(Why does this guy look familiar?)"
    pro "(Wait a second. Is that...)"
    pro "...Unbreakable?"

    scene e005_025_120_viridianmeeting_again_003 with dissolve
    olbm005 "What?"
    pro "You're Unbreakable, aren't you?"
    olbm005 "You're not making any sense, kid. You okay?"
    pro "That's your name. At the PGs."

    scene e005_025_121_viridianmeeting_again_004 with dissolve
    olbm005 "That isn't my name."
    pro "I mean, I know it's not your name but that's what they call you. That's what you go by."
    olbm005 "You sure you don't need some help? Had a little too much champagne? How'd someone like you even get in here?"
    pro "You sound like him, too."

    scene e005_025_122_viridianmeeting_again_005 with dissolve
    olbm005 "*sigh* You won't stop pestering me, will you?"
    pro "I get that you're trying to keep it a secret. I mean, it's not something I want anybody to know about it either."
    olbm005 "You're not the one with a reputation around these parts."
    pro "I see... I don't have to talk about that if you don't want to."

    scene e005_025_123_viridianmeeting_again_006 with dissolve
    olbm005 "Ah, what the hell? You're not the first person to ever see the resemblance."
    unb "Never expected to talk to someone I fought though. Not around here."
    pro "That's not something I ever thought about. I guess Sol City's not as big as I thought."

    scene e005_025_124_viridianmeeting_again_007 with dissolve
    unb "Between you and me, there are people in this city who know everything that's going on. They're just good at keeping secrets."
    unb "Some free advice for you—advice you shouldn't need—but try to keep everything to yourself when you can."
    pro "I'm way ahead of you."

    scene e005_025_125_viridianmeeting_pgs_001 with dissolve
    sau "Name's Saul McCarthy."
    pro "[mc] [mclast]. Nice to meet you, Saul."
    sau "Just remember that's my name. I have no idea who or what Unbreakable is."
    pro "Right... I have to ask though. What's someone like you doing in the PGs?"
    pro "You don't look like someone who needs money."

    scene e005_025_126_viridianmeeting_pgs_002 with dissolve
    sau "That's exactly why. Look around. A bunch of old fuddy-duddies talking about their investments and portfolios and the markets."
    sau "I've been talking that talk all my life. I'm an old man and it got old a long time ago."
    pro "I still don't get what you're looking for out there."

    scene e005_025_127_viridianmeeting_pgs_003 with dissolve
    sau "I have everything I could ever want or need in my life."
    sau "Sometimes I just wanna feel alive. I wanna get my heart pumping again. Nothing does it as well as a fistfight."
    pro "That seems a little extreme, doesn't it? There's nothing else you can do?"
    sau "{i}Nothing{/i} gives you the same adrenaline as putting everything on the line."
    pro "That must be why you don't mind losing."
    sau "I'm winning as soon as I step into that cage."

    scene e005_025_128_viridianmeeting_project_001 with dissolve
    sau "But you didn't come up to me to talk about fisticuffs."
    sau "You got something for me?"
    pro "I might. I have an investment opportunity that's important to me but can make you a lot of money."
    sau "Not that I'm trying to lose money but there's gotta be more to it than that if you're trying to convince me."
    pro "Right. I'm trying to raise money for the coffee shop I work at. It's a landmark in the center of Midtown. If I can get some money for a remodel, I'm sure business would boom."

    scene e005_025_129_viridianmeeting_project_002 with dissolve
    sau "You're trying to get money for a coffee shop? This sounds more like a fundraiser than an investment."
    pro "I'm trying to secure the shop's future. I won't lie to you about that. But if you want to approve a loan, you'll get your investment back plus the interest."
    pro "Or I might even be able to secure a bigger financial stake."
    sau "I've got enough money to open a dozen coffee shops. Why this one?"
    pro "Because your place wouldn't make coffee as good as this place. Plus, you wouldn't get the same atmosphere or service."

    scene e005_025_130_viridianmeeting_project_003 with dissolve
    sau "Coffee is coffee. It's a huge market but most people are just trying to get their caffeine."
    sau "And atmosphere and service can be bought. Pay workers a little extra. Install new technology for streamlined service."
    sau "People don't interact any longer. We stare at screens all day. They just want the coffee."

    scene e005_025_131_viridianmeeting_project_004 with dissolve
    pro "That's just it. At this shop, you get an authentic experience."
    pro "We can't do what other businesses are doing. So, we do what they're {i}not{/i} doing better than anyone else."
    pro "You can get coffee, service, and the atmosphere. Plus, the business is already established. There's a small but loyal customer base."

    scene e005_025_132_viridianmeeting_project_005 with dissolve
    sau "Heh. I almost believe everything you're telling me. This might be some one-of-a-kind experience."
    pro "Everything I've told you is the truth. The coffee is excellent but people come back for other reasons. The place means a lot to them."
    pro "Business is already improving. People just don't know about it yet but when they do, they'll come."

    scene e005_025_133_viridianmeeting_project_006 with dissolve
    sau "Hmmm..."
    sau "With all of the rumors about Sharp, Midtown's a bad investment now."
    sau "A local coffee shop isn't the thing I should be spending my money on if I want to make it back."
    sau "This is a terrible idea for anybody to invest in."
    pro "Please. If you could just give me a chance. I know this is a good investment."
    sau "I do admire your guts..."

    scene e005_025_134_viridianmeeting_offer_001 with dissolve
    sau "All right, I'll make you a deal."
    pro "...You will?"
    sau "I got respect for anybody willing to step into the cage. That proves you've got some balls in whatever it is you're doing."
    sau "What do you need?"
    pro "We would need five-hundred thousand for the remodel."
    sau "Half-a-million dollars, huh?"

    scene e005_025_135_viridianmeeting_offer_002 with dissolve
    sau "All right. No promises but I'll think about it. I gotta see this place to make sure you're serious."
    sau "You can't expect me to plunk down that kinda cash when it could be some cardboard box or your treehouse."
    pro "It's a real place. I'm there every day. You'll see."
    sau "Okay, then. Let's say we have a tentative agreement."
    pro "Great!"

    scene e005_025_136_viridianmeeting_intro_001 with dissolve
    pro "Hey, Riley. Can you come here for a second?"
    ril "Are you sure? I don't want to interrupt your negotiations."
    pro "Everything's coming along fine."

    scene e005_025_137_viridianmeeting_intro_002 with dissolve
    sau "Well... Who's this lovely young woman?"
    pro "Saul, this is my business partner, Riley Fox. She's handling the remodeling numbers for the shop."
    pro "Riley, this is Saul McCarthy. He's willing to put up the money to finance the remodel if everything checks out."

    scene e005_025_138_viridianmeeting_intro_003 with dissolve
    ril "Thank you, Mr. McCarthy. You have no idea what this means to us."
    ril "I know this is a huge investment but I wouldn't be so adamant about this if I didn't believe in it."
    ril "I promise you that you won't regret it."

    scene e005_025_139_viridianmeeting_intro_004 with dissolve
    sau "Let's hold our horses and not get too excited."
    sau "A verbal agreement doesn't mean much until everything is in writing. I've seen it too many times to know."
    sau "I'll need to see this place and get a better look at the financials to see how economically viable its future is."

    scene e005_025_140_viridianmeeting_deal_001 with dissolve
    ril "Sure. I can get those numbers for you."
    ril "The last I checked, everything was trending upward."
    sau "That's a good sign but not a proper indicator of any long-term growth."
    sau "But we'll see once I take a better look at everything."

    scene e005_025_141_viridianmeeting_deal_002 with dissolve
    ril "The shop couldn't be in business for so long if it wasn't able to sustain itself."
    pro "Once you're there and taste the coffee, you'll understand why this is such a good investment."
    pro "There's no other place like it in Sol City."

    scene e005_025_142_viridianmeeting_deal_003 with dissolve
    sau "I'm sure everything will be fine once I see things for myself."
    sau "There's just one more condition I need."
    pro "What is that?"
    sau "A dance with Miss Fox."
    stop backgroundmusic fadeout 1.0

    scene e005_025_143_viridianmeeting_invite_001 with dissolve
    ril "A dance?"
    sau "It's not every day I get to share the floor with a young woman like yourself."
    sau "Humor an old man for just a song."
    ril "Well, I'm not much of a dancer..."

    scene e005_025_144_viridianmeeting_invite_002 with dissolve
    play backgroundmusic "audio/music/dance_waltz_001.ogg" fadein 2.0
    ril "But it looks like a lot of people are on the floor."
    ril "I guess it's not an uncommon business practice."
    ril "And seeing as how you're offering us a deal..."

    scene e005_025_145_viridianmeeting_danceriley_001 with dissolve
    ril "I'm sure a dance is harmless. After all, we could be going into business with him."
    ril "What do you think, [mc]?"

    menu:
        ril "There's nothing wrong with just a dance, right?"

        "{kni_menu}If you're okay with it, I don't see a problem.{/kni_menu}":
            $ ril_knight +=1

            pro "If you're okay with it, I don't see a problem."

            scene e005_025_146_viridianmeeting_danceriley_002_jokerknight_001 with dissolve
            ril "I haven't danced out on a floor since high school. This could be a good way to get my feet back."
            pro "Just try not to hurt yourself."
            ril "*soft laugh* I think I'll be okay."

        "{jok_menu}I could dance in your place for you.{/jok_menu}":
            $ ril_joker +=1

            pro "I could dance in your place for you."

            scene e005_025_146_viridianmeeting_danceriley_002_jokerknight_001 with dissolve
            ril "*laughing* Are you sure? I don't think you'd be okay with another man leading you."
            pro "I'd do my own thing. I can cut a rug like nobody else."
            ril "*laughing* I don't think that's what Saul had in mind."

        "{smo_menu}As long as you're wishing it was me.{/smo_menu}":
            $ ril_smooth +=1

            pro "As long as you're wishing it was me."

            scene e005_025_147_viridianmeeting_danceriley_003_smooth_001 with dissolve
            ril "And why would I do that?"
            pro "I think you'd enjoy it. A lot."
            ril "Don't be too sure about that. I've never seen you dance."
            pro "Then you can imagine what you're missing out on."
            ril "*soft laugh* That could work."

    scene e005_025_148_viridianmeeting_danceriley_004 with dissolve
    sau "How 'bout it, kid?"

    $ two_choice = True
    menu:
        sau "Will you excuse us for a dance?"

        "{dip_menu}Are you sure I can trust you?{/dip_menu}":
            $ mc_diplomat +=1
            $ two_choice = False
            play sound "audio/sounds/universal/diplomatconfirm.ogg"

            pro "Are you sure I can trust you?"

            scene e005_025_149_viridianmeeting_danceriley_005_diplomat_001 with dissolve
            sau "What? Is she your girlfriend or something?"
            pro "I just wanna make sure you're not up to something."

            scene e005_025_150_viridianmeeting_danceriley_005_diplomat_002 with dissolve
            sau "There's a lot of guys out here you should look out for but I'm not one of them."
            sau "Riley's old enough to be my granddaughter."
            pro "If Riley's okay with it, I am."
            sau "It's just a dance. You've got nothing to worry about."

        "{reb_menu}If you disrespect Riley, I'll knock your teeth out.{/reb_menu}":
            $ mc_rebel +=1
            $ two_choice = False
            play sound "audio/sounds/universal/rebelconfirm.ogg"

            pro "If you disrespect Riley, I'll knock your teeth out."
            ril "{i}[mc]{/i}!"

            scene e005_025_151_viridianmeeting_danceriley_006_rebel_001 with dissolve
            sau "*chuckling* I respect a man who stands by his moral principles."
            sau "And I believe you when you say it... I know what you're capable of."
            ril "...What do you mean by that?"
            sau "Nothing. Don't worry, [mc]. I'll have her back in one piece."

    scene e005_025_152_viridianmeeting_danceriley_008 with dissolve
    sau "May I have this dance, Miss Fox?"
    ril "I'm a little out of practice."
    sau "It's easy. You just hold on and let the man lead."

    scene e005_025_153_viridianmeeting_danceriley_009 with dissolve
    pro "(Not sure what to make of him yet. He seems honest about everything.)"
    pro "(He doesn't even seem to mind that I beat him up at the PGs.)"
    pro "(I guess there's no harm in giving him a chance if he's giving {i}us{/i} a chance.)"
    pro "(Better stay on my toes around him and hope this works out.)"

    scene e005_025_154_viridianmeeting_lesson_001 with dissolve
    sau "One, two, three. One, two, three."
    sau "A nice, steady rhythm. Right to the beat."
    sau "It's simple, isn't it?"

    scene e005_025_155_viridianmeeting_lesson_002 with dissolve
    ril "Very simple."
    ril "You're a good teacher."
    ril "I appreciate you willing to give this investment a look."

    scene e005_025_156_viridianmeeting_lesson_003 with dissolve
    sau "That's not a problem."
    sau "But there's other business we need to talk about."
    ril "There is?"
    sau "[mc]... You two are working together..."

    scene e005_025_157_viridianmeeting_lesson_004 with dissolve
    ril "The way you're saying that... It's not a problem, is it?"
    sau "I don't know. Is it?"
    ril "I don't know what you're getting at."
    sau "Oh, you're smarter than you're letting on. You two have a relationship that's more than business."

    scene e005_025_158_viridianmeeting_lesson_005 with dissolve
    ril "*chuckling* We're friendly, sure. I've spent enough time around him to know that."
    sau "And are you more than friends?"
    ril "I don't think so. We barely know each other."
    sau "You do like him though, don't you?"

    if ril_knight >= ril_joker and ril_knight >= ril_smooth:
        ril "I like how honest he is."
        ril "He might be the nicest guy I've ever met. He's sweet. Caring. Compassionate. Sympathetic."
        ril "It's easy to be his friend."

    elif ril_joker > ril_knight and ril_joker >= ril_smooth:
        ril "I like that he always makes me laugh."
        ril "He's not afraid of making a joke. It's like he knows the right thing to make me smile."
        ril "He might be the funniest guy I've ever met."

    elif ril_smooth > ril_knight and ril_smooth > ril_joker:
        ril "He's charming. More charming than any man I've ever known."
        ril "He's not afraid to say what's on his mind. He compliments me without worrying about what my response will be."
        ril "And he says it like he means it. It's hard to find that in someone these days."

    scene e005_025_159_viridianmeeting_lesson_006 with dissolve
    ril "Not that I mind but these are pretty personal questions after just meeting someone?"
    ril "Is this about business or just something you noticed?"
    sau "Both."

    scene e005_025_160_viridianmeeting_lesson_007 with dissolve
    sau "I see something between you two. A unique friendship."
    sau "Maybe I'm just seeing things and it doesn't mean anything."
    sau "Or maybe there's more to it and you {i}do{/i} have something."
    sau "But I always make it a point not to make business personal. You have to separate the two. Even if it's just a friendship."
    sau "You're getting into actual legal territory in certain situations."
    sau "Things can get messy when you're doing business and emotions get involved. You understand what I'm saying?"
    ril "Yeah... I think I do."

    scene e005_025_161_viridianmeeting_lesson_008 with dissolve
    sau "But enough of that serious talk. How about we just enjoy the rest of this dance, eh?"
    ril "I can do that."
    sau "I won't move too fast for you. I'm an old man, you know."
    ril "*laughing* I think you found the right pace."

    scene e005_025_162_viridianmeeting_watch_001 with dissolve
    pro "(Riley looks like she's having a good time.)"
    pro "(Wonder what they're talking about...)"

    scene e005_025_163_viridianmeeting_watch_002 with dissolve
    kat "Hello, [mc]."
    pro "Hi, Kate."
    pro "Is something wrong?"

    scene e005_025_164_viridianmeeting_watch_003 with dissolve
    kat "I'm fine. Tobias is conducting negotiations and I saw you standing by yourself."
    pro "Just watching my business partner out on the dance floor."
    kat "I'm not intruding, am I?"
    pro "I'd rather talk to you than stand here and talk to myself."

    scene e005_025_165_viridianmeeting_watch_004 with dissolve
    kat "This is an interesting crowd, isn't it?"
    kat "Much different from the SCI students we're both used to seeing."
    pro "That's an understatement. Everybody here is a professional with so much experience, I've never felt so out of place before."

    scene e005_025_166_viridianmeeting_people_001 with dissolve
    kat "Might I ask how your business is coming along?"
    pro "Pretty good. I think I might have the deal I was looking for."
    kat "That's wonderful! It seems you've managed to navigate through the personalities of these people."
    pro "I don't know about that but I did meet someone interesting enough I could figure them out."

    scene e005_025_167_viridianmeeting_people_002 with dissolve
    kat "If you've found a business deal, I would say you were successful. You should take pride in that."
    kat "Maybe that's something you should consider for your thesis."
    pro "I've thought about it. It'd be tough to harness all of these personalities and get an idea of what they're like."

    menu:
        kat "If you're interested, I'm sure I can find someone willing who can give you some insight."

        "{kni_menu}Thanks. I appreciate that.{/kni_menu}":
            $ kat_knight +=1

            pro "Thanks. I appreciate that."

            scene e005_025_168_viridianmeeting_people_003 with dissolve
            kat "I want to help you with your thesis as much as I can. This can be mentally overwhelming at times."
            kat "I'll do what I can to help you in that regard."
            pro "I'm sure I can figure something out if you can't."

        "{jok_menu}You must have an address book of interesting people.{/jok_menu}":
            $ kat_joker +=1

            pro "You must have an address book of interesting people."

            scene e005_025_168_viridianmeeting_people_003 with dissolve
            kat "I have access to a lot of people. But I would never violate their privacy."
            kat "I would only recommend individuals appropriate for your project, like Vanessa."
            pro "Someone as interesting as Vanessa... I'm not so sure I should meet anybody else now."
            kat "*soft laugh*"

        "{smo_menu}I think I'm handsome enough I can pull it off myself.{/smo_menu}":
            $ kat_smooth +=1

            pro "I think I'm handsome enough I can pull it off myself."
            pro "Talking to people in Viridian is like talking to anyone else."

            scene e005_025_168_viridianmeeting_people_003 with dissolve
            kat "You might be joking but I'm sure your charm could be enough to influence people to open up to you."
            kat "Individuals in Viridian have a different mindset but they're still human."
            pro "Exactly. I can break someone down no matter where they're from."
            kat "With confidence like that, I'm sure you can."

    scene e005_025_169_viridianmeeting_people_004 with dissolve
    kat "More than anything else, just remember that you want to be able to contain everything you're doing."
    kat "More data for your thesis is always better but you can make proper generalizations even if the data isn't so broad."
    pro "I plan on doing as much as I can and leaving no stone unturned. I want to know what Sol City is all about."
    kat "You know you always have my blessing, regardless of which path you take."

    scene e005_025_170_viridianmeeting_psych_001 with dissolve
    pro "How about you? Have you had any success tonight?"
    pro "I think helping out the psych department is a great investment for anybody here."
    pro "I mean, if you can share that information with me."

    scene e005_025_171_viridianmeeting_psych_002 with dissolve
    kat "I have no issue divulging that information to you, since this pertains to your education in some way."
    kat "It's hard to tell whether tonight has been a success. Decisions like this aren't made in a single night."
    kat "Considerations would still have to be taken to the school board and the president."
    pro "I can see how things wouldn't be so simple..."

    scene e005_025_172_viridianmeeting_psych_003 with dissolve
    kat "I trust Tobias though."
    kat "The man is a negotiator and well-spoken. He wouldn't have gotten into the position he is right now if he weren't."
    kat "And he cares about the psychology department, which I think is more important than anything else."
    pro "Passion is always a good thing."

    scene e005_025_173_viridianmeeting_psych_004 with dissolve
    kat "I've seen how driven he can be when he's passionate about something."
    pro "From the few times I've talked to him, he's seemed intense."
    pro "Has he always been like that?"
    kat "That's very insightful of you. No, he hasn't."

    scene e005_025_174_viridianmeeting_psych_005 with dissolve
    kat "I've counseled him like I have so many others."
    kat "One thing he has going for him is that he {i}is{/i} very intelligent."
    kat "I can only guide people a certain way during our sessions and he was smart enough to take my guidance to improve himself for the better."
    pro "I can't imagine someone not taking your guidance otherwise."

    scene e005_025_175_viridianmeeting_agenda_001 with dissolve
    kat "When I see Tobias and others I've worked with, and the progress they've made..."
    kat "...It makes me think that maybe I'm done."
    pro "Huh? What do you mean?"
    kat "I'm older. I'm accomplished. I should celebrate what I already have."

    scene e005_025_176_viridianmeeting_agenda_002 with dissolve
    kat "I'm always changing my mind every day."
    kat "*laughing* One day, I wonder how strange my life would be if I weren't a dean at SCI."
    kat "The next, I tell myself to get out there and explore."
    pro "Maybe I can counsel you. We all need someone to talk to."
    kat "Maybe you should."

    scene e005_025_177_viridianmeeting_agenda_003 with dissolve
    kat "Even tonight, watching those people out there gives me an odd feeling."
    kat "Some of them are dancing to enjoy themselves and to let their minds roam for a moment."
    kat "Others are still discussing business and completely unaware that they're dancing."

    scene e005_025_178_viridianmeeting_agenda_004 with dissolve
    kat "It's fascinating to watch other people."
    kat "I almost wish I could see myself through different lenses."
    pro "Nobody can do that, so there's no point in thinking too hard about it."

    scene e005_025_179_viridianmeeting_choice_001 with dissolve
    kat "*laughing* You're right. I know better than to worry about something that can never be."
    kat "I apologize for going on another existential tangent. I've been doing that a lot lately around you."
    kat "I suppose it's just because I feel so comfortable talking to you."

    $ two_choice = True
    menu:
        kat "Feel free to speak your mind. You know I'm willing to listen."
        "Both":
            $ two_choice = False

            scene e005_025_180_viridianmeeting_friendly_001 with dissolve
            pro "How about we just watch everybody dance?"
            pro "I'm sure we can make some interesting observations."

            scene e005_025_181_viridianmeeting_friendly_002 with dissolve
            kat "I'm always open to people watching."
            kat "That's not something normal people would find interesting though."
            pro "I guess psychologists aren't normal people then."
            kat "You would be right about that."

            scene e005_025_182_viridianmeeting_friendly_003 with dissolve
            pro "Is it wrong to analyze people and judge them based on how they're dancing?"
            kat "If that judgment was on their dancing ability, I think it would be a bit mean-spirited. But I'm assuming you mean their body language."
            pro "That'd be it."
            kat "Everybody appears cordial. There may be some underlying tension regarding business deals and proposals but they appear more focused on the dance than the discussion."
            pro "That's interesting that you can see that."

            scene e005_025_183_viridianmeeting_friendly_004 with dissolve
            kat "In this kind of situation, a dance like this is a relief from all of the tension."
            kat "The seriousness of all the negotiations is subdued and now they can enjoy the night."
            kat "The majority of the people here are affluent enough they don't have any immediate worries."

            scene e005_025_184_viridianmeeting_friendly_005 with dissolve
            pro "Not to mention all of the champagne flowing through here. I think some of these people are a little looser than they appear."
            kat "*soft laugh* There's a distinct possibility of that."
            pro "I wouldn't hold that against them. If I had that kind of money, I'd enjoy it as much as I could."

            scene e005_025_185_viridianmeeting_friendly_006 with dissolve
            pro "How about you? Are you a dancer?"
            pro "Or is there something else you do to unwind?"

            scene e005_025_186_viridianmeeting_friendly_007 with dissolve
            kat "Oh, I don't do anything special to unwind."
            kat "I still quite enjoy all of the work I do at school."
            kat "I'm not sure I fit in entirely with this group even though I'm similar to their age."

            scene e005_025_187_viridianmeeting_friendly_008 with dissolve
            kat "That young woman dancing over there appears significantly younger than everybody else."
            kat "I'm surprised there's someone her age here."
            kat "She looks like she could be a student at SCI."
            pro "Funny you should say that because she's the one I'm working on a business project with."

            scene e005_025_188_viridianmeeting_aboutriley_001 with dissolve
            kat "Oh, what a coincidence."
            kat "I trust your relationship with her is amicable."
            pro "We're cool. We couldn't have gotten this far if that weren't the case."

            scene e005_025_189_viridianmeeting_aboutriley_002 with dissolve
            kat "I'm glad to hear that."
            kat "As I've told you before, it's good for your mental health to associate with friends."
            kat "Having a friend who's in your age group is beneficial because they can empathize more comfortably with you."
            pro "Riley and I have a lot in common. We're from the same high school, too."

            scene e005_025_190_viridianmeeting_aboutriley_003 with dissolve
            kat "I see. You've known each other a long time then."
            pro "Well... We didn't really {i}know{/i} each other..."
            pro "We just went to the same high school."

            $ two_choice = True
            menu:
                pro "I've been getting to know her better though."

                "I hope we can become good friends.":
                    $ two_choice = False

                    pro "I hope we can become good friends."
                    kat "I'm certain you already are. I see no reason why you wouldn't be."

                "I hope she and I get closer.":
                    $ two_choice = False
                    $ kate_like_riley_005 = True

                    pro "I hope she and I get closer."
                    pro "I wouldn't mind being more than friends with her."

                    if kat_knight >= kat_joker and kat_knight >= kat_smooth:
                        kat "You're an upstanding young man. I'm sure the feeling is mutual for her."
                        pro "I don't know how she feels but it's not something I worry about."

                    elif kat_joker > kat_knight and kat_joker >= kat_smooth:
                        kat "You have a good sense of humor. I think you two would get along well if you're as carefree as you are with me."
                        pro "I'd like to think so."

                    elif kat_smooth > kat_knight and kat_smooth > kat_joker:
                        kat "I'm sure you've done your best to try your charms on her."
                        pro "Is that bad?"
                        kat "*laughing* Not at all. It was merely an observation."

            scene e005_025_191_viridianmeeting_aboutriley_004 with dissolve
            kat "I didn't mean to comment on your relationship."
            kat "I just feel so comfortable talking to you that I have a natural inclination to help."
            pro "No problem. I know that anything we say between each other stays between us."
            kat "That's true. You have my confidentiality even outside of the office."

            scene e005_025_192_viridianmeeting_goodbyefriend_001 with dissolve
            kat "It looks like the song is over."
            kat "I should probably get back to Tobias to see if there's anything I can do to help him."
            kat "It was a pleasure talking to you."
            pro "Thanks, Kate. The pleasure is mine."
            stop backgroundmusic fadeout 2.0

            scene e005_025_193_viridianmeeting_goodbyefriend_002 with dissolve
            kat "If there's anything else you need, feel free to look for me."
            pro "I should be okay but I'll keep that in mind."
            kat "Enjoy the rest of your night, [mc]."
            pro "You, too."
            $ kate_viridian_dance_005 = True

            scene e005_025_194_viridianmeeting_flirty_001 with dissolve
            pro "How about we forget about all this and dance?"
            pro "No sense in letting everybody else have all of the fun."

            scene e005_025_195_viridianmeeting_flirty_002 with dissolve
            kat "I'm not much of a dancer."
            pro "That doesn't matter."
            kat "You want to dance with me?"
            pro "I don't see why not."

            scene e005_025_199_viridianmeeting_leaddance_001 with dissolve
            pro "I cleared out a spot on the dance floor. There's plenty of room for us now."
            pro "How 'bout it?"

            scene e005_025_200_viridianmeeting_leaddance_002 with dissolve
            kat "*soft laugh* Since you're insisting, I don't see the harm."
            kat "I suppose it would be a good way to pass the time."

            scene e005_025_201_viridianmeeting_leaddance_003 with dissolve
            kat "It's been so long since I've danced, I think I might have lost a step."
            pro "Then it's time you went looking."
            pro "Don't worry. I'm sure we'll find it somewhere around here."

            scene e005_025_202_viridianmeeting_leaddance_004 with dissolve
            kat "You seem to know what you're doing."
            pro "Not really. I'm just copying everybody else."
            kat "*soft laugh* Well, you're doing a good job so far."
            kat "I'll follow your lead."

            scene e005_025_203_viridianmeeting_leaddance_005 with dissolve
            pro "Follow my lead..."
            pro "What is everybody else doing?"
            pro "Give me a second to figure this out."
            kat "Of course."

            scene e005_025_204_viridianmeeting_practice_001 with dissolve
            pro "One, two, three. One, two, three. One, two, three."
            kat "*soft laugh* I'm not used to the counting but it helps."
            pro "Just a few more counts and I should have it."
            kat "I think you already do."

            scene e005_025_205_viridianmeeting_practice_002 with dissolve
            kat "You're a natural."
            pro "It helps having a partner who's willing to follow."
            kat "You're doing most of the work. I'm only moving where you're leading me."
            pro "Who would've thought dancing could be so simple?"

            scene e005_025_206_viridianmeeting_dancing_001 with dissolve
            kat "It's part of the reason people are able to have business discussions."
            kat "The dance is just a distraction to lull someone into a state of relaxation so they make a bad deal."
            pro "Remind me not to negotiate with anybody while I'm dancing."
            kat "*soft laugh*"

            scene e005_025_207_viridianmeeting_dancing_002 with dissolve
            kat "I don't think that's something you have to worry about with me."
            pro "Are you sure? Maybe I can convince you to forget about this whole thesis thing and let me graduate without it."
            kat "*laughing* You'll have to try harder than that."
            pro "I accept that challenge."

            scene e005_025_208_viridianmeeting_look_001 with dissolve
            kat "Oops. Almost stepped on your feet there."
            pro "You're fine."
            kat "You distracted me enough that I wasn't even thinking about dancing."
            pro "Looks like it's working then."

            scene e005_025_209_viridianmeeting_look_002 with dissolve
            kat "Just need a few seconds to keep moving our feet at the same rhythm."
            pro "Find the meter in the song."
            kat "I think I have it back."
            pro "(She's distracted...)"

            $ two_choice = True
            menu:
                pro "(While she's not looking, maybe I should...)"

                "(Keep your composure.)":
                    $ two_choice = False

                    pro "(Better not. No idea how she'd react if she caught me.)"

                "(Take a peek down her shirt.)":
                    $ two_choice = False

                    scene e005_025_210_viridianmeeting_look_003 with dissolve
                    pro "*sigh*"
                    pro "(Never thought I'd ever be this close to her...)"
                    pro "(Looks like she has a nice body underneath her shirt, even for an older woman.)"

            scene e005_025_211_viridianmeeting_look_004 with dissolve
            kat "There we are. Right back into it."
            pro "How about we just dance and not worry about negotiations, discussions, or even figuring out the steps?"
            kat "Yes, I'd enjoy that."

            scene e005_025_212_viridianmeeting_curious_001 with dissolve
            tob "...It's a sound investment. The benefits you'd reap from it are tenfold."
            slbm005 "I'm not so sure about that, Tobias. I just don't see the monetary gains from investing in a school, let alone one with an endowment like SCI."
            tob "You know there are board members who have control over that endowment. You would have more input on this particular department."
            slbm005 "And what's so great about this department again?"
            tob "They have one of the finest minds working for them."

            scene e005_025_213_viridianmeeting_curious_002 with dissolve
            tob "Where is she?"
            tob "She was just here a moment ago..."
            tob "She couldn't have left..."

            scene e005_025_214_viridianmeeting_curious_003 with dissolve
            tob "(Oh...)"
            tob "(Dancing with her student...)"
            tob "(Hmmm...)"

            scene e005_025_215_viridianmeeting_curious_004 with dissolve
            slbm005 "Tobias? Are you all right?"
            tob "Fine, fine."
            tob "Just fine."
            slbm005 "About that person you were talking about..."
            tob "Dr. Kate Garcia. She's an exceptional woman..."

            scene e005_025_216_viridianmeeting_comfort_001 with dissolve
            kat "You're a fast learner."
            pro "It's not the most complicated dance."
            pro "Then again, I have a great partner, remember?"

            scene e005_025_217_viridianmeeting_comfort_002 with dissolve
            kat "I think you're a great partner as well."
            kat "I shouldn't be surprised someone like you would pick this up so quickly."
            pro "What do you mean?"

            if kat_knight >= kat_joker and kat_knight >= kat_smooth:
                kat "You always seem to say the right thing. It seems appropriate you would know the right thing to do as well."

            elif kat_joker > kat_knight and kat_joker >= kat_smooth:
                kat "You have a flair for the dramatic, always saying something that others would deem inappropriate but making a joke out of it."
                kat "You've managed to find amusement in something as mundane as a dance."

            elif kat_smooth > kat_knight and kat_smooth > kat_joker:
                kat "You have a certain charm about you. Dancing is a form of partnership."
                kat "Someone like you would have a natural proclivity to it."

            pro "I don't know how much that applies to me but what I do know is that I'm comfortable dancing with you."

            scene e005_025_218_viridianmeeting_comfort_003 with dissolve
            stop backgroundmusic fadeout 3.0
            $renpy.sound.play("audio/sounds/universal/heartbeat_001.ogg", loop=True)
            kat "I feel the same way. Forgive me for what I'm about to say but..."
            pro "But what?"
            kat "I can't remember the last time I felt this comfortable with someone. I feel safe in your arms. I feel... secure."

            $ two_choice = True
            menu:
                kat "I like this feeling."

                "I like this feeling, too.":
                    $ two_choice = False

                    pro "I like this feeling, too."

                    scene e005_025_219_viridianmeeting_comfort_004 with dissolve
                    kat "It's..."
                    pro "It's what?"
                    kat "It's... It's nothing."
                    stop sound

                "I'm sure you'll like it more if you move closer.":
                    $ two_choice = False
                    $ kate_dance_close_005 = True

                    pro "I'm sure you'll like it more if you move closer."

                    scene e005_025_219_viridianmeeting_comfort_004 with dissolve
                    kat "I... I don't think that would be appropriate."
                    pro "You look beautiful tonight, Kate."
                    kat "[mc]... That isn't appropriate either."
                    pro "You just said you're comfortable in my arms."
                    kat "I know... I just... No..."
                    pro "It's okay. I'm here."
                    kat "I think we're fine dancing as we are."
                    stop sound

            scene e005_025_220_viridianmeeting_songend_005 with dissolve
            kat "That's the end of the song."
            pro "Too bad. I was just getting into it."
            kat "As was I. But it was enjoyable while it lasted."
            pro "We'll have to do it again."
            kat "Perhaps."


            scene e005_025_221_viridianmeeting_goodbyeflirty_001 with dissolve
            kat "I'm sure Tobias is interested in speaking to me right now."
            kat "Thank you for keeping me company. I enjoyed that dance."
            pro "Me, too. Good luck with your deal."
            kat "The same to you, [mc]."
        "How about we just watch everybody dance? (Friendly)":
            $ two_choice = False

            scene e005_025_180_viridianmeeting_friendly_001 with dissolve
            pro "How about we just watch everybody dance?"
            pro "I'm sure we can make some interesting observations."

            scene e005_025_181_viridianmeeting_friendly_002 with dissolve
            kat "I'm always open to people watching."
            kat "That's not something normal people would find interesting though."
            pro "I guess psychologists aren't normal people then."
            kat "You would be right about that."

            scene e005_025_182_viridianmeeting_friendly_003 with dissolve
            pro "Is it wrong to analyze people and judge them based on how they're dancing?"
            kat "If that judgment was on their dancing ability, I think it would be a bit mean-spirited. But I'm assuming you mean their body language."
            pro "That'd be it."
            kat "Everybody appears cordial. There may be some underlying tension regarding business deals and proposals but they appear more focused on the dance than the discussion."
            pro "That's interesting that you can see that."

            scene e005_025_183_viridianmeeting_friendly_004 with dissolve
            kat "In this kind of situation, a dance like this is a relief from all of the tension."
            kat "The seriousness of all the negotiations is subdued and now they can enjoy the night."
            kat "The majority of the people here are affluent enough they don't have any immediate worries."

            scene e005_025_184_viridianmeeting_friendly_005 with dissolve
            pro "Not to mention all of the champagne flowing through here. I think some of these people are a little looser than they appear."
            kat "*soft laugh* There's a distinct possibility of that."
            pro "I wouldn't hold that against them. If I had that kind of money, I'd enjoy it as much as I could."

            scene e005_025_185_viridianmeeting_friendly_006 with dissolve
            pro "How about you? Are you a dancer?"
            pro "Or is there something else you do to unwind?"

            scene e005_025_186_viridianmeeting_friendly_007 with dissolve
            kat "Oh, I don't do anything special to unwind."
            kat "I still quite enjoy all of the work I do at school."
            kat "I'm not sure I fit in entirely with this group even though I'm similar to their age."

            scene e005_025_187_viridianmeeting_friendly_008 with dissolve
            kat "That young woman dancing over there appears significantly younger than everybody else."
            kat "I'm surprised there's someone her age here."
            kat "She looks like she could be a student at SCI."
            pro "Funny you should say that because she's the one I'm working on a business project with."

            scene e005_025_188_viridianmeeting_aboutriley_001 with dissolve
            kat "Oh, what a coincidence."
            kat "I trust your relationship with her is amicable."
            pro "We're cool. We couldn't have gotten this far if that weren't the case."

            scene e005_025_189_viridianmeeting_aboutriley_002 with dissolve
            kat "I'm glad to hear that."
            kat "As I've told you before, it's good for your mental health to associate with friends."
            kat "Having a friend who's in your age group is beneficial because they can empathize more comfortably with you."
            pro "Riley and I have a lot in common. We're from the same high school, too."

            scene e005_025_190_viridianmeeting_aboutriley_003 with dissolve
            kat "I see. You've known each other a long time then."
            pro "Well... We didn't really {i}know{/i} each other..."
            pro "We just went to the same high school."

            $ two_choice = True
            menu:
                pro "I've been getting to know her better though."

                "I hope we can become good friends.":
                    $ two_choice = False

                    pro "I hope we can become good friends."
                    kat "I'm certain you already are. I see no reason why you wouldn't be."

                "I hope she and I get closer.":
                    $ two_choice = False
                    $ kate_like_riley_005 = True

                    pro "I hope she and I get closer."
                    pro "I wouldn't mind being more than friends with her."

                    if kat_knight >= kat_joker and kat_knight >= kat_smooth:
                        kat "You're an upstanding young man. I'm sure the feeling is mutual for her."
                        pro "I don't know how she feels but it's not something I worry about."

                    elif kat_joker > kat_knight and kat_joker >= kat_smooth:
                        kat "You have a good sense of humor. I think you two would get along well if you're as carefree as you are with me."
                        pro "I'd like to think so."

                    elif kat_smooth > kat_knight and kat_smooth > kat_joker:
                        kat "I'm sure you've done your best to try your charms on her."
                        pro "Is that bad?"
                        kat "*laughing* Not at all. It was merely an observation."

            scene e005_025_191_viridianmeeting_aboutriley_004 with dissolve
            kat "I didn't mean to comment on your relationship."
            kat "I just feel so comfortable talking to you that I have a natural inclination to help."
            pro "No problem. I know that anything we say between each other stays between us."
            kat "That's true. You have my confidentiality even outside of the office."

            scene e005_025_192_viridianmeeting_goodbyefriend_001 with dissolve
            kat "It looks like the song is over."
            kat "I should probably get back to Tobias to see if there's anything I can do to help him."
            kat "It was a pleasure talking to you."
            pro "Thanks, Kate. The pleasure is mine."
            stop backgroundmusic fadeout 2.0

            scene e005_025_193_viridianmeeting_goodbyefriend_002 with dissolve
            kat "If there's anything else you need, feel free to look for me."
            pro "I should be okay but I'll keep that in mind."
            kat "Enjoy the rest of your night, [mc]."
            pro "You, too."

        "How about we forget about all this and dance? (Flirt)":
            $ two_choice = False
            $ kate_viridian_dance_005 = True

            scene e005_025_194_viridianmeeting_flirty_001 with dissolve
            pro "How about we forget about all this and dance?"
            pro "No sense in letting everybody else have all of the fun."

            scene e005_025_195_viridianmeeting_flirty_002 with dissolve
            kat "I'm not much of a dancer."
            pro "That doesn't matter."
            kat "You want to dance with me?"
            pro "I don't see why not."

            scene e005_025_199_viridianmeeting_leaddance_001 with dissolve
            pro "I cleared out a spot on the dance floor. There's plenty of room for us now."
            pro "How 'bout it?"

            scene e005_025_200_viridianmeeting_leaddance_002 with dissolve
            kat "*soft laugh* Since you're insisting, I don't see the harm."
            kat "I suppose it would be a good way to pass the time."

            scene e005_025_201_viridianmeeting_leaddance_003 with dissolve
            kat "It's been so long since I've danced, I think I might have lost a step."
            pro "Then it's time you went looking."
            pro "Don't worry. I'm sure we'll find it somewhere around here."

            scene e005_025_202_viridianmeeting_leaddance_004 with dissolve
            kat "You seem to know what you're doing."
            pro "Not really. I'm just copying everybody else."
            kat "*soft laugh* Well, you're doing a good job so far."
            kat "I'll follow your lead."

            scene e005_025_203_viridianmeeting_leaddance_005 with dissolve
            pro "Follow my lead..."
            pro "What is everybody else doing?"
            pro "Give me a second to figure this out."
            kat "Of course."

            scene e005_025_204_viridianmeeting_practice_001 with dissolve
            pro "One, two, three. One, two, three. One, two, three."
            kat "*soft laugh* I'm not used to the counting but it helps."
            pro "Just a few more counts and I should have it."
            kat "I think you already do."

            scene e005_025_205_viridianmeeting_practice_002 with dissolve
            kat "You're a natural."
            pro "It helps having a partner who's willing to follow."
            kat "You're doing most of the work. I'm only moving where you're leading me."
            pro "Who would've thought dancing could be so simple?"

            scene e005_025_206_viridianmeeting_dancing_001 with dissolve
            kat "It's part of the reason people are able to have business discussions."
            kat "The dance is just a distraction to lull someone into a state of relaxation so they make a bad deal."
            pro "Remind me not to negotiate with anybody while I'm dancing."
            kat "*soft laugh*"

            scene e005_025_207_viridianmeeting_dancing_002 with dissolve
            kat "I don't think that's something you have to worry about with me."
            pro "Are you sure? Maybe I can convince you to forget about this whole thesis thing and let me graduate without it."
            kat "*laughing* You'll have to try harder than that."
            pro "I accept that challenge."

            scene e005_025_208_viridianmeeting_look_001 with dissolve
            kat "Oops. Almost stepped on your feet there."
            pro "You're fine."
            kat "You distracted me enough that I wasn't even thinking about dancing."
            pro "Looks like it's working then."

            scene e005_025_209_viridianmeeting_look_002 with dissolve
            kat "Just need a few seconds to keep moving our feet at the same rhythm."
            pro "Find the meter in the song."
            kat "I think I have it back."
            pro "(She's distracted...)"

            $ two_choice = True
            menu:
                pro "(While she's not looking, maybe I should...)"

                "(Keep your composure.)":
                    $ two_choice = False

                    pro "(Better not. No idea how she'd react if she caught me.)"

                "(Take a peek down her shirt.)":
                    $ two_choice = False

                    scene e005_025_210_viridianmeeting_look_003 with dissolve
                    pro "*sigh*"
                    pro "(Never thought I'd ever be this close to her...)"
                    pro "(Looks like she has a nice body underneath her shirt, even for an older woman.)"

            scene e005_025_211_viridianmeeting_look_004 with dissolve
            kat "There we are. Right back into it."
            pro "How about we just dance and not worry about negotiations, discussions, or even figuring out the steps?"
            kat "Yes, I'd enjoy that."

            scene e005_025_212_viridianmeeting_curious_001 with dissolve
            tob "...It's a sound investment. The benefits you'd reap from it are tenfold."
            slbm005 "I'm not so sure about that, Tobias. I just don't see the monetary gains from investing in a school, let alone one with an endowment like SCI."
            tob "You know there are board members who have control over that endowment. You would have more input on this particular department."
            slbm005 "And what's so great about this department again?"
            tob "They have one of the finest minds working for them."

            scene e005_025_213_viridianmeeting_curious_002 with dissolve
            tob "Where is she?"
            tob "She was just here a moment ago..."
            tob "She couldn't have left..."

            scene e005_025_214_viridianmeeting_curious_003 with dissolve
            tob "(Oh...)"
            tob "(Dancing with her student...)"
            tob "(Hmmm...)"

            scene e005_025_215_viridianmeeting_curious_004 with dissolve
            slbm005 "Tobias? Are you all right?"
            tob "Fine, fine."
            tob "Just fine."
            slbm005 "About that person you were talking about..."
            tob "Dr. Kate Garcia. She's an exceptional woman..."

            scene e005_025_216_viridianmeeting_comfort_001 with dissolve
            kat "You're a fast learner."
            pro "It's not the most complicated dance."
            pro "Then again, I have a great partner, remember?"

            scene e005_025_217_viridianmeeting_comfort_002 with dissolve
            kat "I think you're a great partner as well."
            kat "I shouldn't be surprised someone like you would pick this up so quickly."
            pro "What do you mean?"

            if kat_knight >= kat_joker and kat_knight >= kat_smooth:
                kat "You always seem to say the right thing. It seems appropriate you would know the right thing to do as well."

            elif kat_joker > kat_knight and kat_joker >= kat_smooth:
                kat "You have a flair for the dramatic, always saying something that others would deem inappropriate but making a joke out of it."
                kat "You've managed to find amusement in something as mundane as a dance."

            elif kat_smooth > kat_knight and kat_smooth > kat_joker:
                kat "You have a certain charm about you. Dancing is a form of partnership."
                kat "Someone like you would have a natural proclivity to it."

            pro "I don't know how much that applies to me but what I do know is that I'm comfortable dancing with you."

            scene e005_025_218_viridianmeeting_comfort_003 with dissolve
            stop backgroundmusic fadeout 3.0
            $renpy.sound.play("audio/sounds/universal/heartbeat_001.ogg", loop=True)
            kat "I feel the same way. Forgive me for what I'm about to say but..."
            pro "But what?"
            kat "I can't remember the last time I felt this comfortable with someone. I feel safe in your arms. I feel... secure."

            $ two_choice = True
            menu:
                kat "I like this feeling."

                "I like this feeling, too.":
                    $ two_choice = False

                    pro "I like this feeling, too."

                    scene e005_025_219_viridianmeeting_comfort_004 with dissolve
                    kat "It's..."
                    pro "It's what?"
                    kat "It's... It's nothing."
                    stop sound

                "I'm sure you'll like it more if you move closer.":
                    $ two_choice = False
                    $ kate_dance_close_005 = True

                    pro "I'm sure you'll like it more if you move closer."

                    scene e005_025_219_viridianmeeting_comfort_004 with dissolve
                    kat "I... I don't think that would be appropriate."
                    pro "You look beautiful tonight, Kate."
                    kat "[mc]... That isn't appropriate either."
                    pro "You just said you're comfortable in my arms."
                    kat "I know... I just... No..."
                    pro "It's okay. I'm here."
                    kat "I think we're fine dancing as we are."
                    stop sound

            scene e005_025_220_viridianmeeting_songend_005 with dissolve
            kat "That's the end of the song."
            pro "Too bad. I was just getting into it."
            kat "As was I. But it was enjoyable while it lasted."
            pro "We'll have to do it again."
            kat "Perhaps."


            scene e005_025_221_viridianmeeting_goodbyeflirty_001 with dissolve
            kat "I'm sure Tobias is interested in speaking to me right now."
            kat "Thank you for keeping me company. I enjoyed that dance."
            pro "Me, too. Good luck with your deal."
            kat "The same to you, [mc]."

    scene e005_025_222_viridianmeeting_rileyjudge_001 with dissolve
    play backgroundmusic "audio/music/viridian_003.ogg" fadein 2.0
    ril "That's that."

    menu:
        ril "How'd I look out there?"

        "{kni_menu}Like a seasoned pro.{/kni_menu}":
            $ ril_knight +=1

            pro "Like a seasoned pro."

            scene e005_025_223_viridianmeeting_rileyjudge_002 with dissolve
            ril "And I've never done anything like that before."
            ril "Imagine how good I'd look if I had some real practice."
            pro "Chase your dreams and believe in yourself. I know you can do it."
            ril "Ha! If I'm going to more meetings like this, I just might."

        "{jok_menu}Like a pizza with extra cheese and pepperoni.{/jok_menu}":
            $ ril_joker +=1

            pro "Like a pizza with extra cheese and pepperoni."

            scene e005_025_223_viridianmeeting_rileyjudge_002 with dissolve
            ril "Are you saying I looked extra tasty and super satisfying?"
            pro "Sure am."
            ril "You know that doesn't make any sense, right?"
            pro "But it sure sounds good though, doesn't it?"
            ril "*chuckling*"

        "{smo_menu}Like an angel dancing on the clouds.{/smo_menu}":
            $ ril_smooth +=1

            pro "Like an angel dancing on the clouds."

            scene e005_025_223_viridianmeeting_rileyjudge_002 with dissolve
            ril "I was that majestic?"
            pro "Heaven might be calling to you because they're missing one of their angels."
            ril "*chuckling* I'd say you were exaggerating if I didn't appreciate it."
            pro "Just calling it like I see it."
            ril "I'm just happy I didn't stumble on my own feet."

    scene e005_025_224_viridianmeeting_rileyjudge_003 with dissolve
    ril "Seriously though, Saul seems all right."
    ril "Not that we had much of a choice but I think he's exactly the kind of open-minded person we were looking for tonight."
    pro "Uh, where is he?"

    scene e005_025_225_viridianmeeting_sealdeal_001 with dissolve
    ril "See for yourself."
    ril "When the dance was done, {i}he{/i} was done. Said he needed a couple of drinks."
    pro "Maybe we {i}should{/i} be having second thoughts about this..."
    ril "*laughing*"

    scene e005_025_226_viridianmeeting_sealdeal_002 with dissolve
    ril "I'd be worried but I'm pretty sure he's legitimate. It's hard to fake it in this room."
    ril "He said he had some business to take care of in the westside though. I wonder what that could be..."
    pro "Uh..."
    ril "Is something wrong?"
    pro "Nothing. It's nothing."

    scene e005_025_227_viridianmeeting_leave_001 with dissolve
    ril "The night started rough but I think we found what we were looking for."
    ril "I'm not sure there's anybody else to talk to."
    pro "And I don't think the people here would be as open as Saul. Looks like we found the one guy who's willing to take the risk we need."
    ril "And that's all that matters."

    scene e005_025_228_viridianmeeting_leave_002 with dissolve
    ril "Looks like you did it."
    pro "And looks like someone owes me a lunch."
    ril "Are we sure you're the one who got the deal? I {i}did{/i} seal it with my dancing."

    if riley_viridian_date_bet_005 == True:
        pro "Sounds like somebody is trying to weasel out of a date."
        ril "To be honest with you, I'm trying to weasel out of a check."
        pro "And here I thought someone with business savvy would be better with money. You businesspeople are all cutthroat."
        ril "Ha! That's how business is done in these parts."

    elif riley_viridian_date_bet_005 == False:
        pro "Don't start this with me."
        ril "*laughing*"

    scene e005_025_229_viridianmeeting_leave_003 with dissolve
    ril "There's nothing left for us here. And to be honest with you, I've had about enough."
    pro "Same here."
    ril "What do you say we get out of here and figure out what's next?"
    pro "Sounds like a good idea."

    stop backgroundmusic fadeout 1.0
    window hide

    scene black
    with fade
    pause

    jump episode05_026_viridian_confrontation

#define config.label_overrides["episode07_020_strip_club_viridian"] = "episode07_020_strip_club_viridian_modded"#???

label episode07_020_strip_club_viridian_modded:

    window hide
    scene e007_020_000_opener_spadesclub_000 with fade
    pause
    $ quick_menu = True

    scene e007_020_001_spadesclub_greet_001 with dissolve
    window show
    play backgroundmusic "audio/music/viridian_001.ogg"
    pro "Hey, Marisa."
    eri "Yo."
    mar "Hey, you two."
    pro "Thanks for coming out."

    scene e007_020_002_spadesclub_greet_002 with dissolve
    mar "Like I said, it's not a problem."
    mar "It's nice that I can finally get out of my comfort zone at the Pink Rabbit."
    mar "I have no idea what a girl like me could expect at a place like this. So thanks for the suggestion and offer to come out here."

    scene e007_020_003_spadesclub_dress_001 with dissolve
    eri "A hot girl like you must get all of the wrong attention from assholes all the time."
    eri "It'd be hard to imagine some jerk in this club being worse than the punks in Old Town but I guess anything's possible."
    eri "Just know that you've got us two watching your back."

    scene e007_020_004_spadesclub_dress_002 with dissolve
    mar "Thanks. It's good to see you again, Erika."
    mar "Funny how it's at another strip club but the circumstances are different."
    mar "That dress looks great on you. And I love what you did with your makeup."

    scene e007_020_005_spadesclub_dress_003 with dissolve
    eri "Well, tonight's important. I had to do something out of the ordinary."
    eri "You think I'll fit in with the rest of the crowd?"
    mar "From what I've seen so far, it's a lot classier than the Rabbit. I think your outfit is perfect."
    mar "The guys in here might be jealous of [mc] for having a woman like you around."

    scene e007_020_006_spadesclub_dress_004 with dissolve
    eri "You hear that, Slick?"
    eri "I look great in this dress. I knew it."
    pro "Huh? I just said that back at your apartment."
    eri "Yeah but it's always great to have another girl's approval. That's how girls are."

    if erika_pursue_005 == True:

        scene e007_020_007_spadesclub_dress_005_pursue_001 with dissolve
        eri "Look at this guy. He's such a stud but he doesn't know too much about how to treat a lady."
        mar "*giggling* I think you both look good together. A beautiful woman and a handsome man."
        eri "He and I are gonna turn some heads. You've got your work cut out for you if you wanna get some attention, Marisa."
        mar "*laughing* I'll try my best."

    elif erika_pursue_005 == False:

        pro "And you have to remind me about it, too?"
        eri "Yep."

    scene e007_020_008_spadesclub_ready_001 with dissolve
    mar "You guys are right on time. My shift is just about to start."
    pro "Do you have everything you need?"
    mar "I've got my outfit in the locker room. Are you two ready to go?"
    pro "I think so."

    scene e007_020_009_spadesclub_ready_002 with dissolve
    mar "Great. Go ahead and get settled in."
    mar "I won't be on stage for a few minutes. If anybody asks how you got in, just let them know you're managing me."
    pro "Managing you. Got it."

    scene e007_020_010_spadesclub_ready_003 with dissolve
    eri "This is exciting."
    pro "What's exciting? Getting some info or walking into a new club?"
    eri "All of it."

    scene e007_020_011_spadesclub_enter_001 with fade
    play backgroundmusic "audio/music/club_003.ogg" fadein 3.0
    mar "Welcome to the Spades Club."
    eri "This is a strip club all right. But just once glance and I could see the guys are dressed differently around here."

    scene e007_020_012_spadesclub_enter_002 with dissolve
    pro "It's different than the Rabbit, that's for sure."
    mar "I think I can get used to this."
    eri "I don't know..."

    scene e007_020_013_spadesclub_enter_003 with dissolve
    eri "Guys in Old Town are more overt about being assholes."
    eri "I'm not gonna give any of these guys a pass. Especially if they have any information we're looking for."
    pro "I wonder if anybody here actually knows anything..."

    scene e007_020_014_spadesclub_plan_001 with dissolve
    eri "I'm not from around here but I wouldn't put it past any of them to do something to Old Town."
    eri "The people on the westside don't even like the people there. There's no telling how much the people here would look down on them."
    pro "The Rules of Old Town still apply around here?"

    scene e007_020_015_spadesclub_focus_001 with dissolve
    eri "Maybe not completely but there are definitely rules to follow."
    eri "Our best bet is to stay on our toes and focus."

    menu:
        eri "We can't let the naked women or the shifty men distract us."

        "{kni_menu}This is a good place to get distracted.{/kni_menu}":
            $ eri_knight +=1

            pro "This is a good place to get distracted."
            pro "But I know what's important."

            scene e007_020_016_spadesclub_focus_002 with dissolve
            eri "It's a shame the circumstances aren't better. I might even have fun in a place like this."
            pro "We'll change the circumstances soon enough."
            eri "Damn right."

        "{jok_menu}Could be worse.{/jok_menu}":
            $ eri_joker +=1

            pro "Could be worse."
            pro "The men could be naked and the women could be shifty, too."

            scene e007_020_016_spadesclub_focus_002 with dissolve
            eri "I wouldn't be surprised if the women were shifty and the men were naked somewhere in this building."
            pro "Uh..."
            eri "Anything's possible, Slick. Especially in a place like this."
            pro "Apparently."

        "{smo_menu}You're enough of a distraction for me.{/smo_menu}":
            $ eri_smooth +=1

            pro "You're enough of a distraction for me."

            scene e007_020_016_spadesclub_focus_002 with dissolve
            eri "I can't be a distraction for you either."
            pro "How can I not be distracted when you look so good in that dress?"
            eri "You don't look so bad yourself, Slick. You know this is about business though."
            pro "Yeah... I know."

    eri "Let's get focused."

    scene e007_020_017_spadesclub_prep_001 with dissolve
    mar "As much as I'd love to stay and chat with you, I should probably get ready to go on stage."
    mar "I'll leave you two to get your business done."

    if marisa_promise_006 == True:

        pro "About that promise you made..."

        scene e007_020_018_spadesclub_prep_002 with dissolve
        mar "*soft laugh* You're bringing that up now?"
        pro "Lots of naked women. Liquor flowing. The atmosphere..."
        mar "Don't worry. I didn't forget. There'll be a time and place. I always keep my promises."
        pro "That's all I needed to hear... For now."
        mar "*laughing* For now."

    elif marisa_promise_006 == False:

        pro "Are you sure you'll be okay up on that stage?"

        scene e007_020_018_spadesclub_prep_002 with dissolve
        mar "As long as there's a pole, I can make it work."
        pro "New audience though."
        mar "New audience, same mindset. I'll be fine, [mc]. Go do what you have to do."
        pro "Thanks again for doing this."
        mar "And thank {i}you{/i} for the idea."

    scene e007_020_019_spadesclub_prep_003 with dissolve
    eri "Hmm... Marisa's got a tight ass, don't you think?"

    if marisa_sex_ever_000 == True:

        pro "Not bad."
        eri "All right, get focused, Slick."
        pro "You're the one talking about her ass."
        eri "I'm talking not gawking."
        pro "What's the difference?"
        eri "What you're doing and what I'm doing."
        pro "*chuckling* Sure. Whatever."

    elif marisa_sex_ever_000 == False:

        pro "So much for being focused..."
        eri "Just an observation. I'm focused, I'm focused."

    scene e007_020_020_spadesclub_split_001 with dissolve
    eri "I think it'd be best if we split up. We can talk to more people and get information faster."
    pro "Are you sure that's a good idea?"
    pro "We came here together. It might be weird if they see us doing our own things separately."

    scene e007_020_021_spadesclub_split_002 with dissolve
    eri "I think it's a good cover."
    eri "I've never lived here but I know people with money like to throw it around."

    if erika_pursue_005 == True:

        eri "People can just assume we're a couple of swingers looking to have some fun with someone new."
        pro "You're right. That's believable. You sure you don't mind me playing the role?"
        eri "You're already doing it with all of the other girls you talk to."
        pro "I don't know what you're talking about."
        eri "*laughing* Whatever."

    elif erika_pursue_005 == False:

        eri "People can assume we're friends trying to help each other find a new experience."
        pro "Hmm... I'm your wingman and you're my wingwoman."
        eri "Something like that."
        pro "Yeah, I think that might work."

    scene e007_020_022_spadesclub_split_003 with dissolve
    eri "I'll go hang by the bar and try to get some action there."
    eri "Get back to me if you find anything out."
    pro "Right."

    scene e007_020_023_spadesclub_split_004 with dissolve
    eri "Remember to stay focused, Slick. We're here on a mission."
    pro "I didn't forget."
    pro "Make sure you don't drink too much."
    eri "Ha! Never do."

    scene e007_020_024_spadesclub_search_001 with dissolve
    pro "(Hmm... Plenty of people to talk to in this club.)"
    pro "(Where do I start?)"
    pro "(Guess I'll just have a seat and scout the area.)"

    scene e007_020_025_spadesclub_wait_001 with dissolve
    pro "(Plenty of girls on stage. Guys drinking and enjoying the show.)"
    pro "(Lots of lively conversation, too.)"

    scene e007_020_026_spadesclub_wait_002 with dissolve
    pro "(I can see how a lot of people could discuss business here.)"
    pro "(It's the perfect place to relax without the pressure of an office or conference room.)"
    pro "(They sure have some kinda life in Viridian...)"
    wvoi "Hey, there."

    scene e007_020_027_spadesclub_intro_001 with dissolve
    rls007 "What are you doing all the way over here by yourself, handsome? The stage is over there."
    pro "Oh... I'm just getting used to the place."
    rls007 "First time here? I can tell. Mind if I have a seat?"
    pro "Not at all."

    scene e007_020_028_spadesclub_intro_002 with dissolve
    rls007 "What's your name, stranger?"
    pro "(Better not give her my real name, just in case anybody finds out what I'm up to.)"
    pro "(It'd be easier to be honest though...)"

    $ two_choice = True
    menu:
        pro "(What kind of name should I give her?)"

        "(Something cool.)":
            $ two_choice = False
            $ stripper_cool_name_007 = True

            scene e007_020_029_spadesclub_intro_003 with dissolve
            pro "Chad. Chad Bigcox."
            pro "Ladies just call me Chad."
            pro "Or Bigcox."
            pro "Whichever you prefer."

            scene e007_020_030_spadesclub_club_001 with dissolve
            rls007 "Oh, I like that name."
            pro "Doesn't everybody?"
            rls007 "My name's Cookie."
            pro "...Like... chocolate chip?"
            cookie "Mmm-hmm, I love cookies."
            pro "Enough to name yourself that..."

        "(Be honest.)":
            $ two_choice = False
            $ stripper_real_name_007 = True

            pro "[mc]."
            pro "That's my name and that's what everybody calls me."

            scene e007_020_030_spadesclub_club_001 with dissolve
            rls007 "[mc]."
            pro "That's it."
            rls007 "I like it."
            cookie "My name's Cookie."
            pro "Cookie. Okay, Cookie."

    scene e007_020_031_spadesclub_club_002 with dissolve
    cookie "So, how do you like the place so far? Are you having a good time?"
    pro "I just got here, so I haven't had much time to form an opinion yet."
    pro "But the place looks fancy. A lot fancier than the clubs I'm used to."

    scene e007_020_032_spadesclub_club_003 with dissolve
    cookie "Oh, sure. I've worked at other clubs in this city before but this is by far the fanciest."
    cookie "Everything is different. The lights. The furniture. The stage. Especially the men."
    pro "I'll bet they are. A lot of rich guys must come around here."
    cookie "You know it."
    pro "(I should start questioning her...)"

    scene e007_020_033_spadesclub_question_001 with dissolve
    pro "Tell me something, Cookie."
    cookie "Sure."
    pro "Do you get a lot of regulars here? Do the guys you see come here often?"

    scene e007_020_034_spadesclub_question_002 with dissolve
    cookie "I think every guy in here is a regular."
    cookie "You don't see too many new guys with money come around."
    cookie "There are a few out-of-towners. They're here one night and then gone the next. But they're rare."
    pro "Then you recognize the customers."
    cookie "I'd say I know a few of them."
    pro "Do you know a guy who has a mark on his nose? He might have bushy eyebrows, too. Dark hair..."

    scene e007_020_035_spadesclub_question_003 with dissolve
    cookie "A mark on his nose?"
    pro "Like a cut or scar."
    cookie "Not that I remember. A lot of guys have bushy eyebrows."
    cookie "Why are you asking?"
    pro "(Making it too obvious. I should pull back a little.)"
    pro "Uh... No reason. Figured you'd get a lot of tough guys coming in here. You know, fighters. Wondered if I should be worried."

    scene e007_020_036_spadesclub_work_001 with dissolve
    cookie "Oh, you don't have to worry about anything like that."
    cookie "There are cameras everywhere and security is tight. You're safer in here than you are outside."
    pro "That's good to know..."
    cookie "So, what do you do for a living? You must be making a lot of money if you're in here."
    pro "Right now I'm just in school. Thought I'd splurge tonight."

    scene e007_020_038_spadesclub_school_001 with dissolve
    cookie "Hey, that's cool. I was thinking about going to school."
    pro "That wouldn't be a bad idea."
    cookie "The money is great here though. Maybe if I save enough I could go somewhere fancy."
    pro "School's pretty expensive around here but I think you'd have enough money for it."

    scene e007_020_039_spadesclub_school_002 with dissolve
    cookie "It's always tough trying to figure out what to study though."
    pro "Sometimes you just have to pick what you like. That's why I went into psychology."
    cookie "That sounds fun. Are you a mind reader?"
    pro "*chuckling* I wouldn't go that far but it does give me some insight into how people think."

    scene e007_020_040_spadesclub_school_003 with dissolve
    cookie "I bet you have a lot of success with the ladies."
    pro "I do okay."
    cookie "I think you're being modest. A handsome young man like you must give girls all they can handle."
    pro "You'd have to ask them."

    scene e007_020_041_spadesclub_stage_001 with dissolve
    cookie "I'd love to stay and chat with you but I'm going up on stage soon."
    pro "I understand... Are you sure you don't remember any regulars that had a scar on their nose?"
    cookie "Sorry. Can't help you."

    scene e007_020_042_spadesclub_stage_002 with dissolve
    cookie "Maybe you should sit up at the stage when I'm dancing. That's where most of the guys hang out."
    cookie "You can get a better look at them for yourself."
    pro "That's a good idea... I can watch you dance while I'm at it."

    scene e007_020_043_spadesclub_fun_001 with dissolve
    cookie "*giggling* You're funny. I think I like you."
    pro "You're not too bad yourself, Cookie."
    cookie "Say, I got an idea."
    pro "Let's hear it."

    scene e007_020_044_spadesclub_fun_002 with dissolve
    cookie "I've still got some time before I go on stage. Why don't you go to the back with me?"
    cookie "I can make you comfortable and we can have some fun. You know, help you enjoy the club and all it has to offer."
    cookie "What do you say?"

    scene e007_020_045_spadesclub_fun_003 with dissolve
    pro "That does sound like fun."
    cookie "Believe me, it is."
    pro "(Maybe it wouldn't hurt to get a lap dance from her... I could try to get more information from her.)"

    scene e007_020_046_spadesclub_fun_004 with dissolve
    pro "Hmm..."
    pro "(Then again, she doesn't seem to have more information than what she already gave me.)"

    scene e007_020_047_spadesclub_fun_005 with dissolve
    pro "(Erika's watching me. Reminding me to stay focused...)"
    pro "(She's right. Can't waste time on enjoying myself when I can help the shop.)"

    if erika_pursue_005 == True:

        scene e007_020_048_spadesclub_fun_006_pursue_001
        pro "(Plus, it'd feel a little weird if I jumped on the first girl I talked to. Especially with Erika right there.)"
        pro "(Better play it cool for now.)"

    cookie "Are you okay?"

    scene e007_020_049_spadesclub_decline_001 with dissolve
    pro "Sorry, I can't right now."

    if erika_pursue_005 == True:

        pro "My girl and I are looking at all of the girls here. She wouldn't approve if I just picked the first girl I talked to."
        cookie "That girl over there? Is she your girlfriend?"
        pro "Something like that."
        cookie "Oh, then you need to get her approval if you're gonna have some fun."
        pro "I'll let you know."

    elif erika_pursue_005 == False:

        pro "My friend and I are just trying to have a relaxing evening tonight. Not take everything in all at once."
        cookie "I understand. Lemme know if you change your mind."
        pro "Sure thing."

    if stripper_cool_name_007 == True:
        cookie "It was nice meeting you, Chad."
        pro "Nice meeting you, too."

    elif stripper_real_name_007 == True:
        cookie "It was nice meeting you, [mc]."
        pro "Nice meeting you, too."

    scene e007_020_050_spadesclub_decline_002 with dissolve
    pro "(She's a nice girl. Too bad she didn't know anything.)"
    pro "(Hope she doesn't start telling people I was asking questions.)"

    scene e007_020_051_spadesclub_decline_003 with dissolve
    pro "(Better play it more subtle with the other girls I talk to.)"
    pro "(I only need a little information from each of them to try and piece something together.)"

    scene black
    with fade
    pro "(I'm alone in my seat but not for long...)"

    scene e007_020_052_spadesclub_interview_001 with dissolve
    pro "(...so I start asking my questions with the description...)"
    csc007 "There are plenty of thin guys who come around here."
    csc007 "I don't really like dancing for them though. They can't handle me."

    scene e007_020_053_spadesclub_interview_002 with dissolve
    pro "(...I give them every detail...)"
    tls007 "Never seen a guy with a scar on his nose. If he did have one, it's because I gave it to him."
    tls007 "I'm done trying to have fun with jerks like that."
    pro "Right..."

    scene e007_020_054_spadesclub_interview_003 with dissolve
    pro "(...But they can never confirm anything for sure.)"
    frg007 "I don't remember too much about the guys I dance with unless they're regulars."
    frg007 "That doesn't sound like any regular I know. Maybe you'd have better luck at the stage and just looking at them yourself."

    scene e007_020_055_spadesclub_idea_001 with dissolve
    pro "Yeah, that's what Cookie said..."
    pro "That's probably a good idea now."

    scene e007_020_056_spadesclub_watch_001 with dissolve
    pro "(This'll be a little trickier than with the dancers.)"
    pro "(Guys will be a lot more suspicious about me asking questions. Gotta be subtle and act like I'm having a good time...)"
    hd007 "Oh, yeah, baby. That's what I like to see. Shake your ass."

    scene e007_020_057_spadesclub_watch_002 with dissolve
    hd007 "Turn that ass this way, baby. Lemme see how soft it is."
    hd007 "Mmm, that looks good. I wanna reach out and bite it."
    hd007 "I like what I see. Make my hot dog nice and plump."
    pro "(Make my hot dog nice and plump?)"

    scene e007_020_058_spadesclub_watch_003 with dissolve
    pro "Yeah... Shake that ass."
    pro "I wanna reach out and just... smack that thing."
    pro "Put it all in my face and eat it like a... Funk Burger."

    scene e007_020_059_spadesclub_intro_001 with dissolve
    pro "She's great, huh?"
    hd007 "Oh, yeah. She knows how to shake those buns, don't she?"
    pro "Good to see a man with such good taste."
    pro "I'm new here. Just trying to get my feel for the club, you know?"

    scene e007_020_060_spadesclub_intro_002 with dissolve
    hd007 "Yeah, good for you."
    pro "The girls around here are so hot."
    pro "Do you think any of them are hotter than my friend Marisa?"

    scene e007_020_061_spadesclub_intro_003 with dissolve
    hd007 "Huh? Are you asking me how hot the girls are here?"
    pro "Sure. There's plenty of hot babes in this place, right? Just wondering what the scenery is like."
    hd007 "Why don't you just look at the stage and see for yourself?"
    pro "That's the problem. There's so many of them."
    pro "I was supposed to meet a buddy of mine but I can't find him. He was supposed to tell me."

    scene e007_020_062_spadesclub_question_001 with dissolve
    hd007 "Yeah, well, I ain't your buddy, so I can't help you."
    pro "Maybe you can help me find my buddy then."
    pro "He's thinner. A little short. Kinda got a mark on his nose. Like a birthmark."
    pro "You seen anybody like that around here?"

    scene e007_020_063_spadesclub_question_002 with dissolve
    hd007 "What the fuck kinda question is that?"
    pro "I'm just looking for my friend."
    hd007 "Your friend doesn't have a cell phone?"
    pro "He turned it off. Didn't wanna be disturbed."

    scene e007_020_064_spadesclub_question_003 with dissolve
    hd007 "Why would your friend turn it off if he knows you're looking for him?"
    pro "He doesn't. It's a surprise, you know. I finally saved up enough money to get in here."
    pro "Maybe you can help me out."

    scene e007_020_065_spadesclub_dancer_001 with dissolve
    hd007 "This bitch is shaking her pretzels in front of my face and you want me to help you find your friend?"
    pro "Just wondering if you've seen him around."
    hd007 "I haven't seen anything except ass and titties."

    scene e007_020_066_spadesclub_dancer_002 with dissolve
    pro "Okay, okay. Sorry."
    pro "Make sure you watch my friend dance when she comes up. She's really hot."
    hd007 "Sure. Whatever."

    scene e007_020_067_spadesclub_meet_001 with dissolve
    mgm007 "You have a friend dancing tonight?"
    pro "It's her first night here. I think she's really hot. Hotter than any girl I've seen in here so far."
    mgm007 "That'll be interesting to see..."
    pro "You come here often?"

    scene e007_020_068_spadesclub_meet_002 with dissolve
    mgm007 "When I get the chance. There's no finer club in the city."
    mgm007 "If you want to find better-looking women, you would have to fly somewhere else."
    pro "I've seen some pretty good-looking girls at the Pink Rabbit."

    scene e007_020_069_spadesclub_meet_003 with dissolve
    mgm007 "The Pink Rabbit? Now I {i}know{/i} you're not from around here."
    pro "What's the difference? I think they're pretty hot over there."
    mgm007 "People come here for the women. But they stay for the atmosphere."
    pro "The atmosphere isn't much different from any club or bar I've been to."

    scene e007_020_070_spadesclub_clue_001 with dissolve
    mgm007 "It might seem that way but there's more to it than that."
    mgm007 "How did you get in here? You didn't pay a cover and walk in, did you?"
    pro "Like I said, I'm here with my friend who's dancing tonight."
    mgm007 "Exactly."

    scene e007_020_071_spadesclub_clue_002 with dissolve
    mgm007 "There's a certain exclusivity to this club."
    mgm007 "When people come here, they come here to get away."
    mgm007 "And if they come here to talk, it's to talk about business they don't want anybody else to hear."
    pro "It's a private club... I can see the appeal."

    scene e007_020_072_spadesclub_clue_003 with dissolve
    mgm007 "People don't come here just to talk to strangers."
    mgm007 "They're either here to talk business... or talk 'business.' Do you understand what I mean?"
    pro "(He seems friendly enough... That just makes him more suspicious though...)"
    pro "I think I understand..."
    pro "Why are you telling me this?"

    scene e007_020_073_spadesclub_warn_001 with dissolve
    mgm007 "Because I enjoy getting away. And I enjoy doing business that I want to be private."
    mgm007 "I only thought you should know they do everything they can to make sure business discussed here stays private."
    pro "They?"

    scene e007_020_074_spadesclub_warn_002 with dissolve
    mgm007 "Men like him."
    mgm007 "Security likes to give people the freedom they want but if they see anything suspicious, they'll look closer."
    pro "I see..."

    scene e007_020_075_spadesclub_warn_003 with dissolve
    pro "(I should probably stop asking questions and just look and see if there's anybody who fits the description.)"
    pro "...I'll keep that in mind."
    pro "Any other advice for this place?"

    scene e007_020_076_spadesclub_think_001 with dissolve
    mgm007 "Just enjoy yourself. Not everybody gets to get into a place like this every day."
    pro "*sigh* That's probably the best thing to do."

    scene black
    with fade
    pro "(I relax and enjoy the show for a bit. Everybody else does the same. Security starts to ignore me.)"
    pro "(I decide to talk to Erika to see if she found anything.)"

    scene e007_020_077_spadesclub_news_001 with dissolve
    pro "I talked to a few people but only some of them were able to give me vague possibilities."
    pro "Everybody else I talked to just didn't wanna talk."
    pro "How about you? You have any luck?"

    scene e007_020_078_spadesclub_news_002 with dissolve
    eri "Not much."
    eri "Just a bunch of guys making offers and girls trying to make some cash."
    pro "Shifty men and naked women."

    scene e007_020_079_spadesclub_news_003 with dissolve
    pro "It's probably best we stop asking so many questions."
    pro "The people will start to get suspicious about us looking for someone specific."
    pro "I just heard people come here to get away. Which probably shouldn't be a surprise to us."

    scene e007_020_080_spadesclub_news_004 with dissolve
    eri "Most people didn't wanna talk any real business. Guess we're too new for any of them to trust us."
    eri "Or maybe I was too obvious about looking for someone."
    pro "I was as subtle as I could be with all of the dancers. The guys at the stage didn't feel like talking."

    scene e007_020_081_spadesclub_news_005 with dissolve
    eri "I think there's a good chance the people here are just hiding something."
    eri "Maybe the guy who used the costume is stupid enough to get caught. But maybe there was a person who hired him to erase all the tracks leading to them."
    pro "Not to mention it could be more than one person. Do you know if all the fires in Old Town all happened at the exact same time?"

    scene e007_020_082_spadesclub_sus_001 with dissolve
    eri "I think so. It'd be the perfect way to tie up the fire department."
    eri "You'd have to be real scum to do something like this. I wouldn't put it past them to calculate it just right."
    pro "Guess the shop got lucky. Don't wanna think about how much worse it could've been if firefighters hadn't shown up so fast."

    scene e007_020_083_spadesclub_sus_002 with dissolve
    eri "I've been looking at all of the folks around here."
    eri "Nobody seems to fit Pete's description."
    pro "You think there's a chance he was off and misremembered?"
    eri "I think it's more likely that the guy's just hiding well. And anybody else involved must be hiding him, too."

    scene e007_020_084_spadesclub_rules_001 with dissolve
    eri "Rule Seven, Slick. Your business is everybody else's."
    pro "So I guess the rules of Old Town apply to Viridian, too."
    eri "It looks like that one does. Everybody in here is just better at hiding what they're up to."

    scene e007_020_085_spadesclub_rules_003 with dissolve
    eri "Look around. You can tell they're up to something just by looking at 'em."
    pro "Maybe they're all just horny and wanna blow their cash."
    eri "Guys with money do a lot more with it than spend it on sex, drugs and booze. They gotta enjoy the power that comes with it."
    pro "Rich and powerful. Looks like we're in a tough spot..."
    pro "...I think we should just wait. No sense in pushing things when we've got the whole night ahead of us. Maybe something will turn up."
    pro "Or maybe the guy we're looking for isn't even here."

    scene e007_020_086_spadesclub_wait_001 with dissolve
    eri "We can take this time to relax and enjoy ourselves. That'll help us make it less obvious we're here for other reasons."
    pro "I can go for that."
    eri "You must be getting tired of going to strip clubs all the time."

    menu:
        eri "Or it must be a pleasant coincidence for you that you always end up in places like this."

        "{kni_menu}I do what I need to do.{/kni_menu}":
            $ eri_knight +=1

            pro "I do what I need to do."
            pro "If I wanna learn about the people of this city, I need to meet all of them. Even the ones in places like this."

            scene e007_020_087_spadesclub_wait_002 with dissolve
            eri "I can see that. You always seem to have an open mind about everything."
            eri "Not everything has to be about work or business though. It's good to see you enjoy yourself when you can."
            pro "Balance is key. It's hard but doable."

        "{jok_menu}I'm going to space next.{/jok_menu}":
            $ eri_joker +=1

            pro "I'm going to space next."
            pro "There are some cool aliens I haven't met. Or fought. Or had sex with."

            scene e007_020_087_spadesclub_wait_002 with dissolve
            eri "Ha! I wouldn't put it past you to do all of those things."
            pro "I'm a man for the people. And the aliens."
            eri "Just be careful not to go starting something a human isn't capable of handling."
            pro "I know how to keep things balanced."

        "{smo_menu}These places just attract me.{/smo_menu}":
            $ eri_smooth +=1

            pro "These places just attract me."
            pro "It must be my natural magnetic attraction and rugged good looks. These places call to me and need my attention."

            scene e007_020_087_spadesclub_wait_002 with dissolve
            eri "With an ego like that, it's not a surprise."
            pro "You gotta call it like I see it."
            eri "Ha! Everybody has to see it your way, huh?"
            pro "My way is the only way. That's why you like me so much."
            eri "*laughing* I don't know about that..."
            pro "Don't judge me. It's a tough balancing act when you're pulled in every direction by so many people. Even for someone like me."

    scene e007_020_088_spadesclub_others_001 with dissolve
    stop backgroundmusic fadeout 4.0
    eri "Speaking of which, how are you balancing everything? In particular, how are you handling all of these ladies?"
    pro "This again, huh?"
    eri "It's a woman's natural curiosity."

    if erika_pursue_005 == True:
        eri "Besides, you have to expect a woman like me to keep nagging you about it. Especially when we have something special going on."
        pro "We do..."
        eri "Then there must be something special going on with someone else."
        eri "A manager needs to know these things. Gotta make sure you keep your head clear when you're going into a fight."
        pro "You're my partner. You're my manager."
        eri "I'm a lot more than that, too."
        eri "Go on now. Spill the beans."

    elif erika_pursue_005 == False:
        eri "The gossip is fun. But I need you to watch your back."
        eri "I'm your manager. Gotta make sure you go into those fights with a clear head."
        pro "You're my partner. You're my manager. You're an intergalactic space paladin."
        eri "Yep."
        eri "Go on now. Spill the beans."

    pro "There aren't any beans to spill."
    eri "C'mon, Slick. I'm your friend. If you can't tell me, who can you tell?"
    pro "There's nothing to tell."

    scene e007_020_089_spadesclub_others_002 with dissolve
    play backgroundmusic "audio/music/hangout_02.ogg" fadein 3.0
    eri "Are you serious? Every girl I met at the party was pretty. Even some of the regulars were pretty."
    pro "They're pretty. That doesn't mean anything."
    eri "All right. Just tell me this. Who's the prettiest?"
    pro "Huh?"
    eri "If you had to pick one, who do you think is the prettiest girl you know?"

    scene e007_020_090_spadesclub_others_003 with dissolve
    pro "That's a tough question."
    eri "Nobody's gonna kill you. We're just having fun here. It's not that serious."
    eri "You can be honest with me."
    default mode07_020 = False
    $ four_choice = True
    menu:
        pro "Well... If I had to be honest about who I think is the best looking..."
        "All":
            $ mode07_020 = True
            jump someoneyouknow
        "It's someone you know.":
            label someoneyouknow:
            $ four_choice = False
            pro "It's someone you know."
            eri "Interesting..."

            $ four_choice = True
            menu:
                eri "...Who is it?"
                "All":
                    $ four_choice = False
                    $ know_pretty_riley_007 = True

                    scene e007_020_091_spadesclub_others_004 with dissolve
                    pro "Riley."
                    pro "I guess I've always had a thing for her since high school."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "Riley's got everything going on. I bet a lot of guys are into her."
                    pro "She was the most popular girl back in high school. I wouldn't be surprised if it's the same in college."
                    eri "Redheads always have an advantage. She carries herself well, too."
                    pro "I don't know. Maybe it's because I've known her for so long. I don't think too much about it."

                    scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                    eri "You might have to. Something could happen between you two."
                    pro "I don't know. We're friends. We're working together on this. I don't know if it'll ever be something more than that."
                    eri "Try not to think too much about it. If you have a chance, you'll see your opportunity. Just gotta take it."
                    $ know_pretty_harlow_007 = True

                    scene e007_020_091_spadesclub_others_004 with dissolve
                    pro "Harlow."
                    pro "I think she's pretty in her own way."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "Harlow..."
                    pro "Wrong answer?"
                    eri "Of course not! Harlow's great!"
                    eri "For some reason she doesn't think she's as pretty as she is."
                    pro "I'm sure there are a lot of reasons for that. I wouldn't want to dig into that unless she wanted me to."

                    scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                    eri "Is there something going on between you two?"

                    if harlow_pursue_004 == True:
                        pro "I like her. I think she likes me, too."
                        eri "And did you do something back at my apartment?"

                        if harlow_invite_kiss_007 == True:
                            pro "C'mon..."

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "I knew it! Don't worry, Slick. I won't tell."
                            pro "Why do I tell you anything?"
                            eri "Because you can trust me, that's why."

                        elif harlow_invite_kiss_007 == False:
                            pro "I didn't invite her back. Didn't seem like now was the best time."

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "I guess it's been too soon since what happened. It seems like a good idea to give her some space."
                            pro "That's what I thought."
                            eri "Glad you told me."

                    elif harlow_pursue_004 == False:
                        pro "It's nothing like that. I look at her as a friend but nothing more."

                        scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                        eri "That's good. Doesn't mean you can't still be close even though it doesn't get romantic or sexual."
                        pro "That's right."
                    $ know_pretty_sophia_007 = True

                    scene e007_020_091_spadesclub_others_004 with dissolve
                    pro "Sophia."
                    pro "Something about her. Maybe it's the red hair."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "I think the red hair has something to do with it."
                    eri "The eyes, the body and the face have a lot to do with it, too."
                    pro "Now that you mention it, I guess I do like everything."

                    scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                    eri "She's pretty but I wonder what she thinks of you."
                    pro "In what way?"
                    eri "You have a pretty crazy life. Sophia's a sweet girl. A {i}regular{/i} girl. I wonder if she can handle you."
                    pro "I'm not looking into it that much. You just asked who I thought was the prettiest."
                    eri "I did. That's a good answer."
                    pro "Gee, {i}thanks{/i}."
                    scene e007_020_091_spadesclub_others_004 with dissolve
                    pro "Someone else not at the party."

                    menu:
                        eri "Who's that?"
                        "All":
                            $ know_pretty_marisa_007 = True

                            pro "Marisa."
                            pro "You obviously know her."

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "Oh, yeah. Marisa's hot."
                            eri "I almost feel sorry for her. She must deal with punks harassing her all the time."
                            pro "She seems to handle it well. She's good at keeping them at a distance."

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "That's the reason she likes you. You're not one of those regular creeps from Old Town."
                            pro "I think that's the reason a woman like her hasn't settled down yet."
                            eri "Not much to choose from. A girl as pretty as her should be in a better place than the Pink Rabbit."
                            pro "I get the sense she likes working there. She makes a great living."
                            eri "Well, she {i}is{/i} hot, so I can believe it."
                            $ know_pretty_jordan_007 = True

                            pro "Jordan."
                            pro "You remember her, right?"

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "The bartender?"
                            pro "That's right."
                            eri "Interesting..."
                            pro "Something wrong?"

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "Never pegged you as a guy who's into older women."
                            pro "I like what I see. Age is just a number to me."
                            eri "She doesn't look as old as someone who'd be working at a bar would look. Not the old hag you'd expect."
                            pro "She gets points for that."
                            eri "When you put it like that, I can see why guys would be really into her."
                            $ know_pretty_lorelei_007 = True

                            pro "Lorelei."
                            pro "I guess I'm crazy."

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "*chuckling* Are you serious?"
                            pro "Why not?"
                            eri "All right, Slick. You do know she wants to see you get your ass kicked, right?"
                            pro "I think I can get her to change her mind."
                            eri "Ha! Good luck with that."

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "Just make sure you don't let thinking about her get in the way of your fights."
                            pro "Hey, if a girl outside the cage was enough of a distraction to make me lose then I deserve to get my ass kicked."
                            eri "That's a good way of putting it. And if you lose because of that, {i}I'll{/i} kick your ass again right after."
                            pro "That's great motivation for me. I'm sure Lori will be impressed."
                            if mode07_020:
                                jump notsomeoneyoumet
                        "Marisa.":
                            $ know_pretty_marisa_007 = True

                            pro "Marisa."
                            pro "You obviously know her."

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "Oh, yeah. Marisa's hot."
                            eri "I almost feel sorry for her. She must deal with punks harassing her all the time."
                            pro "She seems to handle it well. She's good at keeping them at a distance."

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "That's the reason she likes you. You're not one of those regular creeps from Old Town."
                            pro "I think that's the reason a woman like her hasn't settled down yet."
                            eri "Not much to choose from. A girl as pretty as her should be in a better place than the Pink Rabbit."
                            pro "I get the sense she likes working there. She makes a great living."
                            eri "Well, she {i}is{/i} hot, so I can believe it."
                            if mode07_020:
                                jump notsomeoneyoumet
                        "Jordan.":
                            $ know_pretty_jordan_007 = True

                            pro "Jordan."
                            pro "You remember her, right?"

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "The bartender?"
                            pro "That's right."
                            eri "Interesting..."
                            pro "Something wrong?"

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "Never pegged you as a guy who's into older women."
                            pro "I like what I see. Age is just a number to me."
                            eri "She doesn't look as old as someone who'd be working at a bar would look. Not the old hag you'd expect."
                            pro "She gets points for that."
                            eri "When you put it like that, I can see why guys would be really into her."
                            if mode07_020:
                                jump notsomeoneyoumet
                        "Lorelei.":
                            $ know_pretty_lorelei_007 = True

                            pro "Lorelei."
                            pro "I guess I'm crazy."

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "*chuckling* Are you serious?"
                            pro "Why not?"
                            eri "All right, Slick. You do know she wants to see you get your ass kicked, right?"
                            pro "I think I can get her to change her mind."
                            eri "Ha! Good luck with that."

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "Just make sure you don't let thinking about her get in the way of your fights."
                            pro "Hey, if a girl outside the cage was enough of a distraction to make me lose then I deserve to get my ass kicked."
                            eri "That's a good way of putting it. And if you lose because of that, {i}I'll{/i} kick your ass again right after."
                            pro "That's great motivation for me. I'm sure Lori will be impressed."
                            if mode07_020:
                                jump notsomeoneyoumet
                        
                "Riley.":
                    $ four_choice = False
                    $ know_pretty_riley_007 = True

                    scene e007_020_091_spadesclub_others_004 with dissolve
                    pro "Riley."
                    pro "I guess I've always had a thing for her since high school."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "Riley's got everything going on. I bet a lot of guys are into her."
                    pro "She was the most popular girl back in high school. I wouldn't be surprised if it's the same in college."
                    eri "Redheads always have an advantage. She carries herself well, too."
                    pro "I don't know. Maybe it's because I've known her for so long. I don't think too much about it."

                    scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                    eri "You might have to. Something could happen between you two."
                    pro "I don't know. We're friends. We're working together on this. I don't know if it'll ever be something more than that."
                    eri "Try not to think too much about it. If you have a chance, you'll see your opportunity. Just gotta take it."
                    if mode07_020:
                        jump notsomeoneyoumet
                "Harlow.":
                    $ four_choice = False
                    $ know_pretty_harlow_007 = True

                    scene e007_020_091_spadesclub_others_004 with dissolve
                    pro "Harlow."
                    pro "I think she's pretty in her own way."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "Harlow..."
                    pro "Wrong answer?"
                    eri "Of course not! Harlow's great!"
                    eri "For some reason she doesn't think she's as pretty as she is."
                    pro "I'm sure there are a lot of reasons for that. I wouldn't want to dig into that unless she wanted me to."

                    scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                    eri "Is there something going on between you two?"

                    if harlow_pursue_004 == True:
                        pro "I like her. I think she likes me, too."
                        eri "And did you do something back at my apartment?"

                        if harlow_invite_kiss_007 == True:
                            pro "C'mon..."

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "I knew it! Don't worry, Slick. I won't tell."
                            pro "Why do I tell you anything?"
                            eri "Because you can trust me, that's why."

                        elif harlow_invite_kiss_007 == False:
                            pro "I didn't invite her back. Didn't seem like now was the best time."

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "I guess it's been too soon since what happened. It seems like a good idea to give her some space."
                            pro "That's what I thought."
                            eri "Glad you told me."

                    elif harlow_pursue_004 == False:
                        pro "It's nothing like that. I look at her as a friend but nothing more."

                        scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                        eri "That's good. Doesn't mean you can't still be close even though it doesn't get romantic or sexual."
                        pro "That's right."
                    if mode07_020:
                        jump notsomeoneyoumet
                "Sophia.":
                    $ four_choice = False
                    $ know_pretty_sophia_007 = True

                    scene e007_020_091_spadesclub_others_004 with dissolve
                    pro "Sophia."
                    pro "Something about her. Maybe it's the red hair."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "I think the red hair has something to do with it."
                    eri "The eyes, the body and the face have a lot to do with it, too."
                    pro "Now that you mention it, I guess I do like everything."

                    scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                    eri "She's pretty but I wonder what she thinks of you."
                    pro "In what way?"
                    eri "You have a pretty crazy life. Sophia's a sweet girl. A {i}regular{/i} girl. I wonder if she can handle you."
                    pro "I'm not looking into it that much. You just asked who I thought was the prettiest."
                    eri "I did. That's a good answer."
                    pro "Gee, {i}thanks{/i}."
                    if mode07_020:
                        jump notsomeoneyoumet
                "Someone else not at the party.":
                    $ four_choice = False

                    scene e007_020_091_spadesclub_others_004 with dissolve
                    pro "Someone else not at the party."

                    menu:
                        eri "Who's that?"

                        "Marisa.":
                            $ know_pretty_marisa_007 = True

                            pro "Marisa."
                            pro "You obviously know her."

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "Oh, yeah. Marisa's hot."
                            eri "I almost feel sorry for her. She must deal with punks harassing her all the time."
                            pro "She seems to handle it well. She's good at keeping them at a distance."

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "That's the reason she likes you. You're not one of those regular creeps from Old Town."
                            pro "I think that's the reason a woman like her hasn't settled down yet."
                            eri "Not much to choose from. A girl as pretty as her should be in a better place than the Pink Rabbit."
                            pro "I get the sense she likes working there. She makes a great living."
                            eri "Well, she {i}is{/i} hot, so I can believe it."
                            if mode07_020:
                                jump notsomeoneyoumet
                        "Jordan.":
                            $ know_pretty_jordan_007 = True

                            pro "Jordan."
                            pro "You remember her, right?"

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "The bartender?"
                            pro "That's right."
                            eri "Interesting..."
                            pro "Something wrong?"

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "Never pegged you as a guy who's into older women."
                            pro "I like what I see. Age is just a number to me."
                            eri "She doesn't look as old as someone who'd be working at a bar would look. Not the old hag you'd expect."
                            pro "She gets points for that."
                            eri "When you put it like that, I can see why guys would be really into her."
                            if mode07_020:
                                jump notsomeoneyoumet
                        "Lorelei.":
                            $ know_pretty_lorelei_007 = True

                            pro "Lorelei."
                            pro "I guess I'm crazy."

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "*chuckling* Are you serious?"
                            pro "Why not?"
                            eri "All right, Slick. You do know she wants to see you get your ass kicked, right?"
                            pro "I think I can get her to change her mind."
                            eri "Ha! Good luck with that."

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "Just make sure you don't let thinking about her get in the way of your fights."
                            pro "Hey, if a girl outside the cage was enough of a distraction to make me lose then I deserve to get my ass kicked."
                            eri "That's a good way of putting it. And if you lose because of that, {i}I'll{/i} kick your ass again right after."
                            pro "That's great motivation for me. I'm sure Lori will be impressed."
                            if mode07_020:
                                jump notsomeoneyoumet
                        "All":
                            $ know_pretty_marisa_007 = True

                            pro "Marisa."
                            pro "You obviously know her."

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "Oh, yeah. Marisa's hot."
                            eri "I almost feel sorry for her. She must deal with punks harassing her all the time."
                            pro "She seems to handle it well. She's good at keeping them at a distance."

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "That's the reason she likes you. You're not one of those regular creeps from Old Town."
                            pro "I think that's the reason a woman like her hasn't settled down yet."
                            eri "Not much to choose from. A girl as pretty as her should be in a better place than the Pink Rabbit."
                            pro "I get the sense she likes working there. She makes a great living."
                            eri "Well, she {i}is{/i} hot, so I can believe it."
                            $ know_pretty_jordan_007 = True

                            pro "Jordan."
                            pro "You remember her, right?"

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "The bartender?"
                            pro "That's right."
                            eri "Interesting..."
                            pro "Something wrong?"

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "Never pegged you as a guy who's into older women."
                            pro "I like what I see. Age is just a number to me."
                            eri "She doesn't look as old as someone who'd be working at a bar would look. Not the old hag you'd expect."
                            pro "She gets points for that."
                            eri "When you put it like that, I can see why guys would be really into her."
                            $ know_pretty_lorelei_007 = True

                            pro "Lorelei."
                            pro "I guess I'm crazy."

                            scene e007_020_092_spadesclub_fave_001 with dissolve
                            eri "*chuckling* Are you serious?"
                            pro "Why not?"
                            eri "All right, Slick. You do know she wants to see you get your ass kicked, right?"
                            pro "I think I can get her to change her mind."
                            eri "Ha! Good luck with that."

                            scene e007_020_093_spadesclub_fave_002_know_001 with dissolve
                            eri "Just make sure you don't let thinking about her get in the way of your fights."
                            pro "Hey, if a girl outside the cage was enough of a distraction to make me lose then I deserve to get my ass kicked."
                            eri "That's a good way of putting it. And if you lose because of that, {i}I'll{/i} kick your ass again right after."
                            pro "That's great motivation for me. I'm sure Lori will be impressed."
                            if mode07_020:
                                jump notsomeoneyoumet
        "It's not someone you've met.":
            label notsomeoneyoumet:
            $ four_choice = False

            scene e007_020_091_spadesclub_others_004 with dissolve
            pro "It's not someone you've met."
            eri "Interesting..."

            $ four_choice = True
            menu:
                eri "...What does she look like?"
                "(Describe All)":
                    $ four_choice = False
                    $ know_pretty_kate_007 = True

                    pro "Well, she's an older woman. Pretty face. Some curves."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "Older woman? Is that your thing, Slick?"
                    pro "Maybe. Maybe not. I just know that this one is pretty."
                    eri "I see. She must take care of herself if someone like you noticed her."
                    pro "I'm sure she gets plenty of attention."

                    scene e007_020_094_spadesclub_fave_003_unknown_001 with dissolve
                    eri "Anything going on there? Or do you just think she's pretty?"

                    if kate_pursue_007 == True:

                        pro "It's, uh... It's kinda complicated."
                        eri "Oh, geez. That's the last thing I wanna hear from someone who's fighting in a cage. Distractions can really screw you up."
                        pro "Don't worry. I'll be focused."
                        eri "You better be. I'll be damned if I see you lose a fight because your mind is somewhere else."
                        pro "When I'm in the cage my mind is there, too."

                    elif kate_pursue_007 == False:

                        pro "It's nothing like that. I just think she's attractive."
                        eri "I get ya. Sometimes you see someone and you just notice it."
                        pro "Yeah, that's it."
                    $ know_pretty_vanessa_007 = True

                    pro "She's hot. Blond model type. Long legs and a tight body."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "*laughing* Are you talking about a woman or cartoon character?"
                    pro "She's real. Though I haven't ever actually seen her face..."

                    scene e007_020_094_spadesclub_fave_003_unknown_001 with dissolve
                    eri "Huh? You've never seen her face?"
                    pro "Well, half of it anyway. She's always wearing these big aviators."
                    eri "You know, a lot of girls wear shades to hide their faces. You don't even know what she looks like."
                    eri "She could be missing an eye. Or maybe she's got an extra one."
                    pro "...Don't ruin this for me."
                    eri "*cackling* I'm sure she's just as pretty as you think she is."
                    pro "I think so. I can tell these things."
                    $ know_pretty_grace_007 = True

                    pro "She's older. Dark hair. Caramel complexion. Real mature."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "She sounds hot."
                    pro "I think so. She carries herself well, too. That goes a long way."
                    pro "I think it's because she has some modeling experience."

                    scene e007_020_094_spadesclub_fave_003_unknown_001 with dissolve
                    eri "If she's a model then she must be hot."
                    eri "Anything happening there?"

                    if grace_flirt_006 == True:

                        pro "It's too early to tell. Maybe."
                        eri "Well, if she's a model, good luck. They've got personalities."
                        pro "I think this one's mature enough to not be any trouble..."
                        eri "Famous last words."
                        pro "Don't do this to me."
                        eri "Ha!"

                    elif grace_flirt_006 == False:

                        pro "No. Just an observation I made."
                        eri "I see. Well, no shame in noticing a pretty girl when you see her."
                    $ know_pretty_stranger_007 = True

                    pro "She's thin. Dark hair. Kinda serious expression."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "Oh, really? Who is she?"
                    pro "I don't know."
                    eri "What do you mean 'you don't know'? Like, you don't know who she is?"
                    pro "No, I don't. I keep seeing her everywhere though. We saw her at the PGs that one night."

                    scene e007_020_094_spadesclub_fave_003_unknown_001 with dissolve
                    eri "Oh... I think I might have caught a glimpse of her."
                    eri "...Wait, you think the prettiest girl you know is someone you don't know? That doesn't count!"
                    pro "I've seen her multiple times. That counts."
                    eri "No, it doesn't."
                    pro "Yes, it does."
                    eri "No."
                    pro "Yes."
                    eri "*laughing* Lame."
                    if mode07_020:
                        jump ityou
                "(Describe Kate)":
                    $ four_choice = False
                    $ know_pretty_kate_007 = True

                    pro "Well, she's an older woman. Pretty face. Some curves."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "Older woman? Is that your thing, Slick?"
                    pro "Maybe. Maybe not. I just know that this one is pretty."
                    eri "I see. She must take care of herself if someone like you noticed her."
                    pro "I'm sure she gets plenty of attention."

                    scene e007_020_094_spadesclub_fave_003_unknown_001 with dissolve
                    eri "Anything going on there? Or do you just think she's pretty?"

                    if kate_pursue_007 == True:

                        pro "It's, uh... It's kinda complicated."
                        eri "Oh, geez. That's the last thing I wanna hear from someone who's fighting in a cage. Distractions can really screw you up."
                        pro "Don't worry. I'll be focused."
                        eri "You better be. I'll be damned if I see you lose a fight because your mind is somewhere else."
                        pro "When I'm in the cage my mind is there, too."

                    elif kate_pursue_007 == False:

                        pro "It's nothing like that. I just think she's attractive."
                        eri "I get ya. Sometimes you see someone and you just notice it."
                        pro "Yeah, that's it."
                    if mode07_020:
                        jump ityou
                "(Describe Vanessa)":
                    $ four_choice = False
                    $ know_pretty_vanessa_007 = True

                    pro "She's hot. Blond model type. Long legs and a tight body."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "*laughing* Are you talking about a woman or cartoon character?"
                    pro "She's real. Though I haven't ever actually seen her face..."

                    scene e007_020_094_spadesclub_fave_003_unknown_001 with dissolve
                    eri "Huh? You've never seen her face?"
                    pro "Well, half of it anyway. She's always wearing these big aviators."
                    eri "You know, a lot of girls wear shades to hide their faces. You don't even know what she looks like."
                    eri "She could be missing an eye. Or maybe she's got an extra one."
                    pro "...Don't ruin this for me."
                    eri "*cackling* I'm sure she's just as pretty as you think she is."
                    pro "I think so. I can tell these things."
                    if mode07_020:
                        jump ityou
                "(Describe Grace)":
                    $ four_choice = False
                    $ know_pretty_grace_007 = True

                    pro "She's older. Dark hair. Caramel complexion. Real mature."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "She sounds hot."
                    pro "I think so. She carries herself well, too. That goes a long way."
                    pro "I think it's because she has some modeling experience."

                    scene e007_020_094_spadesclub_fave_003_unknown_001 with dissolve
                    eri "If she's a model then she must be hot."
                    eri "Anything happening there?"

                    if grace_flirt_006 == True:

                        pro "It's too early to tell. Maybe."
                        eri "Well, if she's a model, good luck. They've got personalities."
                        pro "I think this one's mature enough to not be any trouble..."
                        eri "Famous last words."
                        pro "Don't do this to me."
                        eri "Ha!"

                    elif grace_flirt_006 == False:

                        pro "No. Just an observation I made."
                        eri "I see. Well, no shame in noticing a pretty girl when you see her."
                    if mode07_020:
                        jump ityou
                "(Describe the familiar-looking stranger)":
                    $ four_choice = False
                    $ know_pretty_stranger_007 = True

                    pro "She's thin. Dark hair. Kinda serious expression."

                    scene e007_020_092_spadesclub_fave_001 with dissolve
                    eri "Oh, really? Who is she?"
                    pro "I don't know."
                    eri "What do you mean 'you don't know'? Like, you don't know who she is?"
                    pro "No, I don't. I keep seeing her everywhere though. We saw her at the PGs that one night."

                    scene e007_020_094_spadesclub_fave_003_unknown_001 with dissolve
                    eri "Oh... I think I might have caught a glimpse of her."
                    eri "...Wait, you think the prettiest girl you know is someone you don't know? That doesn't count!"
                    pro "I've seen her multiple times. That counts."
                    eri "No, it doesn't."
                    pro "Yes, it does."
                    eri "No."
                    pro "Yes."
                    eri "*laughing* Lame."
                    if mode07_020:
                        jump ityou
        "It's you.":
            label ityou:
            $ four_choice = False
            $ know_pretty_erika_007 = True

            scene e007_020_091_spadesclub_others_004 with dissolve
            pro "It's you."
            pro "You're the prettiest girl I know, Erika."

            scene e007_020_092_spadesclub_fave_001 with dissolve
            eri "Pfft! Lame."
            pro "Huh?"
            eri "You're only saying that because I'm standing in front of you."
            pro "It's the truth."

            scene e007_020_095_spadesclub_fave_004_erika_001 with dissolve
            eri "You mean it, huh?"
            pro "Of course."

            if erika_pursue_005 == True:
                eri "I guess it's believable since you and I have our thing going on."
                pro "It's more than a thing. You know I like you. Your looks are part of it."
                eri "*sigh* Don't get mushy on me in a place like this."
                pro "It doesn't matter where we are. I like you. You're the prettiest girl to me."
                eri "Yeah... I guess you're pretty bonkers..."

            elif erika_pursue_005 == False:
                eri "Funny how you think I'm pretty but you don't seem... interested."
                pro "I just think it'd be for the best not to get involved. Things get complicated and..."
                eri "I get it. We have business to handle. That's what's important."
                pro "That's right."
            if mode07_020:
                jump itseverybody
        "It's everybody.":
            label itseverybody:
            $ four_choice = False
            $ know_pretty_everybody_007 = True

            scene e007_020_091_spadesclub_others_004 with dissolve
            pro "It's everybody."
            pro "I think every girl I know is just as pretty as the next. I like them all."

            scene e007_020_092_spadesclub_fave_001 with dissolve
            eri "That's not an answer."
            pro "Yes, it is. Every girl I know is pretty. It's a tie. That's my answer."
            pro "You can't blame me, can you?"

            scene e007_020_096_spadesclub_fave_005_everybody_001 with dissolve
            eri "I guess that's possible. Everybody I've met so far {i}is{/i} pretty."
            pro "See? So, everybody is tied for the prettiest."
            eri "You'd make a great politician... or the worst one."
            pro "I'm just calling it like I see it."
            eri "*laughing* Fine. You got me on that one."

    scene e007_020_097_spadesclub_fave_006 with dissolve
    eri "You just be careful, okay?"
    pro "What do you mean?"
    eri "You're surrounded by a lot of people. I know how guys think. They see a pretty girl and they just can't help themselves sometimes."
    eri "Thinking a girl is pretty is one thing. Pursuing her is another."
    pro "I agree with that."

    scene e007_020_098_spadesclub_warn_001 with dissolve
    eri "You might get involved with a girl. Maybe another one."
    eri "They're all gonna find out eventually. You have to be honest with them if you care about them."
    eri "But then what happens?"
    pro "I don't know if I wanna hear this..."

    scene e007_020_099_spadesclub_warn_002 with dissolve
    eri "Worlds collide. Massive destruction. Damage on every scale."
    pro "Being a little dramatic, aren't we?"
    eri "People are dramatic. We all get emotional. Some easier than others."
    pro "That's what separates us from the animals."
    eri "Exactly. Sometimes there are things you can't explain beyond your feelings."
    pro "What do you think I should do?"

    scene e007_020_100_spadesclub_handleit_001 with dissolve
    stop backgroundmusic fadeout 4.0
    eri "I think you should do what you wanna do. If you a feel a certain way of doing things is right then things will work out in the end."
    pro "But..."
    eri "But I don't think it'll be easy. Chasing multiple women... It's not normal."
    eri "Feelings always complicate things. They get the best of us. It's hard to control them all the time."
    pro "I'll keep that in mind."

    if erika_pursue_005 == True:

        scene e007_020_101_spadesclub_jealous_001 with dissolve
        pro "All this talk about other girls..."
        pro "Feels weird to talk about. Especially when we..."
        pro "I guess you're cool with it. Or..."

        scene e007_020_102_spadesclub_jealous_002 with dissolve
        eri "If you think I'm gonna be your madam and start lining up girls for you, don't even think about it."
        eri "I'll get a fight for you. Not another girl."
        pro "That's a reasonable response. But... what about other girls?"
        eri "What about them?"
        pro "Well... Do you get jealous?"
        eri "*sigh* I guess I'll put it to you this way..."

        scene e007_020_103_spadesclub_jealous_003 with dissolve
        eri "You're my friend. We're business partners. We have something that's more than just physical."
        eri "I don't wanna throw away what we have. I can't imagine things changing between us. Not over something like {i}that{/i}."
        pro "That's one way of looking at it."
        eri "But... It's... It's complicated. There's a longer answer somewhere in there."
        eri "I'm having a good time right now. I don't wanna think about it. I can't say how I'll feel when I just don't know."
        pro "I guess we'll just cross that bridge when we get there. {i}If{/i} we get there."
        eri "*sigh* Just be honest, Slick. That's all I want more than anything else."
        eri "That's what {i}every{/i} girl wants. Even if they don't realize it. It's what's best for everybody."
        pro "I think I understand."

    scene e007_020_104_spadesclub_watch_001 with dissolve
    play backgroundmusic "audio/music/club_003.ogg" fadein 3.0
    eri "Marisa just took the stage. That's a good-looking woman."
    pro "Guess we should watch her dance."
    eri "*laughing* You say that like it's a bad thing."

    scene e007_020_105_spadesclub_watch_002 with dissolve
    eri "She's so hot. The moment I first saw her I thought she was one of the hottest girls I'd ever seen."
    eri "Her face. Her ass. Her tits. Her body. She's the total package."
    pro "She's something all right. She's pretty talented, too."

    scene e007_020_106_spadesclub_watch_003 with dissolve
    eri "She's more than just her looks. That's years of experience up there."
    eri "It's hypnotizing the way she moves. I wish I could move like that."

    if erika_pursue_005 == True:
        pro "I wouldn't mind seeing that."
        eri "Maybe I'll ask her for a lesson."
        pro "*chuckling* Maybe you should."

    elif erika_pursue_005 == False:
        pro "That'd be... interesting."
        eri "C'mon, Slick. You don't think I could work the pole?"
        pro "You could try but..."
        eri "*laughing* Fuck you."
        pro "*chuckling* All right. Let's see it happen then."

    scene e007_020_107_spadesclub_watch_004 with dissolve
    eri "Marisa's got something else though. I can't put my finger on it exactly."
    pro "Maybe it's her confidence."
    eri "I think that's it. The way she moves around that pole... She just owns it."

    scene e007_020_108_spadesclub_watch_005 with dissolve
    pro "She's getting a lot of attention now. Not bad for a girl who makes her living in Old Town."
    eri "A girl like her deserves better than the westside."
    pro "From what she told me, she likes it there. It's where she's comfortable."

    scene e007_020_109_spadesclub_enjoy_001 with dissolve
    eri "I guess..."
    eri "I just hope she's happy doing whatever it is she's doing."
    pro "Mesmerized, huh?"
    eri "She just looks so beautiful up there..."
    eri "You stop thinking about how a lot of people would shame her and you just look at the art of it instead."

    scene e007_020_110_spadesclub_enjoy_002 with dissolve
    eri "Tonight's not such a bad night."
    eri "I got to hang out with you. I get to see a pretty girl on stage. I got to dress up and do my makeup."

    menu:
        eri "I should try to look on the bright side."

        "{kni_menu}You should {i}always{/i} look on the bright side.{/kni_menu}":
            $ eri_knight +=1

            pro "You should {i}always{/i} look on the bright side."
            pro "Especially when times are down."

            scene e007_020_111_spadesclub_enjoy_003 with dissolve
            eri "Always putting such a positive spin on things."
            pro "That's the best way to look at things. Not a bad way to start the weekend."
            eri "Got to go somewhere new. Can't be too mad at that."

        "{jok_menu}And if that doesn't work, you can drink.{/jok_menu}":
            $ eri_joker +=1

            pro "And if that doesn't work, you can drink."

            scene e007_020_111_spadesclub_enjoy_003 with dissolve
            eri "Careful. I might do that."
            pro "What if I'm not joking?"
            eri "You know I have a penchant for whiskey."
            pro "Maybe it's a whiskey night tonight."
            eri "Ha! Maybe it is."

        "{smo_menu}You're with me. That's reason enough.{/smo_menu}":
            $ eri_smooth +=1

            pro "You're with me. That's reason enough."

            scene e007_020_111_spadesclub_enjoy_003 with dissolve
            eri "I can say the same thing about you."
            pro "Yeah, I'm pretty grateful I get to spend the night with myself."
            eri "*laughing* I bet that's something you always do."

            if erika_pursue_005 == True:
                pro "Not tonight. I'm staying at your place, remember?"
                eri "Maybe I changed my mind."
                pro "Then I'll have to change it."
                eri "I'd like to see you try."
                pro "I bet you would..."

            elif erika_pursue_005 == False:
                pro "I like to kick'em out when I'm done."
                eri "Ha! What an asshole."
                pro "That's what they like, baby."
                eri "*laughing* Whatever."

    if erika_pursue_005 == True:

        scene e007_020_112_spadesclub_enjoy_004_pursue_001 with dissolve
        pro "It {i}is{/i} a special night for me though."
        eri "Yeah? How's that?"
        pro "I get to see a hot girl dance on stage while I watch with my girl."
        eri "{i}Your{/i} girl, huh?"

        scene e007_020_113_spadesclub_kiss_001_pursue_002 with dissolve
        eri "I don't know if I like you being so possessive."
        pro "I have to be."
        pro "All these guys in this club... You in this hot dress..."
        pro "You look great tonight, Erika. Can't help myself."
        eri "Well... When you put it like that..."
        eri "I'm pretty bonkers about you, too, Slick."

        scene e007_020_114_spadesclub_kiss_002_pursue_003 with dissolve
        $renpy.sound.play("audio/sounds/universal/kiss_03.ogg")
        eri "Mmm..."

        scene e007_020_115_spadesclub_relax_001_pursue_004 with dissolve
        pro "This is nice. Just relaxing and enjoying the show. Just us."
        eri "Almost feels like we're alone even in a room full of people."
        pro "We should do this more often. Maybe I'll take you somewhere nicer next time."
        eri "Anywhere is fine with me."

    scene e007_020_116_spadesclub_relax_002 with dissolve
    pro "How about we chill out and enjoy the rest of Marisa's show? We can toss a few bills her way for the full experience."
    eri "Sounds like fun. I'll get us a couple of drinks. Maybe some booze will make tonight more enjoyable."
    pro "I think it will. I'll see if I can find us a couple of seats next to the stage."

    scene e007_020_117_spadesclub_bump_001 with dissolve
    pro "(Something about this stage makes Marisa look different. Maybe it's the lighting...)"
    pro "(Either way, she looks great up there.)"
    pro "(No two seats together though... Don't wanna sit next to that guy I was hounding.)"
    pro "(He's been sitting there all night. Guys around here sure got a lot of money to—)"
    voi "Hey!"

    scene e007_020_118_spadesclub_bump_002 with dissolve
    stg007 "What the fuck are you doin', asshole?"
    pro "Oh, sorry. I'm just looking—"
    stg007 "You're standing in the middle of the fuckin' aisle."
    pro "I said sorry—"

    scene e007_020_119_spadesclub_bump_003 with dissolve
    stg007 "Stop standin' there like a dumbass."
    stg007 "I got this hot babe with me and I'm gonna have some fun."
    pro "All right. I'll move out of the way. Geez."

    scene e007_020_120_spadesclub_notice_001 with dissolve
    stg007 "I don't know how a chump like you got into this club but you need to learn some respect. Show some fuckin' manners."
    stg007 "If I didn't have respect for this club, I'd teach you a lesson right here."
    stg007 "Lucky for you I got business to take care of."
    pro "Yeah—"
    pro "(Probably shouldn't make a scene in front of security. I should—)"
    pro "(Wait a second.)"

    scene e007_020_121_spadesclub_notice_002 with dissolve
    pro "(His voice is a little whiny...)"
    pro "(He's thin... short...)"
    pro "(He's got that make on his nose.)"
    pro "(I think...)"
    stg007 "You listenin' to me, punk?"
    pro "(Better play it cool.)"

    scene e007_020_122_spadesclub_warn_001 with dissolve
    pro "Sorry, man. Didn't mean anything by it."
    stg007 "Just don't let it happen again."
    pro "Sure. No problem."

    scene e007_020_123_spadesclub_warn_002 with dissolve
    pro "(Maybe I can follow him back there.)"
    pro "(There's a chance I can overhear what he's talking about. I might get some of the information we've been looking for.)"

    scene e007_020_124_spadesclub_warn_003 with dissolve
    csg007 "What are you doing?"
    pro "I just wanted to go into the backroom and—"
    csg007 "Private dance area only. You're not allowed to go back there without a dancer."
    pro "Right..."

    scene e007_020_125_spadesclub_spot_001 with dissolve
    pro "Hey, Erika."
    eri "Ready to have that drink—"
    pro "I think I saw him. The guy we're looking for."
    eri "Huh? Are you sure?"
    pro "I'm pretty sure it was him. Short. Thin. Mark on his nose."

    scene e007_020_126_spadesclub_spot_002 with dissolve
    eri "Whiny voice?"
    pro "Yeah... He was acting like he's never seen me before."
    eri "Of course. He wouldn't give away that he was at the party."
    pro "He's in the back. Can't go there without a dancer."

    scene e007_020_127_spadesclub_idea_001 with dissolve
    eri "We have to get back there. He might spill some information when he thinks nobody's paying attention."
    pro "That's what I was thinking."
    pro "I'd go back there with Marisa's but she's on stage."
    eri "Then we'll just have to find someone else."

    scene e007_020_128_spadesclub_idea_002 with dissolve
    eri "Let's split up. I'll look for a girl and you do the same."
    eri "Get back there as soon as you can. Follow that guy. Maybe you'll overhear something."
    pro "Okay. Just remember to play it cool. We don't have to do anything tonight. We're just looking for clues."
    eri "Got it."

    scene e007_020_129_spadesclub_search_001 with dissolve
    pro "(Erika's looking for a dancer who's available.)"
    pro "(Looks like everybody is occupied.)"

    scene e007_020_130_spadesclub_search_002 with dissolve
    pro "(Maybe I should just wait for Marisa to finish.)"
    pro "(It's not like I can confront the guy back there. I doubt he'd be spilling secrets to some stripper even if he were responsible for what happened.)"
    pro "(There's a chance though...)"
    pro "(Gotta stay cool. Can't make it obvious...)"

    scene e007_020_131_spadesclub_search_003 with dissolve
    wvoi "Hey."
    pro "Huh?"

    scene e007_020_132_spadesclub_invite_001 with dissolve
    stra "Haven't seen you around here before. You must be new?"
    pro "Hey..."
    pro "(It's her. Again.)"
    pro "(It feels like I've run into this girl a million times...)"
    pro "(Still acting like she's never met me before... Better not mention it right now.)"

    scene e007_020_133_spadesclub_invite_002 with dissolve
    stra "Are you okay?"
    pro "I'm fine. Just fine."
    stra "I was wondering if you wanted to go back there for a private dance."
    stra "We get to be alone. It's a lot of fun. What do you say?"
    pro "(Looks like this is my best chance to get back there.)"

    scene e007_020_134_spadesclub_invite_003 with dissolve
    stra "It's $500 for fifteen minutes."
    pro "(Five hundred...)"
    pro "What exactly do I get for that?"
    stra "Looks like you'll have to go back there to find out."
    pro "(Don't have much of a choice.)"

    scene e007_020_135_spadesclub_invite_004 with dissolve
    stra "Don't worry. You can pay me after you're done."
    pro "You trust me?"
    stra "If you try getting away without paying..."
    pro "Security. I get it."
    stra "Right this way."

    scene e007_020_136_spadesclub_invite_005 with dissolve
    stra "You'll like it once we're away from the floor. It's a lot more private back there."
    pro "Hmm... This should be interesting."

    stop backgroundmusic fadeout 1.0
    window hide

    jump episode07_021_strip_club_private_room

#define config.label_overrides["episode15_009_date_confession"] = "episode15_009_date_confession_modded"#???

label episode15_009_date_confession_modded:

    scene e015_009_001_talk_game_001 with fade
    play backgroundmusic "audio/music/walk_001.ogg"
    pro "That was fun. Unexpected. But fun."
    ril "Definitely."

    scene e015_009_002_talk_game_002 with dissolve
    ril "You know, you're pretty good. I think you would've made the team if you played in high school."
    pro "Basketball's fun. If I took it seriously though, it'd probably affect my grades."
    pro "I don't know how you managed to play varsity with so many things that could distract you."

    scene e015_009_003_talk_game_003 with dissolve
    ril "I remember at the time how tough it was. My schedule was always full."
    ril "Somehow I managed. Looking back, I put in a lot more time than I realized then."
    pro "If anybody could do it, Riley Fox is the one."

    scene e015_009_004_talk_plan_001 with dissolve
    ril "Do you have anything else planned for tonight?"
    pro "Still not satisfied, huh?"

    scene e015_009_005_talk_plan_002 with dissolve
    ril "Not at all. It was a great night regardless of what happened."
    ril "I just enjoyed getting to hang out with you and not talk about... {w}what we usually talk about."
    pro "I feel the same."

    scene e015_009_006_talk_need_001 with dissolve
    ril "I thought... I thought it was such a silly idea. Dressing up like we were going to a high school dance."
    ril "But I've never been more relaxed than I am now. Just being able to forget about all of my obligations and be young again."
    pro "*laughing* You're still young."

    scene e015_009_007_talk_need_002 with dissolve
    ril "Not as young as I used to be. And with all of these adult reponsibilities."
    ril "*sigh* After tonight, I think I'm recharged. I can get back to it better than before."
    pro "It's the end of the night, so I guess I can ask about it now. How's the internship?"

    scene e015_009_008_talk_intern_001 with dissolve
    ril "Aw, we almost went the whole night without getting serious."
    pro "Whoops. I can take it back—"
    ril "*laughing* It's all right."

    scene e015_009_009_talk_intern_002 with dissolve
    ril "Everything's fine. I get all my work done."
    ril "Billy's is doing great, so I have a model business to look at. I'm on track to graduate."
    pro "That's good to hear. Even though it's not that surprising."

    scene e015_009_010_talk_thesis_001 with dissolve
    ril "How about you? How is your thesis coming along?"
    pro "It's coming along as well as it could."
    pro "I've got plenty of data. I should have an early first draft soon."

    scene e015_009_011_talk_thesis_002 with dissolve
    ril "As expected from you. I'm so happy for you."
    ril "It seems so daunting to put together a thesis but you seem passionate and focused about it."
    pro "I am. It's been that way since high school."

    scene e015_009_012_talk_why_001 with dissolve
    stop backgroundmusic fadeout 3.0
    ril "...[mc]... {w}Can I ask you something?"
    pro "Of course."
    ril "Do you know why you went into psychology?"
    ril "Most people don't figure out what they're going to do in high school."

    scene e015_009_013_talk_why_002 with dissolve
    pro "..."
    pro "My dad. I wanted to do it for him."

    scene e015_009_014_talk_why_003 with dissolve
    pro "I saw how he was... {w}after mom died."
    pro "The way he started acting... It was different."

    scene e015_009_015_talk_why_004 with dissolve
    pro "I always looked up to him. He's the strongest person I've ever known."
    pro "To see him so vulnerable... I wanted to do something for him but I couldn't do anything."
    pro "I didn't know what to do. I felt so helpless."
    pro "That's when I decided I wanted to be there for him in the best way I could."
    pro "I figured psychology would help me at least understand what he was going through."
    ril "[mc]... I'm sorry that happened..."

    scene e015_009_016_talk_mom_001 with dissolve
    pro "It all happened so suddenly."
    pro "One day she's there and the next..."

    scene e015_009_017_talk_mom_002 with dissolve
    pro "..."
    ril "..."

    scene e015_009_018_talk_mom_003 with dissolve
    ril "I heard talk about something like that happening at school. You know how gossip spreads."
    ril "I didn't think much about it. Probably because I just didn't want to think about it."
    ril "I can't believe it was you they were talking about."

    scene e015_009_019_talk_mom_004 with dissolve
    ril "[mc], I'm sorry that happened to you. I can't imagine what it's like."
    ril "If you ever want to talk about it, you know I'm here."
    pro "Thanks. It's nice knowing that you care."
    pro "My dad and I have both gotten a lot of support over the years. We're... okay."

    scene e015_009_020_talk_okay_001 with dissolve
    ril "The way you talk about your dad. I think you're just as strong as he is."
    ril "You're doing well for yourself. You've accomplished so much."
    pro "I couldn't have done it without friends like you."

    scene e015_009_021_talk_okay_002 with dissolve
    ril "That means a lot to me. But I know you would find a way somehow if you had to do it alone."
    ril "You're a good person more than anything else. I've seen what you've done."
    ril "I think your mother would be proud of the man you've become."
    pro "I'd like to think so, too."

    scene e015_009_022_talk_silent_001 with dissolve
    ril "..."

    scene e015_009_023_talk_silent_002 with dissolve
    pro "..."

    scene e015_009_024_talk_silent_003 with dissolve
    ril "..."
    pro "..."

    scene e015_009_025_talk_confess_001 with dissolve
    pro "I have to tell you something. It's not something small."
    pro "I... I've kind of been keeping it from a lot of people. But I know I can trust you."

    scene e015_009_026_talk_confess_002 with dissolve
    ril "Of course. What is it?"
    pro "...I've been fighting in Old Town."
    ril "Fighting? I... I don't understand."
    pro "I mean literally fighting."

    scene e015_009_027_talk_confess_003 with dissolve
    pro "In Old Town, there are these illegal underground fights."
    pro "I've been fighting in them."
    ril "What? Why?"

    scene e015_009_028_talk_fight_001 with dissolve
    pro "It was back when Billy was struggling with the coffee shop. I needed to figure out a way to make some money."
    pro "Erika and I made a deal. She would help get me fights and we would split the money."
    pro "It's not just Erika. I made a deal with Saul, too."
    pro "It's the reason he was willing to take care of me and get me my own apartment."

    scene e015_009_029_talk_fight_002 with dissolve
    ril "Is that why—"
    pro "No. It has nothing to do with the coffee shop. He invested in Billy because of Billy, not because of any side deal I made with him."
    ril "Then why would he make that deal? What does he get out of helping you with... fighting?"
    pro "I don't know exactly. I figure if he's helping Billy, I could trust him."
    pro "This is just another deal I made with him. Separately."
    ril "I see..."
    ril "You're not joking, are you?"
    pro "No. Not about something like this."

    scene e015_009_030_talk_quit_001 with dissolve
    ril "This is... {w}a lot for me to take in. It almost sounds like you're making it up."
    pro "I'm not."
    pro "But I'm done. I'm going to tell Erika and Saul that I'm not fighting again."
    ril "What about the deal you made?"
    pro "I'll figure it out. I know they'll understand."
    ril "..."

    scene e015_009_031_talk_now_001 with dissolve
    ril "Why are you telling me this now?"
    pro "Because I want to be completely honest with you. About everything."
    pro "I want you to know the whole truth about me... to trust me like I trust you."
    pro "There's no reason for me to fight anymore. I'm not going to take that risk when I no longer have to."

    scene e015_009_032_talk_great_001 with dissolve
    ril "Are you sure everything is all right?"
    pro "It is now. After everything that's happened and spending tonight with you."
    pro "Talking to all of the people around town... Seeing everything the city has to offer..."
    pro "I see now more than ever how good life has been to me."
    pro "I have everything I could ever need and want. Why take the risk of losing it?"
    pro "I just want to enjoy it now with the people closest to me."

    if riley_dance_date_010 == True:

        pro "Especially you..."

    ril "Right..."

    scene e015_009_033_talk_quiet_001 with dissolve
    ril "..."

    scene e015_009_034_talk_quiet_002 with dissolve
    ril "..."

    scene e015_009_035_talk_weird_001 with dissolve
    play backgroundmusic "audio/music/confession_002.ogg" fadein 3.0
    ril "It's a strange feeling... {w}having someone be open and honest with you."

    scene e015_009_036_talk_weird_002 with dissolve
    ril "To have someone you can call a friend... {w}To not be alone."
    ril "I..."

    scene e015_009_037_talk_alone_001 with dissolve
    ril "...I used to go to parties all the time."
    ril "In high school. In college. Everybody would always invite me."
    ril "'She's the class president. She's so smart. She's so popular. She has to be there.'"

    scene e015_009_038_talk_alone_002 with dissolve
    ril "I'd always feel welcome. The girls would always talk to me and share all of the gossip with me."
    ril "The boys would be nice to me and tell me everything about themselves."
    ril "And they'd listen to me. I'd talk about school and they'd act so interested."

    scene e015_009_039_talk_alone_003 with dissolve
    ril "None of them ever talked to me without some other motive though."
    ril "It didn't matter. Boys and girls all the same."
    ril "The girls just wanted to use me to get attention from guys."
    ril "And the guys... {w}The guys just wanted to... {w}fuck me."

    scene e015_009_037_talk_alone_001 with dissolve
    ril "The last party I was at was full of people."
    ril "Imagine. Surrounded by a bunch of people vying for your attention..."
    ril "I was at the center of it..."

    scene e015_009_040_talk_alone_004 with dissolve
    ril "...And I'd never felt so alone."
    ril "..."

    scene e015_009_041_talk_alone_005 with dissolve
    ril "I was always at those parties. There were {i}so many{/i} people there."
    ril "All of them wanting to talk to me."

    scene e015_009_042_talk_alone_006 with dissolve
    ril "Everybody wanting something from me. And when they didn't get it, they stopped talking to me and disappeared."
    ril "It was like that since high school. And it didn't stop in college."

    scene e015_009_043_talk_alone_007 with dissolve
    ril "There were times I didn't feel like a real person. I was just... there."
    ril "Someone they could get something from and when I didn't have what they wanted, I didn't exist."

    scene e015_009_044_talk_friend_001 with dissolve
    ril "You're different though."

    if ril_knight >= ril_joker and ril_knight >= ril_smooth:

        ril "You're the kindest person I've ever met."
        ril "You say everything with consideration."
        ril "You're not like most guys our age."
        ril "You talk to me like you're not just trying to get something from me."

    elif ril_joker > ril_knight and ril_joker >= ril_smooth:

        ril "You always try to make me laugh."
        ril "Whenever I talk to you, you just say what's on your mind. You're not like anybody else."
        ril "It doesn't matter what kind of mood I'm in, I can't help but smile when we hang out."
        ril "I forget about everything and can just be myself and laugh with you."

    elif ril_smooth > ril_knight and ril_smooth > ril_joker:

        ril "You don't try to hide anything."
        ril "Most guys want something from me but they deny it to make me think there's something more."
        ril "You put it out there. You're honest and that makes me smile."
        ril "You don't say something because you think it's what I want to hear. You just say how you feel."

    ril "{i}You{/i} make me feel like a real person."
    ril "I never had any friends. Not any real friends."

    scene e015_009_045_talk_friend_002 with dissolve
    ril "But I know you. You're the first real friend I've ever had."
    ril "I don't know why you'd want to be my friend. But you are."
    pro "I know why..."

    scene e015_009_046_talk_honest_001 with dissolve
    ril "The first time we met Saul and I danced with him, he told me to be careful. Not to mix business with... something more."
    ril "And for the longest time, I remembered that because of all of the other men who only wanted one thing from me."
    ril "I feel like you're different though."
    ril "I just..."

    #ANIMATION
    scene anim_e015_010_001_riley_choice_001 with dissolve
    ril "...I don't know why you would still want to be my friend when no other guy has before."

    $ four_choice = True
    menu:
        ril "Just be honest, [mc]... That's all I want..."

        "Pursue Riley but keep other relationships active":
            $ four_choice = False
            $ riley_pursue_015 = True

            #$ erika_romance_solo = False
            #$ harlow_romance_solo = False
            #$ kate_romance_solo = False
            #$ vanessa_romance_solo = False

            #$ marisa_romance_solo = False
            #$ jordan_romance_solo = False
            #$ sophia_romance_solo = False

            #$ lorelei_romance_solo = False
            #$ grace_romance_solo = False
            #$ stranger_romance_solo = False

            #PURSUE
            scene e015_009_057_talk_more_001 with dissolve
            pro "It was always more than your looks."
            pro "The first time I saw you back in high school, I knew there was something special about you."
            pro "I can't explain it. I just felt it."

            scene e015_009_058_talk_more_002 with dissolve
            pro "And after getting to know you, I know now that my feeling was right."
            pro "I know that there's more to you than what every other guy sees."
            pro "I didn't see just a pretty girl. I didn't see someone I wanted to screw."

            scene e015_009_059_talk_more_003 with dissolve
            pro "You're smart. You're hard-working. You're focused and driven."
            pro "You're as determined as anybody I've ever met. I've never seen you fail at anything."
            pro "But you're sweet, too. I know you want to help and not just because you get something out of it."

            scene e015_009_060_talk_more_004 with dissolve
            pro "I know you first started helping Billy for school but now I know it's more than that."
            pro "You're kind and considerate."
            pro "I know the real you and not the popular girl everybody else sees."

            scene e015_009_061_talk_more_005 with dissolve
            pro "I had a thing for you in high school because I liked you. All of you."
            pro "I don't know if a guy has ever told you that but that's how I feel."
            pro "I don't know if that makes me different. It's just the truth."

            jump episode15_009_date_confession_part_two_pursue

        "Maybe I did just want to sleep with you. (Pursue Riley)":
            $ four_choice = False
            $ riley_pursue_015 = True

            $ erika_romance_solo = False
            $ harlow_romance_solo = False
            $ kate_romance_solo = False
            $ vanessa_romance_solo = False

            $ marisa_romance_solo = False
            $ jordan_romance_solo = False
            $ sophia_romance_solo = False

            $ lorelei_romance_solo = False
            $ grace_romance_solo = False
            $ stranger_romance_solo = False

            #PURSUE
            scene e015_009_057_talk_more_001 with dissolve
            pro "Maybe I did just want to sleep with you."
            pro "The first time I saw you, you were the most beautiful girl I'd ever seen."
            pro "And I still think you're beautiful."

            scene e015_009_058_talk_more_002 with dissolve
            pro "But talking to you and spending time with you... {w}Actually getting to know you..."
            pro "I know now that you're more than just a pretty face."

            scene e015_009_059_talk_more_003 with dissolve
            pro "You're smart. You're hard-working. You're focused and driven."
            pro "You're as determined as anybody I've ever met. I've never seen you fail at anything."
            pro "But you're sweet, too. I know you want to help and not just because you get something out of it."

            scene e015_009_060_talk_more_004 with dissolve
            pro "I know you first started helping Billy for school but now I know it's more than that."
            pro "You're kind and considerate."
            pro "You're just as beautiful on the inside as you are on the outside."

            scene e015_009_061_talk_more_005 with dissolve
            pro "So... I'll say it... At one point, I did just want to hook up with you."
            pro "I guess that doesn't make me different from most guys in that."
            pro "But that's not why I'm here now. Now I want to be around you for the person you are, not what I first saw."
            pro "Even if it means all we'll ever be is just friends."

            jump episode15_009_date_confession_part_two_pursue

        "It was always more than your looks. (Pursue Riley)":
            $ four_choice = False
            $ riley_pursue_015 = True

            $ erika_romance_solo = False
            $ harlow_romance_solo = False
            $ kate_romance_solo = False
            $ vanessa_romance_solo = False

            $ marisa_romance_solo = False
            $ jordan_romance_solo = False
            $ sophia_romance_solo = False

            $ lorelei_romance_solo = False
            $ grace_romance_solo = False
            $ stranger_romance_solo = False

            #PURSUE
            scene e015_009_057_talk_more_001 with dissolve
            pro "It was always more than your looks."
            pro "The first time I saw you back in high school, I knew there was something special about you."
            pro "I can't explain it. I just felt it."

            scene e015_009_058_talk_more_002 with dissolve
            pro "And after getting to know you, I know now that my feeling was right."
            pro "I know that there's more to you than what every other guy sees."
            pro "I didn't see just a pretty girl. I didn't see someone I wanted to screw."

            scene e015_009_059_talk_more_003 with dissolve
            pro "You're smart. You're hard-working. You're focused and driven."
            pro "You're as determined as anybody I've ever met. I've never seen you fail at anything."
            pro "But you're sweet, too. I know you want to help and not just because you get something out of it."

            scene e015_009_060_talk_more_004 with dissolve
            pro "I know you first started helping Billy for school but now I know it's more than that."
            pro "You're kind and considerate."
            pro "I know the real you and not the popular girl everybody else sees."

            scene e015_009_061_talk_more_005 with dissolve
            pro "I had a thing for you in high school because I liked you. All of you."
            pro "I don't know if a guy has ever told you that but that's how I feel."
            pro "I don't know if that makes me different. It's just the truth."

            jump episode15_009_date_confession_part_two_pursue

        "I always had a thing for you. (Don't Pursue Riley)":
            $ four_choice = False

            #DON'T PURSUE
            scene e015_009_057_talk_more_001 with dissolve
            pro "I always had a thing for you."
            pro "When I first saw you in high school, I thought you were the prettiest girl I'd ever seen in my life."
            pro "I imagined how great it would be to your boyfriend... {w}to have the prettiest girl in school on my arm would have been everything."

            scene e015_009_058_talk_more_002 with dissolve
            pro "But after getting to know you, I see that there's more to you."
            pro "You're smart. You're hard-working. You're focused and driven."

            scene e015_009_059_talk_more_003 with dissolve
            pro "You're as determined as anybody I've ever met. I've never seen you fail at anything."
            pro "But you're sweet, too. I know you want to help and not just because you get something out of it."

            scene e015_009_060_talk_more_004 with dissolve
            pro "Maybe I did want to hook up with you way back in high school. But now..."

            scene e015_009_047_talk_pal_001 with dissolve
            pro "...Now nothing would make me happier than just being your friend."
            pro "That's what matters to me."

            scene e015_009_048_talk_pal_002 with dissolve
            pro "That's the truth. All of it."
            ril "Yeah..."

            jump episode15_009_date_confession_part_three_nopursue

        "It was never about {i}that{/i} for me. (Don't Pursue Riley)":
            $ four_choice = False

            #DON'T PURSUE
            scene e015_009_057_talk_more_001 with dissolve
            pro "It was never about {i}that{/i} for me."
            pro "I didn't care that everybody else thought you were the hottest girl at the school."

            scene e015_009_058_talk_more_002 with dissolve
            pro "It didn't matter to me that every guy wanted to sleep with you."
            pro "There was just something about you. Something special."

            scene e015_009_059_talk_more_003 with dissolve
            pro "And after getting to know you, I realize just how right I was even back then."
            pro "You're smart. You're hard-working. You're focused and driven."

            scene e015_009_060_talk_more_004 with dissolve
            pro "You're as determined as anybody I've ever met. I've never seen you fail at anything."
            pro "But you're sweet, too. I know you want to help and not just because you get something out of it."

            scene e015_009_047_talk_pal_001 with dissolve
            pro "In high school, I just wanted a chance... to know you. To see if I was right that there was more to you."
            pro "I wanted to see if there was something more than what everybody else saw."
            pro "Nothing makes me happier knowing I {i}was{/i} right."

            scene e015_009_048_talk_pal_002 with dissolve
            pro "Even if I were {i}just{/i} your friend, that's everything I could ever want."
            ril "Right..."

            jump episode15_009_date_confession_part_three_nopursue
