init 5:# Screens

    screen notice():
        style_prefix "shortcuts"
        zorder 300
        if disable_saves:
            textbutton "?" action Show("save_blocked"),With(dissolve) yalign 0.98 xalign 0.98 text_size gui.text_size*2 at choice_Q

    screen save_blocked():
        style_prefix "shortcuts"
        zorder 300
        modal True
        add Solid ("#000") alpha .9
        textbutton "?" action Hide("save_blocked"),With(dissolve) yalign 0.98 xalign 0.98 text_size gui.text_size*2
        vbox:
            align (0.5, 0.5)
            text _("Saving is temporarily blocked as your are viewing a modified script.") align (0.5, 0.5) color "#FFF" text_align 0.5
            text _("Once the '?' disappears saving will be enabled again.") align (0.5, 0.5) color "#FFF" text_align 0.5
            text _("Will revert back shortly.") align (0.5, 0.5) color "#FFF" text_align 0.5
        button action Hide("save_blocked"),With(dissolve)
        key "game_menu" action Hide("save_blocked"),With(dissolve)

    screen navigation():

        vbox:
            style_prefix "navigation"
            xpos gui.navigation_xpos

            yalign 0.5

            spacing gui.navigation_spacing

            if main_menu:

                textbutton _("New Game") action Start()

            else:

                textbutton _("History") action ShowMenu("history")

                textbutton _("Save"):
                    if not disable_saves:
                        action ShowMenu("save")

            textbutton _("Load Game") action ShowMenu("load")

            textbutton _("Preferences") action ShowMenu("preferences")

            if JGSLoadable("music_room") and JGSLoadable("music_room_screen"):
                textbutton _("Music") action ShowMenu("musicroom")

            textbutton _("Music Credits") action ShowMenu("creditsmusic")

            if not _in_replay:
                textbutton _("Scene Gallery") action ShowMenu("replayGallery")

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("Main Menu") action MainMenu()

            # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                ## Help isn't necessary or relevant to mobile devices.
                # textbutton _("Help") action ShowMenu("help")

            if renpy.variant("pc"):

                ## The quit button is banned on iOS and unnecessary on Android and
                ## Web.
                textbutton _("Exit Game") action Quit(confirm=not main_menu)

    screen main_menu():
        use mod_check()
        $ tooltip = GetTooltip()

        tag menu

        style_prefix "main_menu"

        add gui.main_menu_background

        frame:
            pass

        use navigation

        # Patreon button
        imagebutton:
            idle "gui/patreon.png"
            hover "gui/patreonhover.png"
            action OpenURL("https://www.patreon.com/venuswaltz")
            xalign 0.00
            yalign 0.95

        # Subscribestar button
        imagebutton:
            idle "gui/subscribestar.png"
            hover "gui/subscribestarhover.png"
            action OpenURL("https://subscribestar.adult/venuswaltz")
            xalign 0.00
            yalign 0.80
        
        $ mod_version = "Mod Compatible" if gui.jg_mod_version == config.version else "Mod Incompatible"
        vbox:
            xalign 1.0
            yalign 0.05
            text "{u}[jg_1]JiG[jg_3][jg_2]SaW[jg_3]{/u}\nMOD Installed":
                size gui.mod_info_size
                outlines [(2, "#fff9", 1, 1)]
                text_align 0.5
                font "mod/CM-Font.otf"

            textbutton "Mod Features":
                xalign 1.0
                text_size gui.text_size
                text_outlines [(2, "#0009", 1, 1)]
                text_align 1.0
                action ShowMenu("mod_features")
                tooltip "Click me to view mod features"
    
            if mod_updated[0] not in ["Mod up-to-date", "JSON Error", "Could Not Connect to Host", "HTTP Error", "Timeout", "Request Error", "None"]:
                textbutton ("%s"%"Update Available" if mod_updated[0] != "Game Version Newer Than Mod" else "Check for updated mod"):
                    xalign 1.0
                    text_size gui.text_size
                    text_outlines [(2, "#0009", 1, 1)]
                    text_align 1.0
                    action OpenURL(gui.mod_update_url)
                    tooltip "Click me to get updated mod"
                if mod_changelog:
                    textbutton "Mod Changelog":
                        xalign 1.0
                        text_size gui.text_size
                        text_outlines [(2, "#0009", 1, 1)]
                        text_align 1.0
                        action ShowMenu("mod_changelog")
                        tooltip "View Mod Changelog"

        if tooltip:
            ## Use With Renpy Version Below 7.5 and 8.0
            frame:
                style_prefix "tooltip"
                hbox:
                    text tooltip
            ## Use With Renpy Version Above 7.5 and 8.0
            #nearrect:
            #    focus "tooltip"
            #    prefer_top True
            #    frame:
            #        at choice_appear(.5)
            #        style_prefix "tooltip"
            #        hbox:
            #            text tooltip

    screen say(who, what, slow_effect=persistent._slow_effect, slow_effect_delay=persistent._effect_delay, always_effect=persistent._always_effect):
        style_prefix "say"

        window:
            id "window"
            
            if persistent._textbox_visible and who:
                background Transform(Frame(gui.textbox_location),
                    alpha=persistent._textbox_alpha,
                    xysize=(config.screen_width, gui.textbox_height))
            else:
                background None
            
            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    
                    text who:
                        id "who"
                        if persistent._fancy_text:
                            slow_effect slow_effect
                            slow_effect_delay slow_effect_delay
                            always_effect always_effect

            text what:
                id "what"
                if persistent._fancy_text:
                    slow_effect slow_effect
                    slow_effect_delay slow_effect_delay
                    always_effect always_effect

        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.
        if not renpy.variant("small") and what != "" and what != None:
            add Transform(SideImage(), alpha=1.0) xalign 0.01 yalign 0.99 #DLD Side

    screen shortcuts():
        style_prefix "shortcuts"
        zorder 300
        default shown = False
        default show_button = False

        mousearea:
            align (1.0, 0.05)
            xysize (gui.text_size,gui.text_size)
            hovered SetLocalVariable("show_button", True),With(dissolve)
            unhovered SetLocalVariable("show_button", False),With(dissolve)

        if shown:
            button:
                padding (0,0,0,0)
                add "#000" alpha .9
                add "splashText"
                xysize (config.screen_width, config.screen_height)
                action SetLocalVariable("shown", False),With(dissolve)
            key "game_menu" action SetLocalVariable("shown", False),With(dissolve)

            text "Click anywhere to close or the ? button" align (0.98, 0.98)

        if show_button:
            textbutton "?" action ToggleLocalVariable("shown"),With(dissolve) align (1.0, 0.05)

    screen mod_changelog():
        $ tooltip = GetTooltip()
        tag menu

        use game_menu("Mod Changelog", scroll="viewport"):
            vbox:
                spacing 10
                for i in mod_changelog:
                    text "%s"%i

    screen mod_check():
        timer 600 action SetVariable("mod_updated", get_latest_mod()) repeat True
        
    screen mod_features():
        $ tooltip = GetTooltip()
        tag menu

        use game_menu("Mod Features", scroll="viewport"):
            vbox:
                spacing 10
                if gui.jg_mod_version == config.version:
                    use mod_options_text
                else:
                    text "Mod is outdated {a=gui.mod_update_url}Click Here{/a} to Check for New Version"
                    text "Most mod options will work"
                    text ""
                    use mod_options_text
                    
        if tooltip:
            ## Use With Renpy Version Below 7.5 and 8.0
            frame:
                style_prefix "tooltip"
                hbox:
                    text tooltip
            ## Use With Renpy Version Above 7.5 and 8.0
            #nearrect:
            #    focus "tooltip"
            #    prefer_top True
            #    frame:
            #        at choice_appear(.5)
            #        style_prefix "tooltip"
            #        hbox:
            #            text tooltip

    screen mod_options_text():
        text "Report any issues you find with the mod {a=[gui.mod_issues]}Here{/a}" tooltip "Github issues tracker"
        text "Walkthrough"
        text "1. Walkthrough Suggestions Toggled using {a=#:None}{color=#f00}(W){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "2. Walkthrough Tooltips Toggled using {a=#:None}{color=#f00}(Shift+T){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        if JGSLoadable("music_room") and JGSLoadable("music_room_screen"):
            text "Music Player"
            text "1. Music Player can be Toggled ingame using {a=#:None}{color=#f00}(M){/color}{/a}" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
            text "2. Hovering over Volume Slider allows mousewheel up/down control" xoffset 50
            text "NOTICE: I have created the music room with the music featured in [config.name]. I do not have the actual track names and artists. If you can match an artist and title to a track, open an issue {a=[gui.mod_issues]}Here{/a}" tooltip "Github issues tracker"
            null height 20
        text "Say Dialogue"
        text "1. Fancy Text Toggled using {a=#:None}{color=#f00}(F){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "2. Text Effect Toggled using {a=#:None}{color=#f00}(E){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "3. Text Always Effect Toggled using {a=#:None}{color=#f00}(R){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "Credit to {a=https://github.com/yukinogatari/Ren-Py-FancyText}yukinogatari{/a} for the original Fancytext Module Modified by\n[gui.mod_dev] for newer Ren'Py Compatibility" xoffset 50 tooltip "yukinogatari Github"
        text "Custom Save Names"
        text "1. Toggle Custom Savenames using {a=#:None}{color=#f00}(Shift+S){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "Hotkeys"
        text "1. Toggle Choice Hotkeys using {a=#:None}{color=#f00}(C){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "2. Hotkeys on Choice Menus using {a=#:None}{color=#f00}(1-9 or NUM 1-9){/color}{/a}" xoffset 50 tooltip "1-9 or NUM 1-9 on choice menus"
        text "3. Hotkeys on Confirm using {a=#:None}{color=#f00}(Y/N){/color}{/a}" xoffset 50 tooltip "Y/N on confirmation screens"
        text "Notifications"
        text "1. Toggle Notification Stack/Standard using {a=#:None}{color=#f00}(N){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "Replays"
        text "1. Rebuilt the way the replays screen is presented to you. Can replay locked scenes without affecting your progress" xoffset 50
        text "2. Added a navigation menu to filter by Episode or Character" xoffset 50
        text "Credit to {a=https://github.com/RenpyRemix/multi-notify}RenpyRemix{/a} for stackable notifications" xoffset 50 tooltip "RenpyRemix Github"
        text "Credit to {a=https://github.com/valery-iwanofu/renpy-shader-collection}valery-iwanofu{/a} for color picker" xoffset 50 tooltip "valery-iwanofu Github"
        null height 30
        if mod_updated[0] not in ["Mod up-to-date", "JSON Error", "Could Not Connect to Host", "HTTP Error", "Timeout", "Request Error", "None"]:
            text "Latest MOD update available at {a=[gui.mod_update_url]}[gui.mod_dev]{/a}" tooltip "Mod Developer"
        text _("If you like what I do consider {a=[gui.donate_mod]}Buying me a beer{/a}") tooltip _("Mod Developer BuyMeACoffee Page")
        text "And lastly {a=[gui.developer_support]}[gui.developer_name]{/a} for developing [config.name!t]" tooltip "Developer Patreon"

    screen confirm(message, yes_action, no_action):

        ## Ensure other screens do not get input while this screen is displayed.
        modal True

        zorder 200

        style_prefix "confirm"

        add "gui/overlay/confirm.png"

        frame:

            vbox:
                xalign .5
                yalign .5
                spacing 45

                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 150

                    textbutton (_("Yes") if not persistent._choice_hotkeys else _("(Y)es")) action yes_action
                    textbutton (_("No") if not persistent._choice_hotkeys else _("(N)o")) action no_action

        ## Right-click and escape answer "no".
        key "game_menu" action no_action
        if persistent._choice_hotkeys:
            key "K_y" action yes_action
            key "K_n" action no_action

    screen game_menu(title, scroll=None, yinitial=0.0):

        style_prefix "game_menu"

        if main_menu:
            add gui.main_menu_background
        else:
            add gui.game_menu_background

        frame:
            style "game_menu_outer_frame"

            hbox:

                ## Reserve space for the navigation section.
                frame:
                    style "game_menu_navigation_frame"

                frame:
                    style "game_menu_content_frame"

                    if scroll == "viewport":

                        viewport:
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            vbox:
                                transclude

                    elif scroll == "vpgrid":

                        vpgrid:
                            cols 1
                            yinitial yinitial

                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            transclude

                    else:

                        transclude

        use navigation

        textbutton _("Return"):
            style "return_button"
            if title == "Walkthrough Colors":
                action Hide("color_picker_wt", transition=dissolve)
            elif title == "Music Player Settings":
                action Hide("color_picker_mr", transition=dissolve)
            else:
                action Return()

        label title

        if main_menu:
            key "game_menu":
                if title == "Walkthrough Colors":
                    action Hide("color_picker_wt", transition=dissolve)
                elif title == "Music Player Settings":
                    action Hide("color_picker_mr", transition=dissolve)
                else:
                    action ShowMenu("main_menu")
        else:
            if title == "Walkthrough Colors":
                key "game_menu" action Hide("color_picker_wt", transition=dissolve)
            elif title == "Music Player Settings":
                key "game_menu" action Hide("color_picker_mr", transition=dissolve)
            else:
                key "game_menu" action Return()

    screen preferences():

        tag menu

        use game_menu(_("Preferences"), scroll="viewport"):

            vbox:

                hbox:
                    box_wrap True

                    if renpy.variant("pc") or renpy.variant("web"):

                        vbox:
                            style_prefix "radio"
                            label _("Display\n[jg_s]")
                            textbutton _("Window"):
                                action Preference("display", "window")
                            textbutton _("Fullscreen"):
                                action Preference("display", "fullscreen")

                    vbox:
                        style_prefix "check"
                        label _("Skip\n[jg_s]")
                        textbutton _("Unseen Text"):
                            action Preference("skip", "toggle")
                        textbutton _("After Choices"):
                            action Preference("after choices", "toggle")
                        textbutton _("Transitions"):
                            action InvertSelected(Preference("transitions", "toggle"))

                    vbox:
                        style_prefix "radio"
                        label _("Label Overrides\n[jg_s]")
                        textbutton _("Enable"):
                            action LabelOverrides(True, True) selected persistent._use_overrides
                        textbutton _("Disable"):
                            action LabelOverrides(False, True) selected not persistent._use_overrides
                            
                    vbox:
                        style_prefix "check"
                        label _("Fancy Text\n[jg_s](Shift+F)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_fancy_text", True),SetField(preferences, "text_cps", 120)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_fancy_text", False),SetField(preferences, "text_cps", 0)
                    ## Additional vboxes of type "radio_pref" or "check_pref" can be
                    ## added here, to add additional creator-defined preferences.

                null height (4 * gui.pref_spacing)

                if persistent._fancy_text:
                    hbox:
                        box_wrap True
                        

                        
                        vbox:
                            style_prefix "check"
                            label _("Effect\n[jg_s](E)")
                            textbutton _("[persistent._slow_effect_title]"):
                                action SlowEffectChange(True)

                        vbox:
                            style_prefix "check"
                            label _("Always Effect\n[jg_s](R)")
                            textbutton _("[persistent._always_effect_title]"):
                                action AlwaysEffectChange(True)

                        vbox:
                            style_prefix "slider"
                            label _("Effect Delay:\n[jg_s]%s Seconds"%EffectDelayDisplay())

                            bar:
                                value FieldValue(persistent, "_effect_delay",
                                    range=1.0,
                                    style="slider",
                                    max_is_zero=False,
                                    step=.1,
                                    force_step=True)

                            textbutton _("Default"):
                                action SetField(persistent, "_effect_delay", 0.2)

                    null height (4 * gui.pref_spacing)

                hbox:#QM
                    box_wrap True
                    vbox:
                        style_prefix "check"
                        label _("Quick Menu\n[jg_s]Position (Shift+Q)")
                        textbutton _("{size=-10}%s{/size}"%QuickPositions()):
                            action CycleQuickMenu(True)

                    vbox:
                        style_prefix "check"
                        label _("Quick Menu\n[jg_s]State (Q)")
                        textbutton _("{size=-10}[persistent._quick_menu_state!c]{/size}"):
                                action CycleQuickStates(True)

                    vbox:
                        style_prefix "check"
                        label _("Quick Menu\n[jg_s]")
                        textbutton _("{size=-10}Customize{/size}"):
                            action Show("customize_quick", dissolve)

                    vbox:
                        style_prefix "check"
                        label _("Notifications\n[jg_s](N)")
                        textbutton _("{size=-10}%s{/size}"%("Notification Stack" if persistent._notify_custom else "Notification Standard")):
                            action ToggleField(persistent, "_notify_custom")

                null height (4 * gui.pref_spacing)

                hbox:#WT
                    box_wrap True
                    vbox:
                        style_prefix "check"
                        label _("Walkthrough\n[jg_s](W)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_walkthrough", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_walkthrough", False)
                    if persistent._walkthrough:
                        vbox:
                            style_prefix "check"
                            label _("Choice Hints\n[jg_s](Shift+T)")
                            textbutton _("Enabled"):
                                action SetField(persistent, "_choice_tooltips", True)
                            textbutton _("Disabled"):
                                action SetField(persistent, "_choice_tooltips", False)
                        vbox:
                            style_prefix "check"
                            label _("Adjust WT Colors\n[jg_s]")
                            textbutton _("Change") action Show("color_picker_wt", transition=dissolve)
                    vbox:
                        style_prefix "check"
                        label _("Choice Hotkeys\n[jg_s](C)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_choice_hotkeys", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_choice_hotkeys", False)

                null height (4 * gui.pref_spacing)

                hbox:
                    box_wrap True
                    vbox:
                        style_prefix "check"
                        label _("Textbox\n[jg_s](T)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_textbox_visible", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_textbox_visible", False)
                    if JGSLoadable("music_room") and JGSLoadable("music_room_screen"):
                        vbox:
                            style_prefix "check"
                            label _("Music Overlay\n[jg_s]{}".format("On" if persistent._music_overlay else "Off"))
                            textbutton _("On"):
                                action SetField(persistent, "_music_overlay", True)
                            textbutton _("Off"):
                                action SetField(persistent, "_music_overlay", False)
                    vbox:
                        style_prefix "check"
                        label _("Support Mod\n[jg_s]{}".format("On" if persistent._support_mod_display else "Off"))
                        textbutton _("On"):
                            action SetField(persistent, "_support_mod_display", True)
                        textbutton _("Off"):
                            action SetField(persistent, "_support_mod_display", False)
                    vbox:
                        style_prefix "check"
                        label _("Savename\n[jg_s](Shift+S)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_custom_savename", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_custom_savename", False)

                null height (4 * gui.pref_spacing)

                hbox:
                    style_prefix "slider"
                    box_wrap True

                    vbox:
                        if persistent._textbox_visible:
                            label _("Textbox Opacity:\n[jg_s]%s"%TextBoxAlpha())

                            bar:
                                value FieldValue(persistent, "_textbox_alpha",
                                    range=1.0,
                                    style="slider",
                                    max_is_zero=False,
                                    step=.01,
                                    force_step=True)

                        label _("Text Speed:\n[jg_s]%s"%TextSpeed())

                        bar:
                            value Preference("text speed")

                        label _("Auto-Forward Time:\n[jg_s]%s"%AutoForwardTime())

                        bar:
                            value Preference("auto-forward time")

                    vbox:

                        label _("Background Music Volume:\n[jg_s]%s"%VolumeDisplay('backgroundmusic'))
                        hbox:
                            bar value MixerValue('backgroundmusic')

                        if config.has_music:
                            label _("Animation / Main Menu Volume:\n[jg_s]%s"%VolumeDisplay('music'))

                            hbox:
                                bar:
                                    value Preference("music volume")

                        if config.has_sound:

                            label _("Sound Volume:\n[jg_s]%s"%VolumeDisplay('sfx'))

                            hbox:
                                bar:
                                    value Preference("sound volume")

                                if config.sample_sound:
                                    textbutton _("Test"):
                                        action Play("sound", config.sample_sound)

                        if config.has_voice:
                            label _("Voice Volume:\n[jg_s]%s"%VolumeDisplay('voice'))

                            hbox:
                                bar:
                                    value Preference("voice volume")

                                if config.sample_voice:
                                    textbutton _("Test"):
                                        action Play("voice", config.sample_voice)

                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing

                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"

    screen color_picker_wt():
        default activate = False
        default option = ""
        default field = ""
        use game_menu("Walkthrough Colors"):
            vbox:
                hbox:#Good Choice
                    spacing 15
                    vbox:
                        textbutton "Good Choice Color":
                            
                            action If(option == "_good_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_good_choice_color"), SetScreenVariable("field", "_good_choice_color")])
                            text_color persistent._good_choice_color
                            text_hover_color adjust_brightness(persistent._good_choice_color, -50)
                    vbox:
                        textbutton "Reset":
                            action SetField(persistent, "_good_choice_color", persistent._default_good_choice_color) 
                            sensitive persistent._good_choice_color != persistent._default_good_choice_color
                hbox:#Bad Choice
                    spacing 15
                    vbox:
                        textbutton "Bad Choice Color":
                            action If(option == "_bad_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_bad_choice_color"), SetScreenVariable("field", "_bad_choice_color")])
                            text_color persistent._bad_choice_color
                            text_hover_color adjust_brightness(persistent._bad_choice_color, -50)
                    vbox:
                        textbutton "Reset":
                            action SetField(persistent, "_bad_choice_color", persistent._default_bad_choice_color) 
                            sensitive persistent._bad_choice_color != persistent._default_bad_choice_color
                hbox:#Recommended Choice
                    spacing 15
                    vbox:
                        textbutton "Recommended Choice Color":
                            action If(option == "_recommended_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")],  
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_recommended_choice_color"), SetScreenVariable("field", "_recommended_choice_color")])
                            text_color persistent._recommended_choice_color
                            text_hover_color adjust_brightness(persistent._recommended_choice_color, -50)
                    vbox:
                        textbutton "Reset":
                            action SetField(persistent, "_recommended_choice_color", persistent._default_recommended_choice_color) 
                            sensitive persistent._recommended_choice_color != persistent._default_recommended_choice_color
                hbox:#Best Choice
                    spacing 15
                    vbox:
                        textbutton "Best Choice Color":
                            action If(option == "_best_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_best_choice_color"), SetScreenVariable("field", "_best_choice_color")])
                            text_color persistent._best_choice_color
                            text_hover_color adjust_brightness(persistent._best_choice_color, -50)
                    vbox:
                        textbutton "Reset":
                            action SetField(persistent, "_best_choice_color", persistent._default_best_choice_color) 
                            sensitive persistent._best_choice_color != persistent._default_best_choice_color
                hbox:#Dealers Choice
                    spacing 15
                    vbox:
                        textbutton "Good Choice Color":
                            action If(option == "_dealers_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_dealers_choice_color"), SetScreenVariable("field", "_dealers_choice_color")])
                            text_color persistent._dealers_choice_color
                            text_hover_color adjust_brightness(persistent._dealers_choice_color, -50)
                    vbox:
                        textbutton "Reset":
                            action SetField(persistent, "_dealers_choice_color", persistent._default_dealers_choice_color) 
                            sensitive persistent._dealers_choice_color != persistent._default_dealers_choice_color

            if activate:
                use color_picker(FieldSimpleValue(persistent,option), field)

    screen quick_menu():

        ## Ensure this appears on top of other screens.
        zorder 100
        default quick_hover = False
        style_prefix "quick"
        if quick_menu:
            if persistent._quick_menu_state == "visible":
                use quick_layout
            elif persistent._quick_menu_state == "hover":
                use quick_mouse
                if quick_hover:
                    use quick_layout
                else:
                    use quick_hover

    screen quick_hover():
        $ qp = persistent._quick_menu_layout
        if persistent._quick_menu_layout in ["bottom_center", "top_center"]:
            hbox:
                xalign 0.5
                style_prefix "quick_menu_%s"%persistent._quick_menu_layout
                text "···"

    screen quick_layout:
        if persistent._quick_menu_layout in ["bottom_center", "top_center"]:
            hbox:
                style_prefix "quick_menu_%s"%persistent._quick_menu_layout
                use quick_menu_buttons

    screen quick_mouse():
        if persistent._quick_menu_layout == "bottom_center":
            mousearea:
                align (0.5,1.0)
                xysize (config.screen_width, gui.text_size)
                hovered ToggleScreenVariable("quick_hover", True),With(dissolve)
                unhovered ToggleScreenVariable("quick_hover", False),With(dissolve)

        if persistent._quick_menu_layout == "top_center":
            mousearea:
                align (0.5,0.0)
                xysize (config.screen_width, gui.text_size)
                hovered ToggleScreenVariable("quick_hover", True),With(dissolve)
                unhovered ToggleScreenVariable("quick_hover", False),With(dissolve)

    screen quick_menu_buttons():
        if persistent._quickmenu_rollback:
            textbutton _("Back"):
                action Rollback()
        if persistent._quickmenu_history:
            textbutton _("History"):
                action ShowMenu('history')
        if persistent._quickmenu_skip:
            textbutton _("Skip"):
                action Skip() alternate Skip(fast=True, confirm=True)
        if persistent._quickmenu_auto:
            textbutton _("Auto"):
                action Preference("auto-forward", "toggle")
        if persistent._quickmenu_save:
            textbutton _("Save"):
                if not disable_saves:
                    action ShowMenu('save')
        if persistent._quickmenu_hide:
            textbutton _("Hide"):
                action HideInterface()
        if persistent._quickmenu_qsave:
            textbutton _("Q.Save"):
                if not disable_saves:
                    action QuickSave()
        if persistent._quickmenu_qload:
            textbutton _("Q.Load"):
                action QuickLoad()
        if persistent._quickmenu_prefs:
            textbutton _("Prefs"):
                action ShowMenu('preferences')
        if persistent._quickmenu_show_menu:
            textbutton _("Menu"):
                action ShowMenu()
        if not _in_replay:
            textbutton _("Cheats"):
                action ShowMenu('cheatmod')
        
        if _in_replay:
            if persistent._quickmenu_end_replay:
                textbutton _("End Replay"):
                    action EndReplay(confirm=True)

    default persistent._quickmenu_rollback = True
    default persistent._quickmenu_history = True
    default persistent._quickmenu_skip = True
    default persistent._quickmenu_auto = True
    default persistent._quickmenu_save = True
    default persistent._quickmenu_hide = True
    default persistent._quickmenu_qsave = True
    default persistent._quickmenu_qload = True
    default persistent._quickmenu_prefs = True
    default persistent._quickmenu_end_replay = True
    default persistent._quickmenu_show_menu = True
    
    screen customize_quick():
        modal True
        add Solid("#000") alpha .9
        vbox:
            align (0.5, 0.5)
            hbox:
                style_prefix "quick_toggles"
                align (0.5,0.5)
                spacing 40
                textbutton _("Back"):
                    action ToggleField(persistent, "_quickmenu_rollback")
                textbutton _("History"):
                    action ToggleField(persistent, "_quickmenu_history")
                textbutton _("Skip"):
                    action ToggleField(persistent, "_quickmenu_skip")
                textbutton _("Auto"):
                    action ToggleField(persistent, "_quickmenu_auto")
                textbutton _("Save"):
                    action ToggleField(persistent, "_quickmenu_save")
                textbutton _("Hide"):
                    action ToggleField(persistent, "_quickmenu_hide")
                textbutton _("Q.Save"):
                    action ToggleField(persistent, "_quickmenu_qsave")
                textbutton _("Q.Load"):
                    action ToggleField(persistent, "_quickmenu_qload")
                textbutton _("Prefs"):
                    action ToggleField(persistent, "_quickmenu_prefs")
                textbutton _("Menu"):
                    action ToggleField(persistent, "_quickmenu_show_menu")
                textbutton _("End Replay"):
                    action ToggleField(persistent, "_quickmenu_end_replay")

        textbutton "Close" action Hide("customize_quick", dissolve) align (0.98,0.98)

    style quick_toggles_button_text:
        color "#F00"
        selected_color "#0F0"
        hover_color gui.hover_color
        selected_hover_color gui.hover_color

    transform choice_Q():
        easein .5 alpha 0.0
        pause .25
        easein .5 alpha 1.0
        repeat 4

    screen choice(items):
        style_prefix get_prefix_choice()
        $ tooltip = GetTooltip()
        default walkthrough = ""
        default hint = ""
        default shown = True
        default animate = True

        timer 6 action SetLocalVariable("shown", False),SetLocalVariable("animate", False),With(dissolve)

        default operators = {
            "<=" : operator.le,   # less than or equal to
            "<"  : operator.lt,   # less than
            ">"  : operator.gt,   # greater than
            ">=" : operator.ge,   # greater than or equal to
            "==" : operator.eq,   # equal tom
            "!=" : operator.ne,   # not equal
            }
        mousearea:
            align 0.0, 0.0
            xysize (50,50)
            hovered SetLocalVariable("shown", True),With(dissolve)
            unhovered SetLocalVariable("shown", False),With(dissolve)
        if shown:
            textbutton "?":
                if animate:
                    at choice_Q 
                action NullAction() 
                tooltip wt_choice_tooltip
                style "_default"
                text_style "_default"
                text_size 50
                text_outlines [(2, "#0009", 1, 1)]
                text_color "#FFFFFFA3"

        vbox:
            for count, i in enumerate(items, 1):
                $ menu_hack(renpy.get_filename_line())
                $ _choice_wt = ""
                $ _choice_hint = ""
                $ _choice_color = gui.text_color
                $ _choice_size = gui.text_size
                if renpy.loadable("mod/walkthrough.rpy"):
                    $ _choices = WalkthroughData(renpy.get_filename_line(), i.caption)
                    if _choices != (None, None, None, None):
                        $ _choice_wt, _choice_hint, _choice_color, _choice_size = _choices

                if isinstance(_choice_wt, dict):
                    $ var_wt = getattr(store, _choice_wt.get("var"))
                    $ op_wt = operators.get(_choice_wt.get("operator"))
                    $ com_wt = _choice_wt.get("value")
                    $ disp_wt = op_wt(var_wt, com_wt)
                    $ walkthrough = _choice_wt.get('msg') if disp_wt else _choice_wt.get('alt_msg')
                elif isinstance(_choice_wt, list):
                    $ walkthrough = custom_join(_choice_wt, " ")
                elif isinstance(_choice_wt, str):
                    $ walkthrough = _choice_wt

                if isinstance(_choice_hint, dict):
                    $ var_hint = getattr(store, _choice_hint.get("var"))
                    $ op_hint = operators.get(_choice_hint.get("operator"))
                    $ com_hint = _choice_hint.get("value")
                    $ disp_hint = op_hint(var_hint, com_hint)
                    if isinstance(_choice_hint.get('msg'), list):
                        $ _hint = custom_join(_choice_hint.get('msg'))
                    elif isinstance(_choice_hint.get('msg'), str):
                        $ _hint = _choice_hint.get('msg')
                    if isinstance(_choice_hint.get('alt_msg'), list):
                        $ _hint_alt = custom_join(_choice_hint.get('alt_msg'))
                    elif isinstance(_choice_hint.get('alt_msg'), str):
                        $ _hint_alt = _choice_hint.get('alt_msg')
                    $ hint = _hint if disp_hint else _hint_alt
                elif isinstance(_choice_hint, list):
                    $ hint = custom_join(_choice_hint)
                elif isinstance(_choice_hint, str):
                    $ hint = _choice_hint

                $ _choice_size = _choice_size-7

                $ number = "{size=-5}{alpha=.5}%s{/alpha}{/size}. "%(count % 10) if count < 10 and persistent._choice_hotkeys else ''
                $ wt_data = " {b}{size=[_choice_size]}{color=[_choice_color]}%s{/color}{/size}{/b}"%(walkthrough) if persistent._walkthrough else ""
                $ output = "{}{}{}".format(number, i.caption, wt_data)

                textbutton output:
                    action i.action
                    xminimum 1500
                    text_align 1.0
                    #right_margin 0
                    #right_padding 10
                    if hint and persistent._walkthrough and persistent._choice_tooltips:
                        tooltip "{}".format(hint)

                key "K_{}".format(count) action (i.action if persistent._choice_hotkeys else NullAction())
                key "K_KP_{}".format(count) action (i.action if persistent._choice_hotkeys else NullAction())

        ## Uncomment the desired tooltip for desired renpy version
        if tooltip:
            ## Use With Renpy Version Below 7.5 and 8.0
            frame:
                style_prefix "tooltip"
                hbox:
                    text tooltip
            ## Use With Renpy Version Above 7.5 and 8.0
            #nearrect:
            #    focus "tooltip"
            #    prefer_top True
            #    frame:
            #        at choice_appear(.5)
            #        style_prefix "tooltip"
            #        hbox:
            #            text tooltip

    transform choice_appear(t=1):
        alpha 0.0
        easein t alpha 1.0

    screen input(prompt):
        # renpy.input("Please type the password and press 'Enter'|hint=cw|anotherkeyword=False", default="cw" if persistent._complete_input else '')
        # modify the input to your hearts content whichever keyword you need the above line is a sample of how it will split them
        style_prefix "input"

        window:
            if persistent._textbox_visible:
                background Transform(Frame(gui.textbox_location),
                    alpha=persistent._textbox_alpha,
                    xysize=(config.screen_width, gui.textbox_height))
            else:
                background None

            vbox:
                xalign gui.dialogue_text_xalign
                xpos gui.dialogue_xpos
                xsize gui.dialogue_width
                ypos gui.dialogue_ypos

                text prompt style "input_prompt" at input_appear(.5)

                input id "input" at input_appear(.5):
                    length 50 
                    if gui.use_custom_caret:
                        caret "custom_caret"

            vbox:
                style_prefix "input_hint"
                textbutton _("Confirm %s")%(u"{font=DejaVuSans.ttf}\u23CE{/font}"):
                    at input_appear(.5)
                    action GetText("input","input"),With(dissolve)

        key "input_enter" action GetText("input","input"),With(dissolve)

    screen file_slots(title):

        default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
        default savename = VariableInputValue('save_name', False)
        default the_page = VariableInputValue("_go_to_page", False)

        use game_menu(title):

            fixed:
                if persistent._custom_savename:
                    if title.lower() == _("save") and not page_name_value.get_page() in ["auto", "quick"]:
                        button:
                            ypos gui.mod_savename_input_ypos
                            xpos gui.mod_savename_input_xpos
                            style "page_label"

                            key_events True
                            action savename.Toggle()

                            input:
                                id "input"
                                length 26
                                size gui.mod_savename_input_size
                                prefix _("Enter A Save Name: ")
                                value savename
                                if gui.use_custom_caret:
                                    caret "custom_caret_2"
                                style "page_label_text"

                ## This ensures the input will get the enter event before any of the
                ## buttons do.
                order_reverse True

                ## The page name, which can be edited by clicking on a button.
                button:
                    ypos gui.mod_save_page_input_ypos
                    style "page_label"

                    key_events True
                    xalign 0.5
                    action page_name_value.Toggle()

                    input:
                        style "page_label_text"
                        value page_name_value
                        if gui.use_custom_caret:
                            caret "custom_caret"

                ## The grid of file slots.
                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5

                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            vbox:

                                add FileScreenshot(slot) xalign 0.5 yalign 0.5 #xysize WideRatio(config.thumbnail_width)

                                text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                    style "slot_time_text"

                                text FileSaveName(slot):
                                    style "slot_name_text"

                                key "save_delete" action FileDelete(slot)
                            if FileLoadable(slot):
                                textbutton _("X"):
                                    action FileDelete(slot)
                                    align (1.0,0.0)
                                    style_prefix "file_slots_delete"

                ## Buttons to access other pages.
                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign 1.0

                    spacing gui.page_spacing

                    textbutton _("<"):
                        action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A"):
                            action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q"):
                            action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]":
                            action FilePage(page)

                    textbutton _(">"):
                        action FilePageNext()

        button:

            key_events True
            xalign 1.0
            action the_page.Toggle()
            hbox:
                
                xsize gui.mod_save_goto_page_xsize
                ysize gui.mod_save_goto_page_ysize
                input:
                    style "page_label_text"
                    align (0.0, 0.5)
                    prefix "Go To Page: "
                    allow [str(i) for i in range(0,10)]
                    if gui.use_custom_caret:
                        caret "custom_caret"
                    length 3
                    value the_page
                textbutton "Go":
                    text_style "page_label_text"
                    align (1.0,0.5)
                    if _go_to_page.isdigit():
                        action FilePage(int(_go_to_page)),SetVariable("_go_to_page",""),the_page.Disable()

                if _go_to_page.isdigit():
                    key "input_enter" action FilePage(int(_go_to_page)),SetVariable("_go_to_page",""),the_page.Disable()

    transform input_appear(t=1):
        alpha 0.0
        easein t alpha 1.0

    screen callstack():
        if not jgs_develop:
            timer .1 action Hide("callstack")
        $ current_line = renpy.get_filename_line()
        $ callstack = renpy.get_return_stack()
        $ mode = renpy.get_mode()
        zorder 500
        vbox:
            ypos 50
            if current_line in walkthrough_dict().keys():
                text "In Dictionary"
            text _("Current Label: [CallStackLabel!q]") outlines [(2, "#0009", 1, 1)] color "#0F0"
            text _("Current Line: [current_line!q]") outlines [(2, "#0009", 1, 1)] color "#0F0"
            text _("Mode: [mode]") outlines [(2, "#0009", 1, 1)] color "#0F0"
            text "Press home to close..."
            if callstack:
                text _("CallStack: [callstack!q]") outlines [(2, "#0009", 1, 1)] color "#0F0"
                textbutton "Clear Stack" action Function(renpy.set_return_stack, [])

    screen tooltip(tooltip, **kwargs):
        $ f_align = kwargs.get("align", (0.5, 0.05))
        if isinstance(tooltip, str):
            pass
        elif isinstance(tooltip, list):
            $ tooltip = "\n".join(tooltip)
        if tooltip:
            frame:
                at choice_appear(.5)
                align f_align
                style_prefix "tooltip"
                hbox:
                    text tooltip size gui.text_size

    screen notify_item(msg, use_atl=True):
        zorder 1500
        tag notify_item

        style_prefix "notify_item"

        frame:

            if use_atl: # ATL not used for history

                at custom_notify_appear

            text msg text_align 0.5

    screen notify_container():
        zorder 1000
        tag notify_container
        fixed:
            align (0.5, (0.05 if persistent._quick_menu_layout == "top_center" else 0.0))
            #pos (5, 50)

            vbox:
                xalign 0.5
                yalign (0.05 if persistent._quick_menu_layout == "top_center" else 0.02)
                #xmaximum 250
                spacing 5

                # We index on the time the notification was added as that
                # is unique. Using index helps manage the ATL nicely
                if notify_messages:
                    for msg_info index msg_info[1] in reversed(notify_messages):
                        if msg_info[1] > time.time() - notify_duration:
                            use notify_item(msg_info[0])

    transform custom_notify_appear():
        xalign 0.5
        #ypos (10 if persistent._quick_menu_layout == "top_center" else 0)

        yoffset -15.0 yzoom 0.0 zoom 0.7 alpha 0.5

        easein 1.0 yoffset 0.0 yzoom 1.0 zoom 1.0 alpha 1.0

        pause 2.0

        easeout 1.0 yoffset -15.0 yzoom 0.0 zoom 0.1 alpha 0.0

        pause .5

        function finish_notify

    default persistent._togglelocked_replays = False
    default persistent._galleryunlock_replays = False
    
    screen replayGallery():

        key "r" action Return(),With(Dissolve(0.2))
        key "game_menu" action Return(),With(Dissolve(0.2))
        timer 1.0 action SceneUnlockCheck() repeat True
        style_prefix "replay_gallery"
        python:
            names = set()
            replaylength = len(ReplayData.Replays)
            colcount = 3
            rowcount = int(math.ceil((float(replaylength) / colcount)))
            remainder = (replaylength % colcount)

            rp_0 = persistent._galleryunlock_replays and not persistent._togglelocked_replays
            rp_1 = persistent._galleryunlock_replays and persistent._togglelocked_replays

            for rep in ReplayData.Replays:
                names.add(rep.name)

        tag menu

        default episode_page = "all"
        default by_name_or_episode = "name"
        default show_episode = True

        
        use game_menu(_("Scene Gallery")):

            label _("Scene selection")
            hbox:
                yoffset 30
                vbox:
                    textbutton "{size=+15}Toggle Navigation{/size}" action ToggleLocalVariable("show_episode")
                vbox:
                    textbutton "{size=+15}%s"%(_("Lock") if persistent.galleryunlock_replays else _("Unlock")) action ToggleField(persistent,"galleryunlock_replays")
                if persistent.galleryunlock_replays:
                    vbox:
                        textbutton _("{size=+15}%s Unseen")%("Unlock" if not persistent.togglelocked_replays else "Lock") action ToggleField(persistent,"togglelocked_replays")
                        
            null height 10

            hbox:
                yalign 1.0
                ysize 750
                if show_episode:
                    vbox:
                        textbutton "{size=+15}Toggle by %s{/size}"%("Episode" if by_name_or_episode == "name" else "Name") action If(by_name_or_episode == "episode", SetLocalVariable("by_name_or_episode", "name"), SetLocalVariable("by_name_or_episode", "episode"))
                        textbutton _("{size=+15}All{/size}") action SetLocalVariable("episode_page", "all")
                        vpgrid:
                            cols 1
                            scrollbars "vertical"
                            draggable True
                            mousewheel True
                            if by_name_or_episode == "episode":
                                vbox:
                                    spacing -10
                                    for i in range(1,gui.current_episode+1):
                                        textbutton _("{size=+15}Episode %d{/size}"%(i)) action SetLocalVariable("episode_page", "Episode {}".format(i))
                            else:
                                vbox:
                                    spacing -10
                                    for name in sorted(list(names)):
                                        if [(replay.name, replay.var) for replay in ReplayData.Replays if safe_eval(replay.var) and name == replay.name]:
                                            textbutton "{size=+15}%s{/size}"%name action SetLocalVariable("episode_page", name)
                                        elif persistent.galleryunlock_replays:
                                            textbutton "{size=+15}%s{/size}"%name action SetLocalVariable("episode_page", name)
                                        else:
                                            textbutton "{size=+15}???{/size}" action SetLocalVariable("episode_page", name)
                vpgrid:
                    cols (colcount if show_episode else colcount+1)
                    scrollbars "vertical"
                    draggable True
                    mousewheel True
                    spacing 25
                    xfill True

                    #grid colcount rowcount:
                    #    allow_underfull True
                    #    spacing 25
                    for replay in ReplayData.Replays:
                        if replay.episode == episode_page or episode_page == "all" or episode_page == replay.name:
                            frame:
                                if safe_eval(replay.var):
                                    imagebutton at replays_trans:
                                        idle (replay.hover if safe_eval(replay.var) else replay.idle)
                                        hover replay.hover
                                        action Replay(replay.label)
                                elif persistent.galleryunlock_replays:
                                    imagebutton at replays_trans:
                                        idle (replay.hover if persistent.togglelocked_replays else replay.idle)
                                        hover replay.hover
                                        if persistent.togglelocked_replays:
                                            action ReplayCustom(replay.label)
                                else:
                                    imagebutton at replays_blur(10):
                                        idle replay.idle
                                text "%s {font=%s}{color=%s}(%s){/color}{/font}"%(
                                            (replay.episode,replay.font,replay.color,replay.name) if safe_eval(replay.var)\
                                        else (replay.episode,replay.font,replay.color,replay.name) if rp_1\
                                        else (replay.episode,gui.text_font,gui.text_color,replay.name) if rp_0\
                                        else ("Locked",gui.text_font,gui.text_color,"???")) size gui.text_size-8
                    
                if remainder == 3:
                    null height 20
                if remainder == 2:
                    null height 20
                    null height 20
                if remainder == 1:
                    null height 20
                    null height 20
                    null height 20
    