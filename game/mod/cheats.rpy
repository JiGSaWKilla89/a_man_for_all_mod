screen cheatmodnavigation():
    modal True
    add "#000"
    add Transform(bg_mod(), zoom=1.00) alpha 0.90 xalign 0.5 yalign 0.5
    textbutton "{size=40}Return{/size}" action Return() xalign 1.0 yalign 1.0
screen cheatmod():
    tag menu
    use cheatmodnavigation
    style_prefix "affections"
    hbox:
        yalign 0.45
        xalign 0.5
        spacing 110
        textbutton "{size=55}Your Stats" action ShowMenu("Yourstats") #xalign 0.30 yalign 0.45
        textbutton "{size=55}Affections" action ShowMenu("Affections") #xalign 0.70 yalign 0.45
        textbutton "{size=55}Relationships" action ShowMenu("Relationships") #xalign 0.70 yalign 0.45
    #textbutton "{size=55}Other Settings" action ShowMenu("otherModSettings") xalign 1.0 yalign 0.05
    #textbutton "{size=55}Variables" action ShowMenu("variables") xalign 1.0 yalign 0.15
    key "K_j" action Return(),With(Dissolve(0.2))
    key "game_menu" action Return(),With(Dissolve(0.2))
screen Yourstats():
    tag menu
    use cheatmodnavigation
    add Transform(mc_mod(), zoom=1.00) xalign 0.5 yalign 0.5
    add Solid("#000") alpha 0.5
    style_prefix "affections"
    textbutton "{size=40}Return{/size}" action ShowMenu("cheatmod") xalign 1.0 yalign 1.0
    key "game_menu" action ShowMenu("cheatmod")
    default hbsize = gui.text_size

    default max_val = max(getattr(store,"mc_diplomat"), getattr(store,"mc_rebel"))


    vbox:
        align (0.5, 0.0)
        yfill True
        vbox:
            ysize (config.screen_height//2)-200
            yalign 0.0
            xfill True
            hbox:
                style "_default"
                box_wrap True
                spacing 200
                align (0.5,0.5)
                vbox:
                    spacing 30
                    text "Diplomat" style "affections_diplomat"
                    fixed:
                        xysize(400,40)
                        bar value VariableValue("mc_diplomat", 100) style "affections_diplomat_bar"
                        text "[mc_diplomat]" style "affections_kjs_bar"
                    textbutton _("Match Highest") action SetVariable("mc_diplomat", max_val)
                vbox:
                    spacing 30
                    text "Rebel" style "affections_rebel"
                    fixed:
                        xysize(400,40)
                        bar value VariableValue("mc_rebel", 100) style "affections_rebel_bar"
                        text "[mc_rebel]" style "affections_kjs_bar"
                    textbutton _("Match Highest") action SetVariable("mc_rebel", max_val)

        if get_char_variables("Mc"):
            vbox:
                ysize (config.screen_height//2)+200
                yalign 1.0
                xfill True
                label "%s Variables"%mc.title()
                vpgrid:
                    cols 2
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    
                    for cheat in CheatVariables.variables:
                        if cheat.character == "Mc":
                            $  hbsize = get_variables_list("Mc")
                            frame:
                                if isinstance(cheat.var, list):
                                    vbox:
                                        ysize hbsize
                                        hbox:
                                            textbutton (cheat.name) action SetVariable(cheat.var[0], not eval(cheat.var[0])), SetVariable(cheat.var[1], not eval(cheat.var[1]))
                                            text "%s"%eval(cheat.var[0]) xalign 1.0 yalign 0.5
                                        hbox:
                                            textbutton (cheat.alt) action SetVariable(cheat.var[1], not eval(cheat.var[1])), SetVariable(cheat.var[0], not eval(cheat.var[0]))
                                            text "%s"%eval(cheat.var[1]) xalign 1.0 yalign 0.5
                                elif isinstance(cheat.var, str):
                                    hbox:
                                        ysize hbsize
                                        if isinstance(cheat.var, str):
                                            textbutton (cheat.name if eval(cheat.var) else cheat.alt) action ToggleVariable(cheat.var)
                                            text "%s"%eval(cheat.var) xalign 1.0  yalign 0.5
screen Affections():
    tag menu
    style_prefix "affections"
    use cheatmodnavigation
    textbutton "Kate" action ShowMenu("charactersStats", who="kate") xalign 0.09
    textbutton "Harlow" action ShowMenu("charactersStats", who="harlow") xalign 0.28
    textbutton "Riley" action ShowMenu("charactersStats", who="riley") xalign 0.5 
    textbutton "Vanessa" action ShowMenu("charactersStats", who="vanessa") xalign 0.72
    textbutton "Erika" action ShowMenu("charactersStats", who="erika") xalign 0.92
    #textbutton "Relationships" action ShowMenu("Relationships") xalign 1.0 yalign 0.02
    textbutton "Return" action ShowMenu("cheatmod") xalign 1.0 yalign 1.0
    key "game_menu" action ShowMenu("cheatmod")
screen charactersStats(who):
    tag menu
    style_prefix "affections"
    use cheatmodnavigation

    default mychar = who.title()
    default hide_interface = False
    
    python:
        who = mychar
        from collections import OrderedDict
        char_stats = OrderedDict((
            ("Kate"    , "kat"),
            ("Harlow"  , "har"),
            ("Riley"   , "ril"),
            ("Vanessa" , "van"),
            ("Erika"   , "eri")
        ))

        char = char_stats.get(who.title(),"")

        highest_value = max(getattr(store,"{}_knight".format(char.lower())), getattr(store,"{}_joker".format(char.lower())), getattr(store,"{}_smooth".format(char.lower())))

    add Transform("mod/affs/%s.jpg"%who.lower(), zoom=1.00) xalign 0.5 yalign 0.5
    add Solid("#000") alpha 0.5
    textbutton "{size=40}Return{/size}" action ShowMenu("Affections") xalign 1.0 yalign 1.0
    textbutton "{size=40}Hide Info{/size}" action ToggleLocalVariable("hide_interface"),With(dissolve) xalign 0.0 yalign 1.0
    default hbsize = gui.text_size
    key "game_menu" action ShowMenu("Affections")
    if not hide_interface:
        vbox:
            align (0.5, 0.0)
            yfill True
            vbox:
                ysize (config.screen_height//2)-200
                yalign 0.0
                xfill True
                hbox:
                    style "_default"
                    box_wrap True
                    spacing 200
                    align (0.5,0.5)
                    vbox:
                        spacing 30
                        text "Knight" style "affections_knight"
                        fixed:
                            xysize(400,40)
                            bar value VariableValue("%s_knight"%char.lower(), 100) style "affections_knight_bar"
                            text "[%s_knight]"%char.lower() style "affections_kjs_bar"
                        textbutton _("Match Highest") action SetVariable("%s_knight"%char.lower(), highest_value)
                    vbox:
                        spacing 30
                        text "Joker" style "affections_joker"
                        fixed:
                            xysize(400,40)
                            bar value VariableValue("%s_joker"%char.lower(), 100) style "affections_joker_bar"
                            text "[%s_joker]"%char.lower() style "affections_kjs_bar"
                        textbutton _("Match Highest") action SetVariable("%s_joker"%char.lower(), highest_value)
                    vbox:
                        spacing 30
                        text "Smooth" style "affections_smooth"
                        fixed:
                            xysize(400,40)
                            bar value VariableValue("%s_smooth"%char.lower(), 100) style "affections_smooth_bar"
                            text "[%s_smooth]"%char.lower() style "affections_kjs_bar"
                        textbutton _("Match Highest") action SetVariable("%s_smooth"%char.lower(), highest_value)
            
            if get_char_variables(who):
                vbox:
                    ysize (config.screen_height//2)+200
                    yalign 1.0
                    xfill True
                    label "%s Variables"%who.title()
                    vpgrid:
                        cols 2
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        
                        for cheat in CheatVariables.variables:
                            if cheat.label == None or (renpy.has_label(cheat.label+"_modded") and renpy.seen_label(cheat.label+"_modded")) or (cheat.label != None and renpy.seen_label(cheat.label)):
                                if cheat.character == who.title():
                                    $  hbsize = get_variables_list(who)
                                    frame:
                                        if cheat.name.startswith("Replay"):
                                            if isinstance(cheat.var, list):
                                                vbox:
                                                    ysize hbsize
                                                    hbox:
                                                        textbutton (cheat.name) action SetVariable(cheat.var[0], not eval(cheat.var[0])), SetVariable(cheat.var[1], not eval(cheat.var[1]))
                                                        text "%s"%eval(cheat.var[0]) xalign 1.0 yalign 0.5
                                                    hbox:
                                                        textbutton (cheat.alt) action SetVariable(cheat.var[1], not eval(cheat.var[1])), SetVariable(cheat.var[0], not eval(cheat.var[0]))
                                                        text "%s"%eval(cheat.var[1]) xalign 1.0 yalign 0.5
                                            elif isinstance(cheat.var, str):
                                                hbox:
                                                    ysize hbsize
                                                    if isinstance(cheat.var, str):
                                                        textbutton (cheat.name if eval(cheat.var) else cheat.alt) action ToggleVariable(cheat.var)
                                                        text "%s"%eval(cheat.var) xalign 1.0  yalign 0.5
                                        else:
                                            if isinstance(cheat.var, list):
                                                vbox:
                                                    ysize hbsize
                                                    hbox:
                                                        textbutton (cheat.name) action SetVariable(cheat.var[0], not eval(cheat.var[0])), SetVariable(cheat.var[1], not eval(cheat.var[1]))
                                                        text "%s"%eval(cheat.var[0]) xalign 1.0 yalign 0.5
                                                    hbox:
                                                        textbutton (cheat.alt) action SetVariable(cheat.var[1], not eval(cheat.var[1])), SetVariable(cheat.var[0], not eval(cheat.var[0]))
                                                        text "%s"%eval(cheat.var[1]) xalign 1.0 yalign 0.5
                                            elif isinstance(cheat.var, str):
                                                hbox:
                                                    ysize hbsize
                                                    if isinstance(cheat.var, str):
                                                        textbutton (cheat.name if eval(cheat.var) else cheat.alt) action ToggleVariable(cheat.var)
                                                        text "%s"%eval(cheat.var) xalign 1.0  yalign 0.5


    hbox: #Navigation
        align (0.5,0.98)
        spacing 25
        for _key, _value in char_stats.items():
            textbutton _key action [SetLocalVariable("mychar", _key),With(Dissolve(0.2))] selected who == _key
screen Relationships():
    tag menu
    style_prefix "affections"
    use cheatmodnavigation
    default who = "Grace"
    default hbsize = gui.text_size
    default hide_interface = False
    python:
        from collections import OrderedDict
        if not met_seo_official:
            char_stats = OrderedDict((
                ("Grace",    "gra"),
                ("Jordan",   "jor"),
                ("Lorelei",  "lor"),
                ("Marisa",   "mar"),
                ("Sophia",   "sop"),
                ("Stranger", "str")
                ))
        else:
            char_stats = OrderedDict((
                ("Grace",   "gra"),
                ("Irene",   "str"),
                ("Jordan",  "jor"),
                ("Lorelei", "lor"),
                ("Marisa",  "mar"),
                ("Sophia",  "sop")
                ))


    add Transform("mod/rels/%s.jpg"%who.lower(), zoom=1.00) xalign 0.5 yalign 0.5
    add Solid("#000") alpha 0.5
    #textbutton "{size=40}Return{/size}" action ShowMenu("Affections") xalign 1.0 yalign 1.0
    #key "game_menu" action ShowMenu("Affections")

    textbutton "Return" action ShowMenu("cheatmod") xalign 1.0 yalign 1.0
    textbutton "{size=40}Hide Info{/size}" action ToggleLocalVariable("hide_interface"),With(dissolve) xalign 0.0 yalign 1.0
    key "game_menu" action ShowMenu("cheatmod")
    
    hbox: #Navigation
        align (0.5,0.98)
        spacing 25
        for _key, _value in char_stats.items():
            textbutton _key action [SetLocalVariable("who", _key),With(Dissolve(0.2))] selected who == _key
    if not hide_interface:
        vbox:
            align (0.5, 0.0)
            yfill True
            vbox:
                ysize (config.screen_height//2)-200
                yalign 0.0
                xfill True
                hbox:
                    style "_default"
                    box_wrap True
                    spacing 200
                    align (0.05,0.5)
                    vbox:
                        spacing 30

                        text"{size=50}{color=#c896ff}%s{/color}"%who ycenter 0.8  outlines [(2, "#000", 0, 3)]
                        fixed:
                            xysize(400,40)
                            bar value VariableValue("%s_flirt_point"%char_stats.get(who, "gra"), 100)
                            text "{size=40}{color=#ffffff}[%s_flirt_point]{/color}"%char_stats.get(who, "gra") xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]
            
            if get_char_variables(who):
                vbox:
                    ysize (config.screen_height//2)+200
                    yalign 1.0
                    xfill True
                    label "%s Variables"%who.title()
                    vpgrid:
                        cols 2
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        
                        for cheat in CheatVariables.variables:
                            if cheat.character == who.title():
                                $  hbsize = get_variables_list(who)
                                frame:
                                    if isinstance(cheat.var, list):
                                        vbox:
                                            ysize hbsize
                                            hbox:
                                                textbutton (cheat.name) action SetVariable(cheat.var[0], not eval(cheat.var[0])), SetVariable(cheat.var[1], not eval(cheat.var[1]))
                                                text "%s"%eval(cheat.var[0]) xalign 1.0 yalign 0.5
                                            hbox:
                                                textbutton (cheat.alt) action SetVariable(cheat.var[1], not eval(cheat.var[1])), SetVariable(cheat.var[0], not eval(cheat.var[0]))
                                                text "%s"%eval(cheat.var[1]) xalign 1.0 yalign 0.5
                                    elif isinstance(cheat.var, str):
                                        hbox:
                                            ysize hbsize
                                            if isinstance(cheat.var, str):
                                                textbutton (cheat.name if eval(cheat.var) else cheat.alt) action ToggleVariable(cheat.var)
                                                text "%s"%eval(cheat.var) xalign 1.0  yalign 0.5

# Defaults
default modnarrator = Character("JiGSaW", who_color="#FB4301")
default episode_end = 1
default episode_mc = 1
default met_seo_official = False
default replay_override = False
default replay_override_label = ""
default current_episode = "Episode 0"

# Transform
transform replays_trans:
    on idle:
        easein .2 matrixcolor(SaturationMatrix(0.0, desat=(0.2126, 0.7152, 0.0722)))
    on hover:
        easein .2 matrixcolor(SaturationMatrix(1.0, desat=(0.2126, 0.7152, 0.0722)))

transform replays_blur(v):
    blur v

# Styles
style replay_gallery_frame:
    padding (10,10,10,0)
    xysize (320, 220)
    align (0.5,0.5)
    background None

style replay_gallery_text:
    align (0.5,1.0)
    text_align 0.5
    outlines [(2, "#0009", 1, 1)]

style replay_gallery_hbox:
    spacing 30

style replay_gallery_vbox:
    xsize 300

style replay_gallery_vscrollbar is gui_vscrollbar:
    unscrollable "hide"
    xalign 1.0

style affections_label_text:
    size gui.title_text_size
    color gui.accent_color
    align (0.5,0.5)
    text_align 0.5
    outlines [(2, "#0009", 1, 1)]

style affections_label:
    align (0.5,0.0)

style affections_vpgrid:
    xsize config.screen_width
    yalign 0.0
    xalign 0.5
    spacing 50
    yoffset -30
    ysize (config.screen_height//2)-30

style affections_button:
    padding (0,0,0,0)
    yalign 0.5

style affections_frame:
    padding gui.frame_borders.padding
    background Transform(Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile), alpha=.7)


    right_margin 10
    left_margin 10

style affections_hbox:
    xsize (config.screen_width//2)-70

style affections_button_text:
    outlines [(2, "#0009", 1, 1)]
    text_align 0.5
    size 40
    color gui.text_color
    hover_color gui.hover_color
    selected_color "#7a007a"
    selected_hover_color gui.hover_color
    insensitive_color gui.insensitive_color

style affections_text:
    outlines [(2, "#0009", 1, 1)]
    text_align 0.5
    size 40

style affections_vscrollbar is gui_vscrollbar:
    unscrollable "hide"
    xalign 1.0 #xoffset 120

    #gui.textbox_location

style affections_knight_bar:
    ysize gui.bar_size
    left_bar Frame(Solid("#4bafff"), gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style affections_joker_bar:
    ysize gui.bar_size
    left_bar Frame(Solid("#00af00"), gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style affections_smooth_bar:
    ysize gui.bar_size
    left_bar Frame(Solid("#ff0096"), gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style affections_kjs_bar:
    size 40
    color gui.text_color
    xcenter 0.5 
    ycenter 0.45 
    outlines [(2, "#000", 0, 2)]

style affections_knight:
    color "#4bafff"
    size 50
    ycenter 0.8
    outlines [(2, "#0009", 0, 3)]

style affections_joker:
    color "#00af00"
    size 50
    ycenter 0.8  
    outlines [(2, "#000", 0, 3)]

style affections_smooth:
    color "#ff0096"
    size 50
    ycenter 0.8
    outlines [(2, "#0009", 0, 3)]

style affections_diplomat_bar:
    ysize gui.bar_size
    left_bar Frame(Solid("#ffc800"), gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style affections_rebel_bar:
    ysize gui.bar_size
    left_bar Frame(Solid("#ff0000"), gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style affections_diplomat:
    color "#ffc800"
    size 50
    ycenter 0.8
    outlines [(2, "#0009", 0, 3)]

style affections_rebel:
    color "#ff0000"
    size 50
    ycenter 0.8  
    outlines [(2, "#000", 0, 3)]


init python:
    def get_char_variables(who):
        return any(i for i in CheatVariables.variables if i.character == who.title())

    def get_variables_list(who):
        return gui.text_size * 4 if any(isinstance(c.var, list) for c in CheatVariables.variables if c.character == who.title()) else gui.text_size

    class CheatVariables():
        variables = []
        def __init__(self, character, name, alt, var, label=None):
            self.character = character
            self.name = name
            self.alt = alt
            self.var = var
            self.label = label
            CheatVariables.variables.append(self)

            if character == "Stranger":
                # Create a new instance with updated attributes and add it
                alternate = CheatVariables("Irene", name.replace("Stranger", "Irene"), alt.replace("Stranger", "Irene"), var, label)

            if character == "Jordan" and var == "jordan_marisa_threesome_sex_bar_008":
                alternate = CheatVariables("Marisa", name.replace("Jordan", "Marisa"), alt.replace("Jordan", "Marisa"), var, label)
                

        def __repr__(self):
            return "({}, {}, {})".format(self.character, self.var, eval(self.var))


#define cheat_marica_sex_006 = CheatVariables("Marisa", "Had Sex With Marisa Before", "Didn't Have Sex With Marisa Before", "marisa_sex_previous_006", "episode06_000_variables")

#define cheat_comfort_kate_003 = CheatVariables("Kate", "Comforted Kate", "Didn't Comfort Kate", "comfort_kate_meeting_003")
#
define cheat_erika_romance_solo = CheatVariables(
    "Erika", 
    "Erika Solo Romance", 
    "No Erika Solo Romance", 
    "erika_romance_solo"
    )
define cheat_harlow_romance_solo = CheatVariables(
    "Harlow", 
    "Harlow Solo Romance", 
    "No Harlow Solo Romance", 
    "harlow_romance_solo"
    )
define cheat_riley_romance_solo = CheatVariables(
    "Riley", 
    "Riley Solo Romance", 
    "No Riley Solo Romance", 
    "riley_romance_solo"
    )
define cheat_vanessa_romance_solo = CheatVariables(
    "Vanessa", 
    "Vanessa Solo Romance", 
    "No Vanessa Solo Romance", 
    "vanessa_romance_solo"
    )
define cheat_marisa_romance_solo = CheatVariables(
    "Marisa", 
    "Marisa Solo Romance", 
    "No Marisa Solo Romance", 
    "marisa_romance_solo"
    )
define cheat_jordan_romance_solo = CheatVariables(
    "Jordan", 
    "Jordan Solo Romance", 
    "No Jordan Solo Romance", 
    "jordan_romance_solo"
    )
define cheat_sophia_romance_solo = CheatVariables(
    "Sophia", 
    "Sophia Solo Romance", 
    "No Sophia Solo Romance", 
    "sophia_romance_solo"
    )
define cheat_lorelei_romance_solo = CheatVariables(
    "Lorelei", 
    "Lorelei Solo Romance", 
    "No Lorelei Solo Romance", 
    "lorelei_romance_solo"
    )
define cheat_grace_romance_solo = CheatVariables(
    "Grace", 
    "Grace Solo Romance", 
    "No Grace Solo Romance", 
    "grace_romance_solo"
    )
define cheat_stranger_romance_solo = CheatVariables(
    "Stranger", 
    "Stranger Solo Romance", 
    "No Stranger Solo Romance", 
    "stranger_romance_solo"
    )
define cheat_kate_romance_solo = CheatVariables(
    "Kate", 
    "Kate Solo Romance", 
    "No Kate Solo Romance", 
    "kate_romance_solo"
    )

define cheat_harlow_pursue_004 = CheatVariables(
    "Harlow", 
    "Pursue Harlow", 
    "Didn't pursue Harlow", 
    "harlow_pursue_004", 
    "episode04_019_viridian_meeting_room"
    )
define cheat_erika_pursue_005 = CheatVariables(
    "Erika", 
    "Pursue Erika", 
    "Didn't pursue Erika", 
    "erika_pursue_005", 
    "episode05_019_oldtownbar_erika"
    )
define cheat_kate_pursue_007 = CheatVariables(
    "Kate", 
    "Pursue Kate", 
    "Don't pursue Kate", 
    "kate_pursue_007", 
    "episode07_017_psych_office"
    )
define cheat_kate_office_pursue_decline_007 = CheatVariables(
    "Kate", 
    "Declined pursuing Kate", 
    "Didn't decline pursuing Kate", 
    "kate_office_pursue_decline_007",
    "episode07_017_psych_office"
    )
define cheat_vanessa_pursue_011 = CheatVariables(
    "Vanessa", 
    "Pursue Vanessa", 
    "Don't pursue Vanessa", 
    "vanessa_pursue_011", 
    "episode11_013_uptown_sushidate_vanessa_dancefloor"
    )
define cheat_riley_pursue_015 = CheatVariables(
    "Riley", 
    "Pursue Riley", 
    "Don't pursue Riley", 
    "riley_pursue_015",
    "episode15_009_date_confession"
    )


define cheat_erika_sex_ever_000 = CheatVariables(
    "Erika", 
    "Ever had sex with Erika", 
    "Never had sex with Erika", 
    "erika_sex_ever_000", 
    "episode07_010_apartment_erika_sex"
    )
define cheat_harlow_sex_ever_000 = CheatVariables(
    "Harlow", 
    "Ever had sex with Harlow", 
    "Never had sex with Harlow", 
    "harlow_sex_ever_000", 
    "episode07_014_funk_burger"
    )
define cheat_kate_sex_ever_000 = CheatVariables(
    "Kate", 
    "Ever had sex with Kate", 
    "Never had sex with Kate", 
    "kate_sex_ever_000", 
    "episode07_017_psych_office"
    )
define cheat_marisa_sex_ever_000 = CheatVariables(
    "Marisa", 
    "Ever had sex with Marisa", 
    "Never had sex with Marisa", 
    "marisa_sex_ever_000", 
    "episode08_009_midtown_bar_marisa_jordan"
    )
define cheat_jordan_sex_ever_000 = CheatVariables(
    "Jordan", 
    "Ever had sex with Jordan", 
    "Never had sex with Jordan", 
    "jordan_sex_ever_000", 
    "episode08_009_midtown_bar_marisa_jordan"
    )
define cheat_sophia_sex_ever_000 = CheatVariables(
    "Sophia", 
    "Ever had sex with Sophia", 
    "Never had sex with Sophia", 
    "sophia_sex_ever_000", 
    "episode09_011_alskitchen_outside_sophia"
    )
define cheat_grace_sex_ever_000 = CheatVariables(
    "Grace", 
    "Ever had sex with Grace", 
    "Never had sex with Grace", 
    "grace_sex_ever_000", 
    "episode11_006_uptown_apartment_meeting_grace"
    )
define cheat_lorelei_sex_ever_000 = CheatVariables(
    "Lorelei", 
    "Ever had sex with Lorelei", 
    "Never had sex with Lorelei", 
    "lorelei_sex_ever_000", 
    "episode12_020_chargersgym_checkin"
    )
define cheat_stranger_sex_ever_000 = CheatVariables(
    "Stranger", 
    "Ever had sex with Stranger", 
    "Never had sex with Stranger", 
    "stranger_sex_ever_000", 
    "episode13_009_hillside_irene_conversation"
    )
define cheat_riley_sex_ever_000 = CheatVariables(
    "Riley", 
    "Ever had sex with Riley", 
    "Never had sex with Riley", 
    "riley_sex_ever_000", 
    "episode15_009_date_confession"
    )


define cheat_erika_kiss_001 = CheatVariables(
    "Erika",
    "Kissed Erika",
    "Didn't Kiss Erika",
    "erika_kiss_001",
    "replay_e001_erika_kiss_choice"
    )
define cheat_erika_bj_001 = CheatVariables(
    "Erika",
    "Blowjob from Erika",
    "No Blowjob from Erika",
    "erika_bj_001",
    "episode01_012_erikatease"
    )
define cheat_erika_bj_001 = CheatVariables(
    "Mc",
    "Threatened Daniel",
    "Didn't threaten Daniel",
    "daniel_threaten_001",
    "episode01_015_coffeeshop_confrontation"
    )
define cheat_confess_riley_001 = CheatVariables(
    "Riley",
    "Confessed to Riley",
    "Didn't Confess to Riley",
    "confess_riley_001",
    "episode01_016_coffeeshop_outside"
    )
define cheat_riley_friend_002 = CheatVariables(
    "Riley",
    "Riley is a Friend",
    "Riley is not a Friend",
    "riley_friend_002",
    "episode02_009_bigpetes"
    )
define cheat_riley_crush_002 = CheatVariables(
    "Riley",
    "Riley is your Crush",
    "Riley is not your Crush", 
    "riley_crush_002",
    "episode02_010_coffeeshop_return"
    )
define cheat_vanessa_word_002 = CheatVariables(
    "Vanessa",
    "Want to win for Vanessa",
    "Didn't want to win for Vanessa", 
    "vanessa_word_002",
    "episode02_013_uptown_vanessa"
    )
define cheat_erika_fight_for_002 = CheatVariables(
    "Erika",
    "Fight for Erika",
    "Didn't Fight for Erika",
    "erika_fight_for_002",
    "episode02_015_oldtown_firstfight"
    )
define cheat_marisa_private_sex_002 = CheatVariables(
    "Marisa",
    "Fuck Marisa",
    "Didn't Fuck Marisa",
    "marisa_private_sex_002",
    "episode02_017_pinkrabbit_privatedance"
    )
define cheat_jack_fight_erika_003 = CheatVariables(
    "Erika",
    "Confirm Fighting for Erika",
    "Didn't Confirm Fight for Erika",
    "jack_fight_erika_003",
    "episode03_003_boxinggym"
    )
define cheat_jordan_pretty_003 = CheatVariables(
    "Jordan",
    "Told Jordan she is pretty",
    "Didn't tell Jordan she is pretty",
    "jordan_pretty_003",
    "episode03_007_midtownbar_meet_jordan"
    )
define cheat_jordan_for_her_003 = CheatVariables(
    "Jordan",
    "Worked for Jordan",
    "Didn't work for Jordan",
    "jordan_for_her_003",
    "episode03_010_midtownbar_cleanup"
    )
define cheat_comfort_kate_meeting_003 = CheatVariables(
    "Kate",
    "Comfort Kate",
    "Didn't comfort Kate",
    "comfort_kate_meeting_003",
    "episode03_011_sci_president_meeting_kate"
    )
define cheat_billy_kate_pretty_003 = CheatVariables(
    "Kate",
    "Told Billy Kate is attractive",
    "Didn't tell Billy Kate is attractive",
    "billy_kate_pretty_003",
    "episode03_012_coffeeshop_kate"
    )
define cheat_erika_kiss_pgs_003 = CheatVariables(
    "Erika",
    "Kiss Erika at Proving Grounds",
    "Didn't kiss Erika at Proving Grounds",
    "erika_kiss_pgs_003",
    "episode03_015_pgs_outside_deal"
    )
define cheat_jordan_shirt_off_003 = CheatVariables(
    "Jordan",
    "Take Jordan's bra off",
    "Didn't take Jordan's bra off",
    "jordan_shirt_off_003",
    "episode03_018_midtown_bar_backroom"
    )
define cheat_jordan_tell_riley_003 = CheatVariables(
    "Jordan",
    "Told Jordan you like Riley",
    "Didn't tell Jordan you like Riley",
    "jordan_tell_riley_003",
    "episode03_018_midtown_bar_backroom"
    )
define cheat_jordan_sex_accept_003 = CheatVariables(
    "Jordan",
    "Fuck Jordan how she wants to be fucked",
    "Didn't fuck Jordan how she wants to be fucked",
    "jordan_sex_accept_003",
    "episode03_018_midtown_bar_backroom"
    )
define cheat_like_vanessa_bruno_004 = CheatVariables(
    "Vanessa",
    "Told Bruno you like Vanessa",
    "Didn't tell Bruno you like Vanessa",
    "like_vanessa_bruno_004",
    "episode04_004_uptown_bruno_convo"
    )
define cheat_sophia_goodbye_004 = CheatVariables(
    "Sophia",
    "Chatted Sophia up",
    "Didn't chat Sophia up",
    "sophia_goodbye_004",
    "episode04_007_psych_sophia"
    )
define cheat_caress_hand_kate_004 = CheatVariables(
    "Kate",
    "Caress Kate's hand",
    "Didn't caress Kate's hand",
    "caress_hand_kate_004",
    "episode04_007_psych_sophia"
    )
define cheat_marisa_sex_deal_004 = CheatVariables(
    "Marisa",
    "Have sex with Marisa",
    "Didn't have sex with Marisa",
    "marisa_sex_deal_004",
    "episode04_013_coffee_riley_marisa"
    )
define cheat_erika_fool_around_004 = CheatVariables(
    "Erika",
    "Fool around with Erika",
    "Didn't fool around with Erika",
    "erika_fool_around_004",
    "episode04_015_oldtown_goodbye"
    )
define cheat_kiss_harlow_viridian_004 = CheatVariables(
    "Harlow",
    "Kiss Harlow at Viridian",
    "Didn't kiss Harlow at Viridian",
    "kiss_harlow_viridian_004",
    "episode04_019_viridian_meeting_room"
    )
define cheat_kate_be_there_005 = CheatVariables(
    "Kate",
    "Be there for Kate",
    "Don't be there for Kate",
    "kate_be_there_005",
    "episode05_007_dinerkate"
    )
define cheat_kate_hug_diner_005 = CheatVariables(
    "Kate",
    "Hugged Kate at dinner",
    "Didn't hug Kate at Dinner",
    "kate_hug_diner_005",
    "episode05_007_dinerkate"
    )
define cheat_erika_console_bar_005 = CheatVariables(
    "Erika",
    "Consoled Erika",
    "Didn't console Erika",
    "erika_console_bar_005",
    "episode05_009_midtownbar_erika"
    )
define cheat_erika_kiss_midtown_005 = CheatVariables(
    "Erika",
    "Pulled Erika in for a kiss",
    "Didn't pull Erika in for a kiss",
    "erika_kiss_midtown_005",
    "episode05_009_midtownbar_erika"
    )
define cheat_sophia_flirt_coffee_005 = CheatVariables(
    "Sophia",
    "Flirted with Sophia",
    "Didn't flirt with Sophia",
    "sophia_flirt_coffee_005",
    "episode05_010_coffeeshop_sophia"
    )
define cheat_harlow_pinkrabbit_finger_005 = CheatVariables(
    "Harlow",
    "Fingered Harlow at the Pink Rabbit",
    "Didn't finger Harlow at the Pink Rabbit",
    "harlow_pinkrabbit_finger_005",
    "episode05_011_pinkrabbit_tests"
    )
define cheat_billy_impress_vanessa_005 = CheatVariables(
    "Vanessa",
    "Tried to impress Vanessa",
    "Didn't try to impress Vanessa",
    "billy_impress_vanessa_005",
    "episode05_014_coffeeshop_clubprep"
    )
define cheat_vanessa_for_her_005 = CheatVariables(
    "Vanessa",
    "Do it for Vanessa",
    "Didn't do it for Vanessa",
    "vanessa_for_her_005",
    "episode05_015_club_danceoff"
    )
define cheat_vanessa_kiss_club_005 = CheatVariables(
    "Vanessa",
    "Tried to kiss Vanessa",
    "Didn't try to kiss Vanessa",
    "vanessa_kiss_club_005",
    "episode05_015_club_danceoff"
    )
define cheat_marisa_kiss_viridian_005 = CheatVariables(
    "Marisa",
    "Pulled Marisa in for a kiss",
    "Didn't pull Marisa in for a kiss",
    "marisa_kiss_viridian_005",
    "episode05_017_viridian_marisa"
    )
define cheat_erika_sex_oldtown_005 = CheatVariables(
    "Erika",
    "Had some fun with Erika",
    "Didn't have some fun with Erika",
    "erika_sex_oldtown_005",
    "episode05_020_oldtown_outside"
    )
define cheat_stranger_compliment_005 = CheatVariables(
    "Stranger",
    "Complimented Stranger",
    "Didn't compliment Stranger",
    "stranger_compliment_005",
    "episode05_025_viridian_meeting"
    )
define cheat_riley_viridian_date_bet_005 = CheatVariables(
    "Riley",
    "Made a bet with Riley for a date",
    "Didn't make a bet with Riley for a date",
    "riley_viridian_date_bet_005",
    "episode05_025_viridian_meeting"
    )
define cheat_kate_like_riley_005 = CheatVariables(
    "Kate",
    "Told Kate you like Riley",
    "Didn't tell Kate you like Riley",
    "kate_like_riley_005",
    "episode05_025_viridian_meeting"
    )
define kate_viridian_dance_005 = CheatVariables(
    "Kate",
    "Dance with Kate",
    "Didn't dance with Kate",
    "kate_viridian_dance_005",
    "episode05_025_viridian_meeting"
    )
define cheat_kate_dance_close_005 = CheatVariables(
    "Kate",
    "Dance closer to Kate",
    "Didn't dance closer to Kate",
    "kate_dance_close_005",
    "episode05_025_viridian_meeting"
    )
define cheat_kate_flirt_kiss_006 = CheatVariables(
    "Kate",
    "Kissed Kate",
    "Didn't kiss Kate",
    "kate_flirt_kiss_006",
    "episode06_003_psychologyoffice_thesis"
    )
define cheat_harlow_hallway_kiss_006 = CheatVariables(
    "Harlow",
    "Kissed Harlow in the hallway",
    "Didn't kiss Harlow in the hallway",
    "harlow_hallway_kiss_006",
    "episode06_005_chemlab_hallway"
    )
define cheat_vanessa_grace_like_006 = CheatVariables(
    "Grace",
    "Told Grace you like Vanessa",
    "Didn't tell Grace You Like Vanessa",
    "vanessa_grace_like_006",
    "episode06_007_uptown_apexoffice_meeting"
    )
define cheat_grace_flirt_006 = CheatVariables(
    "Grace",
    "Flirted with Grace",
    "Didn't flirt with Grace",
    "grace_flirt_006",
    "episode06_007_uptown_apexoffice_meeting"
    )
define cheat_riley_feed_fry_006 = CheatVariables(
    "Riley",
    "Had Riley feed you a Fry",
    "Didn't have Riley feed you a Fry",
    "riley_feed_fry_006",
    "episode06_008_uptown_midtown_lunchdate_riley"
    )
define cheat_marisa_sex_latenight_006 = CheatVariables(
    "Marisa",
    "Had late night sex with Marisa",
    "Didn't have late night sex with Marisa",
    "marisa_sex_latenight_006",
    "episode06_010_bedroom_latenighttext_marisa"
    )
define cheat_sophia_pretty_costume_006 = CheatVariables(
    "Sophia",
    "Told Sophia she looks pretty in any outfit",
    "Didn't tell Sophia she looks pretty in any outfit",
    "sophia_pretty_costume_006",
    "episode06_012_coffeeshop_invite_sophia"
    )
define cheat_lorelei_flirt_006 = CheatVariables(
    "Lorelei",
    "Flirted with Lorelei",
    "Didn't flirt with Lorelei",
    "lorelei_flirt_006",
    "episode06_013_oldtown_provinggrounds_tournament"
    )
define cheat_jordan_flirt_first_006 = CheatVariables(
    "Jordan",
    "Flirted with Jordan (First Time)",
    "Didn't flirt with Jordan (First Time)",
    "jordan_flirt_first_006",
    "episode06_016_midtown_bar_thesis"
    )
define cheat_jordan_flirt_second_006 = CheatVariables(
    "Jordan",
    "Flirted with Jordan (Second Time)",
    "Didn't flirt with Jordan (Second Time)",
    "jordan_flirt_second_006",
    "episode06_016_midtown_bar_thesis"
    )
define cheat_jordan_sex_006 = CheatVariables(
    "Jordan",
    "Had sex with Jordan",
    "Didn't have sex with Jordan",
    "jordan_sex_006",
    "episode06_016_midtown_bar_thesis"
    )
define cheat_jordan_like_006 = CheatVariables(
    "Jordan",
    "Told Jordan you like her",
    "Didn't tell Jordan you like her",
    "jordan_like_006",
    "episode06_017_midtown_bar_sex_jordan"
    )
define cheat_marisa_promise_006 = CheatVariables(
    "Marisa",
    "Promised Marisa",
    "Didn't promise Marisa",
    "marisa_promise_006",
    "episode06_018_coffee_halloween_party_001_entrances"
    )
define cheat_sophia_flirt_photo_006 = CheatVariables(
    "Sophia",
    "Flirted with Sophia",
    "Didn't flirt with Sophia",
    "sophia_flirt_photo_006",
    "episode06_019_coffee_halloween_party_002_pictures"
    )
define cheat_vanessa_selfie_006 = CheatVariables(
    "Vanessa",
    "Took a selfie with Vanessa",
    "Didn't take a selfie with Vanessa",
    "vanessa_selfie_006",
    "episode06_020_coffee_halloween_party_003_vanessa"
    )
define cheat_vanessa_flirt_006 = CheatVariables(
    "Vanessa",
    "Flirted with Vanessa",
    "Didn't flirt with Vanessa",
    "vanessa_flirt_006",
    "episode06_020_coffee_halloween_party_003_vanessa"
    )
define cheat_sophia_hug_goodbye_006 = CheatVariables(
    "Sophia",
    "Hugged Sophia",
    "Didn't hug Sophia",
    "sophia_hug_goodbye_006",
    "episode06_021_coffee_halloween_party_004_dancing"
    )
define cheat_erika_admit_riley_006 = CheatVariables(
    "Erika",
    "Admitted to Erika you like Riley",
    "Didn't admit to Erika you like Riley",
    "erika_admit_riley_006",
    "episode06_021_coffee_halloween_party_004_dancing"
    )
define cheat_harlow_sex_coffeeshop_006 = CheatVariables(
    "Harlow",
    "Had sex with Harlow",
    "Didn't have sex with Harlow",
    "harlow_sex_coffeeshop_006",
    "episode06_021_coffee_halloween_party_004_dancing"
    )
define cheat_riley_flirt_handshake_006 = CheatVariables(
    "Riley",
    "Handshake flirted with Riley",
    "Didn't handshake flirt with Riley",
    "riley_flirt_handshake_006",
    "episode06_021_coffee_halloween_party_004_dancing"
    )
define cheat_erika_costumes_007 = CheatVariables(
    "Erika",
    "Costume shopping with Erika",
    "No costume shopping with Erika",
    "erika_costumes_007",
    "episode07_006_costume_shop"
    )
define cheat_erika_maid_costume_007 = CheatVariables(
    "Erika",
    "Pictured Erika in Maid costume",
    "Didn't picture Erika in Maid costume",
    "erika_maid_costume_007",
    "episode07_006_costume_shop"
    )
define cheat_erika_apartment_sex_007 = CheatVariables(
    "Erika",
    "Had sex with Erika in her apartment",
    "Didn't have sex with erika in her apartment",
    "erika_apartment_sex_007",
    "episode07_010_apartment_erika_sex"
    )
define cheat_vanessa_bikini_gawk_007 = CheatVariables(
    "Vanessa",
    "Gawked at Vanessa in her Bikini",
    "Didn't gawk at Vanessa in her Bikini",
    "vanessa_bikini_gawk_007",
    "episode07_011_uptown_pool"
    )
define cheat_vanessa_sunscreen_flirt_007 = CheatVariables(
    "Vanessa",
    "Put sunscreen on Vanessa",
    "Didn't put Sunscreen on Vanessa",
    "vanessa_sunscreen_flirt_007",
    "episode07_011_uptown_pool"
    )
define cheat_vanessa_photo_selfie_007 = CheatVariables(
    "Vanessa",
    "Took a photo of Vanessa",
    "Didn't take a photo of Vanessa",
    "vanessa_photo_selfie_007",
    "episode07_011_uptown_pool"
    )
define cheat_vanessa_duo_shirtless_007 = CheatVariables(
    "Vanessa",
    "Attempted sexier pic",
    "Didn't attempt a sexier pic",
    "vanessa_duo_shirtless_007",
    "episode07_011_uptown_pool"
    )
define cheat_harlow_invite_kiss_007 = CheatVariables(
    "Harlow",
    "Fooled around with Harlow",
    "Didn't fool around with Harlow",
    "harlow_invite_kiss_007",
    "episode07_014_funk_burger"
    )
define cheat_kate_flirt_007 = CheatVariables(
    "Kate", 
    "Pursue Kate (Start)", 
    "Don't pursue Kate (Start)", 
    "kate_flirt_007",
    "episode07_017_psych_office"
    )
define cheat_kate_office_sex_007 = CheatVariables(
    "Kate",
    "Fingered Kate in her office",
    "Didn't finger Kate in her office",
    "kate_office_sex_007",
    "episode07_017_psych_office"
    )
define cheat_riley_ask_date_007 = CheatVariables(
    "Riley",
    "Asked Riley on a Date",
    "Didn't ask Riley on a date",
    "riley_ask_date_007",
    "episode07_018_coffee_mission"
    )
define cheat_viridian_007 = CheatVariables(
    "Mc",
    "Cool Stripper Name",
    "Real Stripper Name", 
    ["stripper_cool_name_007", "stripper_real_name_007"],
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_erika_007 = CheatVariables(
    "Erika",
    "Told Erika she is pretty",
    "Didn't tell Erika she is pretty",
    "know_pretty_erika_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_everybody_007 = CheatVariables(
    "Erika",
    "Told Erika everybody is pretty",
    "Didn't tell Erika everybody is pretty",
    "know_pretty_everybody_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_riley_007 = CheatVariables(
    "Erika",
    "Told Erika Riley is pretty",
    "Didn't tell Erika Riley is pretty",
    "know_pretty_riley_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_harlow_007 = CheatVariables(
    "Erika",
    "Told Erika Harlow is pretty",
    "Didn't tell Erika Harlow is pretty",
    "know_pretty_harlow_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_sophia_007 = CheatVariables(
    "Erika",
    "Told Erika Sophia is pretty",
    "Didn't tell Erika Sophia is pretty",
    "know_pretty_sophia_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_marisa_007 = CheatVariables(
    "Erika",
    "Told Erika Marisa is pretty",
    "Didn't tell Erika Marisa is pretty",
    "know_pretty_marisa_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_jordan_007 = CheatVariables(
    "Erika",
    "Told Erika Jordan is pretty",
    "Didn't tell Erika Jordan is pretty",
    "know_pretty_jordan_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_lorelei_007 = CheatVariables(
    "Erika",
    "Told Erika Lorelei is pretty",
    "Didn't tell Erika Lorelei is pretty",
    "know_pretty_lorelei_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_kate_007 = CheatVariables(
    "Erika",
    "Told Erika Kate is pretty",
    "Didn't tell Erika Kate is pretty",
    "know_pretty_kate_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_vanessa_007 = CheatVariables(
    "Erika",
    "Told Erika Vanessa is pretty",
    "Didn't tell Erika Vanessa is pretty",
    "know_pretty_vanessa_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_grace_007 = CheatVariables(
    "Erika",
    "Told Erika Grace is pretty",
    "Didn't tell Erika Grace is pretty",
    "know_pretty_grace_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_know_pretty_stranger_007 = CheatVariables(
    "Erika",
    "Told Erika Stranger is pretty",
    "Didn't tell Erika Stranger is pretty",
    "know_pretty_stranger_007",
    "episode07_020_strip_club_viridian"
    )
define cheat_dance_flirt_stranger_007 = CheatVariables(
    "Stranger",
    "Flirted with Stranger",
    "Didn't flirt with Stranger",
    "dance_flirt_stranger_007",
    "episode07_021_strip_club_private_room"
    )
define cheat_jordan_marisa_threesome_sex_bar_008 = CheatVariables(
    "Jordan",
    "Had a threesome with Jordan",
    "Didn't have a threesome with Jordan",
    "jordan_marisa_threesome_sex_bar_008",
    "episode08_009_midtown_bar_marisa_jordan"
    )
define cheat_jordan_sex_bar_008 = CheatVariables(
    "Jordan",
    "Had sex with Jordan at her bar",
    "Didn't have sex with Jordan at her bar",
    "jordan_sex_bar_008",
    "episode08_009_midtown_bar_marisa_jordan"
    )
define marisa_sex_apartment_008 = CheatVariables(
    "Jordan",
    "Had sex with Marisa at her apartment",
    "Didn't have sex with Marisa at her apartment",
    "marisa_sex_apartment_008",
    "episode08_009_midtown_bar_marisa_jordan"
    )
define cheat_jordan_solo_serious_008 = CheatVariables(
    "Jordan",
    "Dating Jordan solo",
    "Not dating Jordan solo",
    "jordan_solo_serious_008",
    "episode08_012_midtown_bar_sex"
    )
define cheat_riley_flirt_club_008 = CheatVariables(
    "Riley",
    "Flirted with Riley at the club",
    "Didn't flirt with Riley at the club",
    "riley_flirt_club_008",
    "episode08_027_comedy_club_riley"
    )
define cheat_sophia_study_date_008 = CheatVariables(
    "Sophia",
    "Asked Sophia on a study date",
    "Didn't ask Sophia on a study date",
    "sophia_study_date_008",
    "episode08_028_comedy_club_sophia"
    )
define cheat_sophia_sex_first_009 = CheatVariables(
    "Sophia",
    "Had sex with Sophia",
    "Didn't have sex with Sophia",
    "sophia_sex_first_009",
    "episode09_011_alskitchen_outside_sophia"
    )
define cheat_vanessa_shades_flirt_009 = CheatVariables(
    "Vanessa",
    "Flirted with Vanessa shades on",
    "Didn't flirt with Vanessa shades on",
    "vanessa_shades_flirt_009",
    "episode09_019_comedyclub_goodbye"
    )
define cheat_sophia_next_date_010 = CheatVariables(
    "Sophia",
    "Asked Sophia on another date",
    "Didn't ask Sophia on another date",
    "sophia_next_date_010",
    "episode10_008_psychoffice_hallway"
    )
define cheat_riley_dance_date_010 = CheatVariables(
    "Riley",
    "Convinced Riley to go on a date",
    "Didn't convince Riley to go on a date",
    "riley_dance_date_010",
    "episode10_012_newcoffeeshop_rebuild"
    )
define cheat_grace_accept_sex_011 = CheatVariables(
    "Grace",
    "Had sex with Grace",
    "Didn't have sex with Grace",
    "grace_accept_sex_011",
    "episode11_006_uptown_apartment_meeting_grace"
    )
define cheat_lori_first_sex_012 = CheatVariables(
    "Lorelei",
    "Had sex with Lorelei",
    "Didn't have sex with Lorelei",
    "lori_first_sex_012",
    "episode12_020_chargersgym_checkin"
    )
define cheat_irene_hillside_first_sex_013 = CheatVariables(
    "Stranger",
    "Had sex with Stranger",
    "Didn't have sex with Stranger",
    "irene_hillside_first_sex_013",
    "episode13_009_hillside_irene_conversation"
    )
define cheat_vanessa_pineapple_pizza_like_014 = CheatVariables(
    "Vanessa",
    "Told Vanessa you like pineapple on pizza",
    "Didn't tell Vanessa you like pineapple on pizza",
    "vanessa_pineapple_pizza_like_014",
    "episode14_009_pizzadate_vanessa"
    )
define cheat_vanessa_private_shaved_014 = CheatVariables(
    "Vanessa",
    "Quessed pussy fully shaved",
    "Didn't guess pussy fully shaved",
    "vanessa_private_shaved_014",
    "episode14_011_bedroom_vanessa_start"
    )
define cheat_riley_sex_015 = CheatVariables(
    "Riley",
    "Had sex with Riley",
    "Didn't have sex with Riley",
    "riley_sex_015",
    "episode15_009_date_confession"
    )
define cheat_riley_private_trim_015  = CheatVariables(
    "Riley",
    "Armired Riley shaved pussy",
    "Didn't admire Riley shaved pussy",
    "riley_private_trim_015 ",
    "episode15_010_date_hotel_sex"
    )


define cheat_replay_epi001erika01 = CheatVariables(
    "Erika",
    "Replay Erika Episode 1 Unlocked",
    "Replay Erika Episode 1 Locked",
    "persistent.epi001erika01"
    )
define cheat_replay_epi002marisa01 = CheatVariables(
    "Marisa",
    "Replay Marisa Episode 2 Unlocked",
    "Replay Marisa Episode 2 Locked",
    "persistent.epi002marisa01"
    )
define cheat_replay_epi003jordan01 = CheatVariables(
    "Jordan",
    "Replay Jordan Episode 3 Unlocked",
    "Replay Jordan Episode 3 Locked",
    "persistent.epi003jordan01"
    )
define cheat_replay_epi004erika01 = CheatVariables(
    "Erika",
    "Replay Erika Episode 4 Unlocked",
    "Replay Erika Episode 4 Locked",
    "persistent.epi004erika01"
    )
define cheat_replay_epi004harlow01 = CheatVariables(
    "Harlow",
    "Replay Harlow Episode 4 Unlocked",
    "Replay Harlow Episode 4 Locked",
    "persistent.epi004harlow01"
    )
define cheat_replay_epi004marisa01 = CheatVariables(
    "Marisa",
    "Replay Marisa Episode 4 Unlocked",
    "Replay Marisa Episode 4 Locked",
    "persistent.epi004marisa01"
    )
define cheat_replay_epi005harlow01 = CheatVariables(
    "Harlow",
    "Replay Harlow Episode 5 Unlocked",
    "Replay Harlow Episode 5 Locked",
    "persistent.epi005harlow01"
    )
define cheat_replay_epi005erika01 = CheatVariables(
    "Erika",
    "Replay Erika Episode 5 Unlocked",
    "Replay Erika Episode 5 Locked",
    "persistent.epi005erika01"
    )
define cheat_replay_epi006marisa01 = CheatVariables(
    "Marisa",
    "Replay Marisa Episode 6 Unlocked",
    "Replay Marisa Episode 6 Locked",
    "persistent.epi006marisa01"
    )
define cheat_replay_epi006jordan01 = CheatVariables(
    "Jordan",
    "Replay Jordan Episode 6 Unlocked",
    "Replay Jordan Episode 6 Locked",
    "persistent.epi006jordan01"
    )
define cheat_replay_epi006harlow01 = CheatVariables(
    "Harlow",
    "Replay Harlow Episode 6 Unlocked",
    "Replay Harlow Episode 6 Locked",
    "persistent.epi006harlow01"
    )
define cheat_replay_epi007erika01 = CheatVariables(
    "Erika",
    "Replay Erika Episode 7 Unlocked",
    "Replay Erika Episode 7 Locked",
    "persistent.epi007erika01"
    )
define cheat_replay_epi007harlow01 = CheatVariables(
    "Harlow",
    "Replay Harlow Episode 7 Unlocked",
    "Replay Harlow Episode 7 Locked",
    "persistent.epi007harlow01"
    )
define cheat_replay_epi007kate01 = CheatVariables(
    "Kate",
    "Replay Kate Episode 7 Unlocked",
    "Replay Kate Episode 7 Locked",
    "persistent.epi007kate01",
    )
define cheat_replay_epi008threesome01_jordan = CheatVariables(
    "Jordan",
    "Replay Marisa/Jordan Episode 8 Unlocked",
    "Replay Marisa/Jordan Episode 8 Locked",
    "persistent.epi008threesome01"
    )
define cheat_replay_epi008threesome01_marisa = CheatVariables(
    "Marisa",
    "Replay Marisa/Jordan Episode 8 Unlocked",
    "Replay Marisa/Jordan Episode 8 Locked",
    "persistent.epi008threesome01"
    )
define cheat_replay_epi008jordan01 = CheatVariables(
    "Jordan",
    "Replay Jordan Episode 8 Unlocked",
    "Replay Jordan Episode 8 Locked",
    "persistent.epi008jordan01"
    )
define cheat_replay_epi008marisa01 = CheatVariables(
    "Marisa",
    "Replay Marisa Episode 8 Unlocked",
    "Replay Marisa Episode 8 Locked",
    "persistent.epi008marisa01"
    )
define cheat_replay_epi008kate01 = CheatVariables(
    "Kate",
    "Replay Kate Episode 8 Unlocked",
    "Replay Kate Episode 8 Locked",
    "persistent.epi008kate01",
    )
define cheat_replay_epi009erika01 = CheatVariables(
    "Erika",
    "Replay Erika Episode 9 Unlocked",
    "Replay Erika Episode 9 Locked",
    "persistent.epi009erika01"
    )
define cheat_replay_epi009harlow01 = CheatVariables(
    "Harlow",
    "Replay Harlow Episode 9 Unlocked",
    "Replay Harlow Episode 9 Locked",
    "persistent.epi009harlow01"
    )
define cheat_replay_epi009sophia01 = CheatVariables(
    "Sophia",
    "Replay Sophia Episode 9 Unlocked",
    "Replay Sophia Episode 9 Locked",
    "persistent.epi009sophia01"
    )
define cheat_replay_epi010marisa01 = CheatVariables(
    "Marisa",
    "Replay Marisa Episode 10 Unlocked",
    "Replay Marisa Episode 10 Locked",
    "persistent.epi010marisa01"
    )
define cheat_replay_epi010harlow01 = CheatVariables(
    "Harlow",
    "Replay Harlow Episode 10 Unlocked",
    "Replay Harlow Episode 10 Locked",
    "persistent.epi010harlow01"
    )
define cheat_replay_epi011kate01 = CheatVariables(
    "Kate",
    "Replay Kate Episode 11 Unlocked",
    "Replay Kate Episode 11 Locked",
    "persistent.epi011kate01",
    )
define cheat_replay_epi011grace01 = CheatVariables(
    "Grace",
    "Replay Grace Episode 11 Unlocked",
    "Replay Grace Episode 11 Locked",
    "persistent.epi011grace01"
    )
define cheat_replay_epi012erika01 = CheatVariables(
    "Erika",
    "Replay Erika Episode 12 Unlocked",
    "Replay Erika Episode 12 Locked",
    "persistent.epi012erika01"
    )
define cheat_replay_epi012lorelei01 = CheatVariables(
    "Lorelei",
    "Replay Lorelei Episode 12 Unlocked",
    "Replay Lorelei Episode 12 Locked",
    "persistent.epi012lorelei01"
    )
define cheat_replay_epi013sophia01 = CheatVariables(
    "Sophia",
    "Replay Sophia Episode 13 Unlocked",
    "Replay Sophia Episode 13 Locked",
    "persistent.epi013sophia01"
    )
define cheat_replay_epi013marisa01 = CheatVariables(
    "Marisa",
    "Replay Marisa Episode 13 Unlocked",
    "Replay Marisa Episode 13 Locked",
    "persistent.epi013marisa01"
    )
define cheat_replay_epi013irene01 = CheatVariables(
    "Stranger",
    "Replay Stranger Episode 13 Unlocked",
    "Replay Stranger Episode 13 Locked",
    "persistent.epi013irene01"
    )
define cheat_replay_epi013kate01 = CheatVariables(
    "Kate",
    "Replay Kate Episode 13 Unlocked",
    "Replay Kate Episode 13 Locked",
    "persistent.epi013kate01",
    )
define cheat_replay_epi013harlowfix01 = CheatVariables(
    "Harlow",
    "Replay Harlow Episode 13 Unlocked",
    "Replay Harlow Episode 13 Locked",
    "persistent.epi013harlowfix01"
    )
define cheat_replay_epi014vanessa01 = CheatVariables(
    "Vanessa",
    "Replay Vanessa Episode 14 Unlocked",
    "Replay Vanessa Episode 14 Locked",
    "persistent.epi014vanessa01"
    )
define cheat_replay_epi015riley01 = CheatVariables(
    "Riley",
    "Replay Riley Episode 15 Unlocked",
    "Replay Riley Episode 15 Locked",
    "persistent.epi015riley01"
    )








