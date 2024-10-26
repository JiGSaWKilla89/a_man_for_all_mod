default persistent._good_choice_color = "#0F0"
default persistent._default_good_choice_color = "#0F0"

default persistent._bad_choice_color = "#F00"
default persistent._default_bad_choice_color = "#F00"

default persistent._recommended_choice_color = "#FF0"
default persistent._default_recommended_choice_color = "#FF0"

default persistent._best_choice_color = "#00F"
default persistent._default_best_choice_color = "#00F"

default persistent._dealers_choice_color = "#F0F"
default persistent._default_dealers_choice_color = "#F0F"


init 1000 python:
    """
    Within this script is all the functions necessary to list, 
    extract and compare files.
    The main function here is the walthrough_dict' that returns the walkthrough data
    """
    import os

    use_archive_format = True

    def menu_hack(line):
        global met_seo_official
        if line == (u'scripts/episode008/e08_002.rpyc', 400):
            met_seo_official = True

    
    def walkthrough_dict():
        green = persistent._good_choice_color
        blue = persistent._best_choice_color
        yellow = persistent._recommended_choice_color
        red = persistent._bad_choice_color
        pink = persistent._dealers_choice_color

        _dech = " {color=[persistent._dealers_choice_color]}Dealers Choice{/color}"
        _goch = " {color=[persistent._good_choice_color]}Good Choice{/color}"
        _bach = " {color=[persistent._bad_choice_color]}Bad Choice{/color}"
        _recc = " {color=[persistent._recommended_choice_color]}Recommended{/color}"
        _bech = " {color=[persistent._best_choice_color]}Best Choice{/color}"

        return {
            (u'scripts/episode001/e01_002.rpyc', 160) : {
                "(Sneak a peek at her cleavage.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [],
                    "color" : blue
                    },
                },
            (u'scripts/episode001/e01_008.rpyc', 140) : {
                "(I'm sure she won't mind.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [],
                    "color" : yellow
                    },
                },
            (u'scripts/episode001/e01_011.rpyc', 174) : {
                "Let me show you how good a kisser I am." : {
                    "wt" : "{}".format(_recc),
                    "hint" : [
                        "Leads to kissing Erika",
                        "erica_kiss_001 = True",
                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode001/e01_012.rpyc', 80) : {
                "I'm willing if you are." : {
                    "wt" : "{}".format(_recc),
                    "hint" : [
                        "Leads to a Blowjob from Erika",
                        "erika_bj_001 = True"
                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode001/e01_016.rpyc', 71) : {
                "I've always... admired you." : {
                    "wt" : "{}".format(_recc),
                    "hint" : [
                        "Confession to Riley",
                        "confess_riley_001 = True"
                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode002/e02_001.rpyc', 416) : {
                "(Check her butt out)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [

                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode002/e02_009.rpyc', 98) : {
                "We're friends but this is for a school project." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Riley is a Friend",
                        "riley_friend_002 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode002/e02_010.rpyc', 64) : {
                "She's still as pretty as I remember her." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Riley is you Crush",
                        "riley_crush_002 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode002/e02_013.rpyc', 145) : {
                "I'll do this for you... to see you win." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Wants to win for Vanessa",
                        "vanessa_word_002 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode002/e02_015.rpyc', 308) : {
                "I won't let Erika down." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Fight For Erika",
                        "erika_fight_for_002 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode002/e02_016.rpyc', 367) : {
                "(Take a peek at her ass.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [

                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode002/e02_016.rpyc', 452) : {
                "(Check her out.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [

                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode002/e02_017.rpyc', 263) : {
                "Yeah... I wanna fuck you. (Sex)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Marissa Private Sex",
                        "marisa_private_sex_002 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode003/e03_003.rpyc', 154) : {
                "I'm fighting for Erika." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Fighting for Erika",
                        "jack_fight_erika_003 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode003/e03_003.rpyc', 314) : {
                "How about a kiss goodbye?" : {
                    "wt" : "{}".format(_bech if eri_smooth >= 1 else ''),
                    "hint" : [
                        "Required Erika Smooth >= 1" if eri_smooth >= 1 else "",
                        ],
                    "color" : blue if eri_smooth >= 1 else None
                    },
                },
            (u'scripts/episode003/e03_007.rpyc', 134) : {
                "For a pretty woman like you, I don't see why not." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Tell Jordan she is pretty",
                        "jordan_pretty_003 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode003/e03_009.rpyc', 125) : {
                "(Photobomb!)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [],
                    "color" : blue
                    },
                },
            (u'scripts/episode003/e03_010.rpyc', 205) : {
                "A little hard work for a pretty woman" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Do a little bit of work for jordan",
                        "jordan_for_her_003 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode003/e03_011.rpyc', 229) : {
                "(Comfort her)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Comfort Kate",
                        "comfort_kate_meeting_003 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode003/e03_012.rpyc', 456) : {
                "She's attractive..." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Told Billy Kate is Attractive",
                        "billy_kate_pretty_003 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode003/e03_015.rpyc', 120) : {
                "(Pull her in for a kiss.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Kiss Erika at Proving Grounds",
                        "erika_kiss_pgs_003 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode003/e03_018.rpyc', 97) : {
                "Take it off. (Keep going)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Take Jordan's bra off",
                        "jordan_shirt_off_003 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode003/e03_018.rpyc', 135) : {
                "I like Riley." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Tell Jordan you like Riley",
                        "jordan_tell_riley_003 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode003/e03_018.rpyc', 266) : {
                "Yeah... Yeah, I can do that. (Sex)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Fuck Jordan how she wants to be fucked",
                        "jordan_sex_accept_003 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode003/e03_018.rpyc', 416) : {
                "Spread your legs." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Tell Jordan To Spread Her Legs"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode004/e04_004.rpyc', 51) : {
                "I do like her..." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Told Bruno you like Vanessa",
                        "like_vanessa_bruno_004 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode004/e04_007.rpyc', 87) : {
                "Hey, Sophia..." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Chat Sophia up",
                        "sophia_goodbye_004 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode004/e04_007.rpyc', 289) : {
                "(Caress her hand.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Caress Kate's hand",
                        "caress_hand_kate_004 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode004/e04_013.rpyc', 339) : {
                "Sure, I'll do it." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Leads to another menu"
                        ],
                    "color" : pink
                    },
                "Sounds like a bad idea." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Leads to another menu"
                        ],
                    "color" : pink
                    },
                },
            (u'scripts/episode004/e04_013.rpyc', 363) : {
                "You. (Sex with Marisa)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Have sex with Marisa",
                        "marisa_sex_deal_004 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode004/e04_013.rpyc', 455) : {
                "I'm gonna fuck you. (Sex with Marisa)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Have sex with Marisa",
                        "marisa_sex_deal_004 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode004/e04_015.rpyc', 29) : {
                "(Fool around with Erika.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Fool around with Erika",
                        "erika_fool_around_004 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode004/e04_017.rpyc', 711) : {
                "(Dance with Vanessa.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [
                        "Leads to another menu"
                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode004/e04_017.rpyc', 749) : {
                "(Check her out.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode004/e04_017.rpyc', 991) : {
                "(Put a hand on her shoulder.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode004/e04_019.rpyc', 209) : {
                "I could see it, sure. (Pursue Harlow)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Pursue Harlow",
                        "harlow_pursue_004 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode004/e04_019.rpyc', 428) : {
                "(Go in for a kiss.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Kiss Harlow at Viridian",
                        "kiss_harlow_viridian_004 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode004/e04_019.rpyc', 625) : {
                "(Take a peek at her ass.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode004/e04_020.rpyc', 140) : {
                "(69 with Marisa.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode005/e05_006.rpyc', 396) : {
                "(Dance close to Vanessa.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode005/e05_007.rpyc', 413) : {
                "I want to be there for you." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                            "Be There for Kate",
                            "kate_be_there_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode005/e05_007.rpyc', 634) : {
                "(Give her a hug.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                            "Hug Kate",
                            "kate_hug_diner_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode005/e05_007.rpyc', 714) : {
                "(Take a closer look at her.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode005/e05_009.rpyc', 276) : {
                "(Get close to her and console her.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Console Erika",
                        "erika_console_bar_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode005/e05_009.rpyc', 441) : {
                "(Pull her in for a kiss.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Pull Erika in for a Kiss",
                        "erika_kiss_midtown_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode005/e05_010.rpyc', 190) : {
                "By the way, nice top. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Flirt with Sophia",
                        "sophia_flirt_coffee_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode005/e05_011.rpyc', 458) : {
                "(Enjoy the show and have some fun with Harlow.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Finger Harlow in the Pink Rabbit",
                        "harlow_pinkrabbit_finger_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode005/e05_014.rpyc', 48) : {
                "I'm trying to impress her and everybody else." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Try to impress Vanessa",
                        "billy_impress_vanessa_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode005/e05_015.rpyc', 883) : {
                "For you." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Doing it for Vanessa",
                        "vanessa_for_her_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode005/e05_015.rpyc', 927) : {
                "(Go in for a kiss.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Kiss Vanessa",
                        "vanessa_kiss_club_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode005/e05_016.rpyc', 52) : {
                "(Send her a dick pic.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [
                        
                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode005/e05_017.rpyc', 200) : {
                "(Pull her in for a kiss.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Pull Marisa in for a Kiss",
                        "marisa_kiss_viridian_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode005/e05_019.rpyc', 380) : {
                "I want to be with you wherever you go. (Pursue Erika)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Pursue Erika",
                        "erika_pursue_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode005/e05_019.rpyc', 478) : {
                "I want to be with you wherever you go. (Pursue Erika)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Pursue Erika",
                        "erika_pursue_005 = True"
                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode005/e05_020.rpyc', 64) : {
                "I'm up for something. (Have some fun with Erika)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Have some fun with Erika",
                        "erika_sex_oldtown_005 = True"
                        ],
                    "color" : yellow
                    },
                },
            
            (u'scripts/episode005/e05_025.rpyc', 130) : {
                "(Compliment her.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Compliment Stranger",
                        "stranger_compliment_005 = True"
                        ],
                    "color" : blue
                    },
                },  
            (u'game/mod/overwrites.rpy', 660) : {
                "(Compliment her.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Compliment Stranger",
                        "stranger_compliment_005 = True"
                        ],
                    "color" : blue
                    },
                },  
                      
            (u'scripts/episode005/e05_025.rpyc', 551) : {
                "I'm expecting you to take me somewhere special. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Riley Date Bet",
                        "riley_viridian_date_bet_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'game/mod/overwrites.rpy', 1081) : {
                "I'm expecting you to take me somewhere special. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Riley Date Bet",
                        "riley_viridian_date_bet_005 = True"
                        ],
                    "color" : blue
                    },
                },

            (u'scripts/episode005/e05_025.rpyc', 1468) : {
                "How about we just watch everybody dance? (Friendly)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                "How about we forget about all this and dance? (Flirt)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                },
            (u'game/mod/overwrites.rpy', 1998) : {
                "Both" : {
                    "wt" : "{}".format(_dech+_recc),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                "How about we just watch everybody dance? (Friendly)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                "How about we forget about all this and dance? (Flirt)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                },
            
            (u'scripts/episode005/e05_025.rpyc', 1533) : {
                "I hope she and I get closer." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Told Kate you Like Riley",
                        "kate_like_riley_005 = True"
                        ],
                    "color" : pink
                    },
                },
            (u'game/mod/overwrites.rpy', 2062) : {
                "I hope she and I get closer." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Told Kate you Like Riley",
                        "kate_like_riley_005 = True"
                        ],
                    "color" : pink
                    },
                },

            (u'scripts/episode005/e05_025.rpyc', 1657) : {
                "(Take a peek down her shirt.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [
                        
                        ],
                    "color" : yellow
                    },
                },
            (u'game/mod/overwrites.rpy', 2183) : {
                "(Take a peek down her shirt.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [
                        
                        ],
                    "color" : yellow
                    },
                },

            (u'scripts/episode005/e05_025.rpyc', 1733) : {
                "I'm sure you'll like it more if you move closer." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Dance Closer to Kate",
                        "kate_dance_close_005 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'game/mod/overwrites.rpy', 2259) : {
                "I'm sure you'll like it more if you move closer." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Dance Closer to Kate",
                        "kate_dance_close_005 = True"
                        ],
                    "color" : blue
                    },
                },

            (u'scripts/episode006/e06_003.rpyc', 197) : {
                "I want you to be there. (Take things further with Kate.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Kiss Kate",
                        "kate_flirt_kiss_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_005.rpyc', 109) : {
                "(Kiss her.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Kiss Harlow in the Hallway",
                        "harlow_hallway_kiss_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_007.rpyc', 237) : {
                "I like her." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Tell Grace you like Vanessa",
                        "vanessa_grace_like_006 = True"
                        ],
                    "color" : pink
                    },
                "I like her. I want to fuck her." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Tell Grace you like Vanessa and want to fuck her",
                        "vanessa_grace_like_006 = True"
                        ],
                    "color" : pink
                    },
                },
            (u'scripts/episode006/e06_007.rpyc', 310) : {
                "You're a good-looking woman, Grace. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Flirt with Grace",
                        "grace_flirt_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_008.rpyc', 307) : {
                "(Have her feed one to you.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Feed Riley a Fry",
                        "riley_feed_fry_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_008.rpyc', 537) : {
                "Okay, it's for me. (Flirt)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode006/e06_009.rpyc', 218) : {
                "And am I somewhere in that future with you? (Flirt)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode006/e06_009.rpyc', 280) : {
                "Maybe I'll do more than say hello. (Flirt)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode006/e06_010.rpyc', 49) : {
                "(Hook-up with Marisa.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Have Late Night sex with Marisa",
                        "marisa_sex_latenight_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_011.rpyc', 111) : {
                "(Go down on her.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode006/e06_011.rpyc', 458) : {
                "All right." : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode006/e06_012.rpyc', 115) : {
                "I'm sure you'll look pretty in any outfit. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Tell Sophia she will look pretty in any outfit",
                        "sophia_pretty_costume_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_013.rpyc', 1116) : {
                "(Make Lori jealous by kissing Erika.) (Flirt with Lori)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Make Lori Jealous",
                        "lorelei_flirt_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_013.rpyc', 1176) : {
                "I'll see you around, babe. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Flirt with Lori",
                        "lorelei_flirt_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_016.rpyc', 54) : {
                "But you like a guy with a wild side. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Flirt with Jordan",
                        "jordan_flirt_first_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_016.rpyc', 299) : {
                "Both. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Flirt with Jordan",
                        "jordan_flirt_second_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_016.rpyc', 396) : {
                "(Have sex with Jordan.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Have sex With Jordan",
                        "jordan_sex_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_017.rpyc', 275) : {
                "I like you a lot, Jordan." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Tell Jordan you like her",
                        "jordan_like_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_018.rpyc', 563) : {
                "I'm sure he's fine. (Flirt)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode006/e06_018.rpyc', 636) : {
                "You can stay here a little longer. (Flirt)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode006/e06_018.rpyc', 722) : {
                "I'm not done with you yet. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Promise Marisa",
                        "marisa_promise_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_018.rpyc', 830) : {
                "I think it looks great on you. (Flirt)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode006/e06_019.rpyc', 1168) : {
                "(Grab her ass.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [
                        
                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode006/e06_019.rpyc', 1226) : {
                "I think you look great tonight. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Sophia Flirt",
                        "sophia_flirt_photo_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_019.rpyc', 1265) : {
                "A few years. (Flirt)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode006/e06_020.rpyc', 364) : {
                "I want to take a picture with you. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Take a selfie with Vanessa",
                        "vanessa_selfie_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_020.rpyc', 403) : {
                "(Pull Vanessa close.) (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Flirt with Vanessa",
                        "vanessa_flirt_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_020.rpyc', 442) : {
                "(Look down her shirt.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode006/e06_021.rpyc', 729) : {
                "How about a hug? (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Hug Sophia",
                        "sophia_hug_goodbye_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_021.rpyc', 959) : {
                "I might have a thing for her." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Admit to Erika you like Riley",
                        "erika_admit_riley_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_021.rpyc', 1031) : {
                "I might have a thing for her." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Admit to Erika you like Riley",
                        "erika_admit_riley_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_021.rpyc', 1149) : {
                "(Have some fun with Harlow.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Have Sex with Harlow",
                        "harlow_sex_coffeeshop_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode006/e06_021.rpyc', 1423) : {
                "Maybe we can add a little more to it. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Riley Handshake Flirt",
                        "riley_flirt_handshake_006 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_006.rpyc', 151) : {
                "Uh... Sure..." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Costume Shopping with Erika",
                        "erika_costumes_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_006.rpyc', 178) : {
                "You." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Erika Maid Costume",
                        "erika_maid_costume_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_008.rpyc', 561) : {
                "I think I want some 'dessert.' (Flirt)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode007/e07_010.rpyc', 42) : {
                "(Have sex with Erika)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Have Sex with Erika",
                        "erika_sex_ever_000 = True",
                        "erika_apartment_sex_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_010.rpyc', 78) : {
                "(Have some fun with Erika)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Have fun with Erika",
                        "erika_sex_ever_000 = True",
                        "erika_apartment_sex_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_010.rpyc', 115) : {
                "(Fuck Erika)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Fuck Erika",
                        "erika_sex_ever_000 = True",
                        "erika_apartment_sex_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_011.rpyc', 54) : {
                "Well... Only because you insist." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Gawk at Vanessa in her Bikini",
                        "vanessa_bikini_gawk_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_011.rpyc', 295) : {
                "(Offer to put some sunscreen on her) (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Put Sunscreen on Vanessa",
                        "vanessa_sunscreen_flirt_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_011.rpyc', 394) : {
                "I need to take a picture of you for myself." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Take Photo of Vanessa",
                        "vanessa_photo_selfie_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_011.rpyc', 423) : {
                "(Offer to put some sunscreen on) (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Offer to Put Sunscreen on Vanessa",
                        "vanessa_sunscreen_flirt_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_011.rpyc', 577) : {
                "We need to take a sexier pic. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Take a Sexier Pic",
                        "vanessa_duo_shirtless_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_011.rpyc', 675) : {
                "(Offer to put some sunscreen on her) (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Offer to Put Sunscreen on Vanessa",
                        "vanessa_sunscreen_flirt_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_014.rpyc', 631) : {
                "I wanna stay longer with you. (Fool around with Harlow)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Fool around with Harlow",
                        "harlow_sex_ever_000 = True",
                        "harlow_invite_kiss_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_014.rpyc', 825) : {
                "I need a kiss goodbye. (Fool around with Harlow)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Fool around with Harlow",
                        "harlow_sex_ever_000 = True",
                        "harlow_invite_kiss_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode007/e07_017.rpyc', 309) : {
                "Yes...  It's important... (Potentially Pursue Kate)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Potentially Pursue Kate",
                        "kate_flirt_007 = True"
                        ],
                    "color" : blue
                    },
                },
            
            (u'scripts/episode007/e07_017.rpyc', 390) : {
                "I know I can make things work. (Pursue Kate)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Disables all other relationships",
                        "kate_sex_ever_000 = True",
                        "kate_office_sex_007 = True",
                        "kate_pursue_007 = True",
                        "erika_romance_solo = False",
                        "harlow_romance_solo = False",
                        "riley_romance_solo = False",
                        "vanessa_romance_solo = False",
                        "marisa_romance_solo = False",
                        "jordan_romance_solo = False",
                        "sophia_romance_solo = False",
                        "lorelei_romance_solo = False",
                        "grace_romance_solo = False",
                        "stranger_romance_solo = False",
                        ],
                    "color" : blue
                    },
                "I can't help myself. (Pursue Kate)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Disables all other relationships",
                        "kate_sex_ever_000 = True",
                        "kate_office_sex_007 = True",
                        "kate_pursue_007 = True",
                        "erika_romance_solo = False",
                        "harlow_romance_solo = False",
                        "riley_romance_solo = False",
                        "vanessa_romance_solo = False",
                        "marisa_romance_solo = False",
                        "jordan_romance_solo = False",
                        "sophia_romance_solo = False",
                        "lorelei_romance_solo = False",
                        "grace_romance_solo = False",
                        "stranger_romance_solo = False",
                        ],
                    "color" : blue
                    },
                "Maybe denying ourselves is right. (Don't pursue Kate)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Do not Pursue Kate",
                        "kate_office_pursue_decline_007 = True"
                        ],
                    "color" : blue
                    },
                "I guess I'm not thinking straight. (Don't pursue Kate)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Do not Pursue Kate",
                        "kate_office_pursue_decline_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'game/mod/overwrites.rpy', 387) : {
                "Pursue Kate while still pursuing others" : {
                    "wt" : "{}".format(_dech+_recc),
                    "hint" : [
                        "Pursue Kate", 
                        "kate_office_sex_007 = True",
                        "Kate Office Sex",
                        "kate_pursue_007 = True",
                        "kate_sex_ever_000 = True"
                        ],
                    "color" : pink
                    },
                "I know I can make things work. (Pursue Kate)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Disables all other relationships",
                        "kate_sex_ever_000 = True",
                        "kate_office_sex_007 = True",
                        "kate_pursue_007 = True",
                        "erika_romance_solo = False",
                        "harlow_romance_solo = False",
                        "riley_romance_solo = False",
                        "vanessa_romance_solo = False",
                        "marisa_romance_solo = False",
                        "jordan_romance_solo = False",
                        "sophia_romance_solo = False",
                        "lorelei_romance_solo = False",
                        "grace_romance_solo = False",
                        "stranger_romance_solo = False",
                        ],
                    "color" : pink
                    },
                "I can't help myself. (Pursue Kate)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Disables all other relationships",
                        "kate_sex_ever_000 = True",
                        "kate_office_sex_007 = True",
                        "kate_pursue_007 = True",
                        "erika_romance_solo = False",
                        "harlow_romance_solo = False",
                        "riley_romance_solo = False",
                        "vanessa_romance_solo = False",
                        "marisa_romance_solo = False",
                        "jordan_romance_solo = False",
                        "sophia_romance_solo = False",
                        "lorelei_romance_solo = False",
                        "grace_romance_solo = False",
                        "stranger_romance_solo = False",
                        ],
                    "color" : pink
                    },
                "Maybe denying ourselves is right. (Don't pursue Kate)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Do not Pursue Kate",
                        "kate_office_pursue_decline_007 = True"
                        ],
                    "color" : pink
                    },
                "I guess I'm not thinking straight. (Don't pursue Kate)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Do not Pursue Kate",
                        "kate_office_pursue_decline_007 = True"
                        ],
                    "color" : pink
                    },
                },
            
            (u'scripts/episode007/e07_018.rpyc', 271) : {
                "(Ask Riley out on a date) (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Asked Riley On A Date",
                        "riley_ask_date_007 = True"
                        ],
                    "color" : blue
                    },
                },
            
            (u'scripts/episode007/e07_020.rpyc', 246) : {
                "(Something cool.)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Cool Stripper Name",
                        "stripper_cool_name_007 = True"
                        ],
                    "color" : pink
                    },
                "(Be honest.)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Real Stripper Name",
                        "stripper_real_name_007 = True"
                        ],
                    "color" : pink
                    },
                },
            (u'game/mod/overwrites.rpy', 2946) : {
                "(Something cool.)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Cool Stripper Name",
                        "stripper_cool_name_007 = True"
                        ],
                    "color" : pink
                    },
                "(Be honest.)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Real Stripper Name",
                        "stripper_real_name_007 = True"
                        ],
                    "color" : pink
                    },
                },
            
            (u'scripts/episode007/e07_020.rpyc', 693) : {
                "It's someone you know." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                "It's not someone you've met." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                "It's you." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_erika_007 = True"
                        ],
                    "color" : pink
                    },
                "It's everybody." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_everybody_007 = True"
                        ],
                    "color" : pink
                    },
                },
            (u'game/mod/overwrites.rpy', 3393) : {
                "All" : {
                    "wt" : "{}".format(_dech+_recc),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                "It's someone you know." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                "It's not someone you've met." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                "It's you." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_erika_007 = True"
                        ],
                    "color" : pink
                    },
                "It's everybody." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_everybody_007 = True"
                        ],
                    "color" : pink
                    },
                },
           
            (u'scripts/episode007/e07_020.rpyc', 702) : {
                "Riley." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_riley_007 = True"
                        ],
                    "color" : pink
                    },
                "Harlow." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_harlow_007 = True"
                        ],
                    "color" : pink
                    },
                "Sophia." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_sophia_007 = True"
                        ],
                    "color" : pink
                    },
                "Someone else not at the party." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                },
            (u'game/mod/overwrites.rpy', 3405) : {
                "All" : {
                    "wt" : "{}".format(_dech+_recc),
                    "hint" : [
                        "know_pretty_riley_007 = True",
                        "know_pretty_harlow_007 = True",
                        "know_pretty_sophia_007 = True",

                        ],
                    "color" : pink
                    },
                "Riley." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_riley_007 = True"
                        ],
                    "color" : pink
                    },
                "Harlow." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_harlow_007 = True"
                        ],
                    "color" : pink
                    },
                "Sophia." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_sophia_007 = True"
                        ],
                    "color" : pink
                    },
                "Someone else not at the party." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                },

            (u'scripts/episode007/e07_020.rpyc', 796) : {
                "Marisa." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_marisa_007 = True"
                        ],
                    "color" : pink
                    },
                "Jordan." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_jordan_007 = True"
                        ],
                    "color" : pink
                    },
                "Lorelei." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_lorelei_007 = True"
                        ],
                    "color" : pink
                    },
                },
            (u'game/mod/overwrites.rpy', 3488) : {
                "All" : {
                    "wt" : "{}".format(_dech+_recc),
                    "hint" : [
                        "know_pretty_marisa_007 = True",
                        "know_pretty_jordan_007 = True",
                        "know_pretty_lorelei_007 = True"
                        ],
                    "color" : pink
                    },
                "Marisa." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_marisa_007 = True"
                        ],
                    "color" : pink
                    },
                "Jordan." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_jordan_007 = True"
                        ],
                    "color" : pink
                    },
                "Lorelei." : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_lorelei_007 = True"
                        ],
                    "color" : pink
                    },
                },

            (u'scripts/episode007/e07_020.rpyc', 863) : {
                "(Describe Kate)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "know_pretty_kate_007 = True"
                        ],
                    "color" : blue
                    },
                "(Describe Vanessa)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "know_pretty_vanessa_007 = True"
                        ],
                    "color" : blue
                    },
                "(Describe Grace)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "know_pretty_grace_007 = True"
                        ],
                    "color" : blue
                    },
                "(Describe the familiar-looking stranger)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [

                        ],
                    "color" : blue
                    },
                },
            (u'game/mod/overwrites.rpy', 3821) : {
                "(Describe All)" : {
                    "wt" : "{}".format(_dech+_recc),
                    "hint" : [
                        "know_pretty_kate_007 = True",
                        "know_pretty_vanessa_007 = True",
                        "know_pretty_grace_007 = True",
                        "know_pretty_stranger_007 = True"
                        ],
                    "color" : pink
                    },
                "(Describe Kate)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_kate_007 = True"
                        ],
                    "color" : pink
                    },
                "(Describe Vanessa)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_vanessa_007 = True"
                        ],
                    "color" : pink
                    },
                "(Describe Grace)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_grace_007 = True"
                        ],
                    "color" : pink
                    },
                "(Describe the familiar-looking stranger)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "know_pretty_stranger_007 = True"
                        ],
                    "color" : pink
                    },
                },
            
            (u'scripts/episode007/e07_021.rpyc', 65) : {
                "(Enjoy the dance) (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Enjoy The Dance",
                        "dance_flirt_stranger_007 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode008/e08_002.rpyc', 400) : {
                "We should get to know each other better. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "str_flirt_point +=1"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode008/e08_003.rpyc', 221) : {
                "You really care about me. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "str_flirt_point +=1"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode008/e08_009.rpyc', 165) : {
                "I might be..." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "mar_flirt_point +=1"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode008/e08_009.rpyc', 336) : {
                "(Have a threesome with Jordan and Marisa.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "marisa_sex_ever_000 = True",
                        "jordan_sex_ever_000 = True",
                        "Have a Threesome",
                        "jordan_marisa_threesome_sex_bar_008 = True",
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode008/e08_009.rpyc', 436) : {
                "(Have some fun with Jordan.) (Sex)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Sex With Jordan",
                        "jordan_sex_ever_000 = True",
                        "jordan_sex_bar_008 = True",
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode008/e08_012.rpyc', 99) : {
                "I like you. Maybe I want to take things further." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Jordan Solo Serious",
                        "jordan_solo_serious_008 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode008/e08_019.rpyc', 161) : {
                "(Go down on her.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode008/e08_027.rpyc', 75) : {
                "Or maybe we can stay here. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Flirt with Riley in Club",
                        "riley_flirt_club_008 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode008/e08_028.rpyc', 145) : {
                "(Ask Sophia out on a date.) (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Ask Sophia on a Date",
                        "sop_flirt_point +=1",
                        "sophia_study_date_008 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode009/e09_010.rpyc', 132) : {
                "Maybe you and I can get... involved. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "sop_flirt_point +=1"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode009/e09_010.rpyc', 176) : {
                "Maybe you can do something about that. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "sop_flirt_point +=1"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode009/e09_011.rpyc', 55) : {
                "(Accept Sophia's invite to her place.) (Interested)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode009/e09_011.rpyc', 77) : {
                "That's fine with me. (Accept)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "sophia_sex_ever_000 = True",
                        "Sophia Sex",
                        "sophia_sex_first_009 = True"

                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode009/e09_012.rpyc', 247) : {
                "(Go down on her.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode009/e09_012.rpyc', 834) : {
                "(Kiss and compliment her.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode009/e09_019.rpyc', 131) : {
                "...taking a picture with my girl. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Vanessa Flirt Shades",
                        "vanessa_shades_flirt_009 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode010/e010_005.rpyc', 224) : {
                "(Send her a text to meet tonight.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode010/e010_008.rpyc', 128) : {
                "That sounds like fun." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Sophia Next Date",
                        "sophia_next_date_010 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode010/e010_009.rpyc', 246) : {
                "And maybe we'll get to know each other better. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "gra_flirt_point +=1"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode010/e010_011.rpyc', 151) : {
                "(Kiss her.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode010/e010_012.rpyc', 377) : {
                "(Convince Riley to go out on a date.) (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Convince Riley To Go a Date",
                        "riley_dance_date_010 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode011/e011_006.rpyc', 400) : {
                "Let's do something tonight. (Have fun with Grace.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Have Sex With Grace",
                        "grace_sex_ever_000 = True",
                        "grace_accept_sex_011 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode011/e011_007.rpyc', 196) : {
                "(Go down on her.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode011/e011_013.rpyc', 682) : {
                "You're so beautiful. (Pursue Vanessa)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Pursue Vanessa",
                        "vanessa_pursue_011 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode012/e012_002.rpyc', 193) : {
                "I got something you can handle right now. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "lor_flirt_point +=1"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode012/e012_002.rpyc', 274) : {
                "A favor, huh? (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "lor_flirt_point +=1"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode012/e012_020.rpyc', 286) : {
                "Is that what you want? (Fuck Lorelei)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "lori_first_sex_012 = True",
                        "Fuck Lorelei",
                        "lorelei_sex_ever_000 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode012/e012_022.rpyc', 262) : {
                "I'm just trying to impress you. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "str_flirt_point +=1"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode013/e013_006.rpyc', 162) : {
                "(Take a peek at her ass.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode013/e013_006.rpyc', 396) : {
                "(Invite Marisa over to fuck.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "marisa_sex_ever_000 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode013/e013_009.rpyc', 136) : {
                "(Flirt and make a move on her.) (Sex)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "stranger_sex_ever_000 = True",
                        "Fuck Irene",
                        "irene_hillside_first_sex_013 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode013/e013_014.rpyc', 173) : {
                "(Go down on her to relax her.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode014/e014_002.rpyc', 46) : {
                "And maybe after, I can choke you next. (Flirt)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "lor_flirt_point +=1"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode014/e014_009.rpyc', 162) : {
                "No way! I love pineapple on pizza!" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Tell Vanessa You Like Pineapple on Pizza",
                        "vanessa_pineapple_pizza_like_014 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode014/e014_011.rpyc', 82) : {
                "(I bet she's shaved completely...)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Vanessa Shaved",
                        "vanessa_private_shaved_014 = True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode015/e015_006.rpyc', 401) : {
                "(Check Riley out.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode015/e015_006.rpyc', 483) : {
                "(Move close and kiss Riley.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            
            (u'scripts/episode015/e015_009.rpyc', 278) : {
                "Maybe I did just want to sleep with you. (Pursue Riley)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Riley Solo Romance",
                        "riley_pursue_015 = True",
                        "erika_romance_solo = False",
                        "harlow_romance_solo = False",
                        "kate_romance_solo = False",
                        "vanessa_romance_solo = False",
                        "marisa_romance_solo = False",
                        "jordan_romance_solo = False",
                        "sophia_romance_solo = False",
                        "lorelei_romance_solo = False",
                        "grace_romance_solo = False",
                        "stranger_romance_solo = False",
                        ],
                    "color" : pink
                    },
                "It was always more than your looks. (Pursue Riley)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Riley Solo Romance",
                        "riley_pursue_015 = True",
                        "erika_romance_solo = False",
                        "harlow_romance_solo = False",
                        "kate_romance_solo = False",
                        "vanessa_romance_solo = False",
                        "marisa_romance_solo = False",
                        "jordan_romance_solo = False",
                        "sophia_romance_solo = False",
                        "lorelei_romance_solo = False",
                        "grace_romance_solo = False",
                        "stranger_romance_solo = False",
                        ],
                    "color" : pink
                    },
                "I always had a thing for you. (Don't Pursue Riley)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                "It was never about {i}that{/i} for me. (Don't Pursue Riley)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                },
            (u'game/mod/overwrites.rpy', 4653) : {
                "Pursue Riley but keep other relationships active" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Pursue Riley",
                        "riley_pursue_015 = True"
                        ],
                    "color" : pink
                    },
                "Maybe I did just want to sleep with you. (Pursue Riley)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Riley Solo Romance",
                        "riley_pursue_015 = True",
                        "erika_romance_solo = False",
                        "harlow_romance_solo = False",
                        "kate_romance_solo = False",
                        "vanessa_romance_solo = False",
                        "marisa_romance_solo = False",
                        "jordan_romance_solo = False",
                        "sophia_romance_solo = False",
                        "lorelei_romance_solo = False",
                        "grace_romance_solo = False",
                        "stranger_romance_solo = False",
                        ],
                    "color" : pink
                    },
                "It was always more than your looks. (Pursue Riley)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [
                        "Riley Solo Romance",
                        "riley_pursue_015 = True",
                        "erika_romance_solo = False",
                        "harlow_romance_solo = False",
                        "kate_romance_solo = False",
                        "vanessa_romance_solo = False",
                        "marisa_romance_solo = False",
                        "jordan_romance_solo = False",
                        "sophia_romance_solo = False",
                        "lorelei_romance_solo = False",
                        "grace_romance_solo = False",
                        "stranger_romance_solo = False",
                        ],
                    "color" : pink
                    },
                "I always had a thing for you. (Don't Pursue Riley)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                "It was never about {i}that{/i} for me. (Don't Pursue Riley)" : {
                    "wt" : "{}".format(_dech),
                    "hint" : [

                        ],
                    "color" : pink
                    },
                },

            (u'scripts/episode015/e015_009.rpyc', 523) : {
                "(Accept Riley's offer to have sex.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Have Sex With Riley",
                        "riley_sex_015 = True",
                        "riley_sex_ever_000 = True",
                        ],
                    "color" : blue
                    },
                },
            (u'game/mod/overwrites.rpy', 4943) : {
                "(Accept Riley's offer to have sex.)" : {
                    "wt" : "{}".format(_bech),
                    "hint" : [

                        ],
                    "color" : blue
                    },
                },

            (u'scripts/episode015/e015_010.rpyc', 204) : {
                "I like the way you trimmed it." : {
                    "wt" : "{}".format(_bech),
                    "hint" : [
                        "Like Riley's Pussy",
                        "riley_private_trim_015 == True"
                        ],
                    "color" : blue
                    },
                },
            (u'scripts/episode015/e015_010.rpyc', 236) : {
                "(Go down on Riley.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },
            (u'scripts/episode015/e015_010.rpyc', 706) : {
                "(Go down on Riley.)" : {
                    "wt" : "{}".format(_recc),
                    "hint" : [

                        ],
                    "color" : yellow
                    },
                },

            }

    valid_dic_items = [#Changes Every Update
    
        ]

    ignore_dic = load_data("z_walkthrough_ignore")
    
    ignore_list = [
        ]

    end_list = [
        ".flac", ".mp3", ".ogg", "opus", ".wav", #Audio Extensions
        ".webm", ".avi", ".mp4", ".mkv", ".ogv", #Video Extensions
        ".webp", ".png", ".jpg", #Image Extensions
        #".rpyc", ".rpa", #Renpy Extensions
        ".ttf", ".otf", ".ttc", #Font Extensions
        ".txt", #Other Extensions
        ".save", "persistent", ".json",
        ]
    
    def read_rpy_file(file):
        try:
            with renpy.open_file(file, encoding="utf-8") as readfile:
                return readfile.readlines()
        except:
            with renpy.file(file) as readfile:
                return readfile.readlines()
        else:
            try:
                with open(os.path.join(config.gamedir, file), "r", encoding="utf-8") as readfile:
                    return readfile.readlines()
            except:
                with open(os.path.join(config.gamedir, file), "r") as readfile:
                    return readfile.readlines()

    def extract_rpy(name):
        """
        Extract the rpy file within the basedir to folder extracted_files
        """
        path = os.path.join(config.basedir, "extracted_{}".format(name))

        subfolder = os.path.dirname(os.path.join(config.basedir, "extracted_{}".format(name))).replace("\\","/")
        
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)

        f = read_rpy_file(name)
        if os.path.exists(path):
            return
        try:
            with open(path, "w", encoding="utf-8") as d:
                d.writelines(f)
        except:
            with open(path, "w") as d:
                d.writelines(f)

    def check_dic(current_dictionary, scripts, use_precise=True):
        """
        Generate a dictionary from 'scripts' containing
        'short_key', 'name' and 'path'
        This grabs the full .rpy file while busy

        Iterate over 'generated_dictionary' and 'current_dictionary'
        to do comparisons of files and lines

        Uses two functions to find the menu lines to see if they match 'current_dictionary'

        Function 'find_closest_menu_before_name' uses a range checker to match where 
        menu is found and searches backwards using a distance checker (Precise Search)

        Function 'find_menu_before_name' uses a range checker to match where
        menu is found and searches backwards no distance (Fuzzy Search)

        Outputs data to 'walkthrough_check.txt' to make corrections and check

        """

        counter = 0
        generated_dictionary = {}

        def find_closest_menu_before_name(lines, name, r_count, out=False):
            closest_menu_line = None
            min_distance = float('inf')

            for i, line in enumerate(lines):
                line = line.replace("\\","")
                # Check if the name, including double quotes, is in the line
                if name in line:
                    # Check if this `name` line is after `r_count`
                    if i >= r_count:
                        # Search backwards from the current line to find the nearest `menu`
                        for j in range(i, -1, -1):
                            if 'menu' in lines[j]:
                                # Calculate distance from `r_count` to the found `menu`
                                distance = abs(r_count - j)
                                if distance < min_distance:
                                    if out:
                                        print("Found {} in {} at {}").format(name, line.strip(), i+1)
                                    min_distance = distance
                                    closest_menu_line = j + 1  # Convert to 1-indexed
                                break  # Stop searching backwards once we find the closest menu
            return closest_menu_line

        def find_menu_before_name(lines, name, out=False):
            for i, line in enumerate(lines):
                if name in line:
                    # Search backwards from the current line
                    for j in range(i, -1, -1):
                        if 'menu' in lines[j]:
                            if out:
                                print("Found {} in {} at {}").format(name, line.strip(), i+1)
                            # Return the line number (1-indexed)
                            return j + 1
            return None
        
        def output(line):
            p = os.path.join(config.basedir, "walkthrough_check.txt")
            with open(p, 'a') as file:
                print(line)
                file.write("{}\n".format(line))

        for short_key, name, path in scripts:
            generated_dictionary[short_key] = [name, read_rpy_file(path), path]
            extract_rpy(path)

        # Iterate over the generated dictionary and the current walkthrough dictionary
        for key, value in generated_dictionary.items():
            for wt_key, wt_value in current_dictionary.items():
                r_count = wt_key[1]
                # Check if the name in value[0] is part of the current wt_key[0]
                if "{}".format(value[0] if use_archive_format else "game/{}".format(value[0])) in wt_key[0]:
                    for name in wt_value:
                        # Find the closest menu line number
                        ln = find_closest_menu_before_name(value[1], '"{}"'.format(name), r_count) #Precise Search
                        al = find_menu_before_name(value[1], '"{}"'.format(name)) #Fuzzy Search
                        # Create the tuple with the filename and the line number
                        if use_archive_format:
                            d = ("{}c".format(value[2]), ln) if use_precise else  ("{}c".format(value[2]), al) #Create the correct value .rpyc and line number
                        else:
                            include_game = "game/" if not value[2].startswith("game/") else ""
                            d = ("{}{}".format(include_game,value[2]), ln) if use_precise else  ("{}{}".format(include_game,value[2]), al) #Create the correct value .rpyc and line number
                        # Print the result with the correct key and value
                        if wt_key != d and not wt_key in valid_dic_items:
                            counter += 1
                            output("Current: {}\nNew: {}\nLine: {}\nCould Be Mistaken For a Sub Menu\n".format(wt_key, d, name))
        return "Total Items not matching correctly: {}".format(counter)

    def filter_wt(fil):
        """

        'fil' needs to be the full path eg '"new scripts/Student Interaction.rpy"' or
        'script.rpy'

        It will match the lines from the file with the walkthrough dictionary
        """
       
        out = []

        for script, i in walkthrough_dict().keys():
            if fil in script:
                out.append(i)
       
        return out

    def get_rpy_files(ignore_list=ignore_list, end_list=end_list):
        rpys = []
        """
        
        This Function Gets all the files mainly '.rpy'
        files.
        
        Add files to ignore in 'ignore_list'
        
        Add extensions to ignore in 'end_list'

        """

        for file in renpy.list_files():
            if file.startswith(("python-packages", "mod", "tl")):
                continue
            if not file in ignore_list:
                if file.endswith(".rpy"):
                    rpys.append(file)

        return rpys

    def get_menu_lines(filename, ignore_lines, episodes=1):
        """
        This Function will find all the menu lines in the script
        
        Function will output data to 'menu_finder.txt' in the base
        game dir

        Uses external Function 'read_rpy_file' to open the files within
        the archives

        """
        def replacing(item, episode):
            replacements = []#["scripts/", "core/"] + ["episode{:03}/".format(i) for i in range(1, 15+1)]
            for i in replacements:
                item = item.replace(i, '')
            
            return item+("c" if use_archive_format else '')

        output_data = []
        data = read_rpy_file(filename)
        p = os.path.join(config.basedir, "menu_finder.txt")

        for i, line in enumerate(data, 1):
            if line.strip().startswith(("label", "tag", "define", "if", "elif", "#")):
                continue
            elif "quick_menu" in line:
                continue
            elif "menu:" in line and not i in ignore_lines:
                output_data.append((replacing(filename, episodes), i))
            elif "menu " in line and not i in ignore_lines:
                output_data.append((replacing(filename, episodes), i))
        if output_data:
            with open(p, "a") as file:
                for c, i in enumerate(output_data, 1):
                    file.write("{} {}\n".format(c, str(i)))
                file.write("\n")

    def update_check_walkthrough(episode=gui.current_episode):
        """
        Use this to check if the lines match up after
        every update an get new menu items.

        Uses external function 'get_menu_lines'
        whilst checking to find current_lines using 'filter_wt' and ignore lists

        Uses external function 'check_dic'

        """

        p = os.path.join(config.basedir, "menu_finder.txt")

        if os.path.exists(p):
            with open(p, "w") as f:
                pass


        files = get_rpy_files()
        files = [i.replace(".rpy", "") for i in files if i.endswith(".rpy")]

        def replacing(item, episode):
            replacements = ["scripts/", "core/"] + ["episode{:03}/".format(i) for i in range(0, 15+1)]
            for i in replacements:
                item = item.replace(i, '')
            
            return item

        for i in files:
            lst = replacing(i, episode)
            data = ignore_dic.get(lst, [])

            get_menu_lines("{}.rpy".format(i), filter_wt("{}".format(i))+data, 15)

        return check_dic(walkthrough_dict(),[("{}".format(i), "{}".format(i), "{}.rpy".format(i)) for i in files])

"""
^\s*\$(?!.*\b(persistent|two_choice|quick_menu|sex_four_choice|sex_three_choice|four_choice|sex_two_choice)\b).*= True\s*$
"""