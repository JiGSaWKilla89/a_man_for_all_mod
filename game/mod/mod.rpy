init -1500 python early:
    import os
    import zipfile
    zip_path = os.path.join(config.gamedir, "mod", "mutagen.zip")
    zip_directory = os.path.join(config.gamedir, "python-packages")
    zip_final = os.path.join(zip_directory, "mutagen")

    def extract_packages(zip_path, directory, zip_final):

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(directory)

        if os.path.exists(zip_final):
            os.unlink(zip_path)

    if os.path.exists(zip_path):
        extract_packages(zip_path, zip_directory, zip_final)

init -500 python:
    def JGSLoadable(item, ext=".rpy"):
        return renpy.loadable("mod/{}{}".format(item,ext))

init python:
    if JGSLoadable("music_room") and JGSLoadable("music_room_screen"):
        shortcuts = """
            {size=75}{color=FB4301}JiG{/color}{color=#000}SaW{/color} Mod Shortcuts{/size}

            Toggle Cheat Menu: {color=FB4301}J{/color}
            Toggle Textbox Shortcut: {color=FB4301}T{/color}
            Toggle Choice Hotkeys: {color=FB4301}C{/color}
            Toggle Custom Savenames: {color=FB4301}Shift+S{/color}
            Toggle Fancy Text: {color=FB4301}Shift+F{/color}
            Toggle Fancy Text Effect: {color=FB4301}E{/color}
            Toggle Fancy Text Always Effect: {color=FB4301}R{/color}
            Toggle Walkthrough: {color=FB4301}W{/color}
            Toggle Walkthrough Choice Tooltips: {color=FB4301}Shift+T{/color}
            Toggle Music Room: {color=FB4301}M{/color}
            Toggle Notifications Stack/Standard: {color=FB4301}N{/color}
            Toggle Quick Menu Visibility: {color=FB4301}Q{/color}
            Toggle Quick Menu Position: {color=FB4301}Shift+Q{/color}
            Adjust Textbox Visibility Keypad {color=FB4301}+/-{/color}
            """
    else:
        shortcuts = """
            {size=75}{color=FB4301}JiG{/color}{color=#000}SaW{/color} Mod Shortcuts{/size}

            Toggle Cheat Menu: {color=FB4301}J{/color}
            Toggle Textbox Shortcut: {color=FB4301}T{/color}
            Toggle Choice Hotkeys: {color=FB4301}C{/color}
            Toggle Custom Savenames: {color=FB4301}Shift+S{/color}
            Toggle Fancy Text: {color=FB4301}Shift+F{/color}
            Toggle Fancy Text Effect: {color=FB4301}E{/color}
            Toggle Fancy Text Always Effect: {color=FB4301}R{/color}
            Toggle Walkthrough: {color=FB4301}W{/color}
            Toggle Walkthrough Choice Tooltips: {color=FB4301}Shift+T{/color}
            Toggle Notifications Stack/Standard: {color=FB4301}N{/color}
            Toggle Quick Menu Visibility: {color=FB4301}Q{/color}
            Toggle Quick Menu Position: {color=FB4301}Shift+Q{/color}
            Adjust Textbox Visibility Keypad {color=FB4301}+/-{/color}
            """

    wt_choice_tooltip = """Each Choice marked with either Good Choice/Bad Choice is
        just a recommendation from me.
        You play the game the way you want.
        """

init -5 python:
    import time
    import operator
    config.developer = True
    config.console = True
    config.autoreload = True
    config.rollback_length = 100
    config.hard_rollback_limit = 150

    if not persistent._always_effect_title:
        persistent._always_effect_title = "None"

    if not persistent._slow_effect_title:
        persistent._slow_effect_title = "Fade"

    if not persistent._effect_delay:
        persistent._effect_delay = 0.2

    if persistent._quick_menu_state == None:
        persistent._quick_menu_state = "visible"

    if not persistent._quick_menu_layout:
        persistent._quick_menu_layout = "bottom_center"

    if persistent._fancy_text == None:
        persistent._fancy_text = True

    if persistent._choice_hotkeys == None:
        persistent._choice_hotkeys = True
    
    if persistent._walkthrough == None:
        persistent._walkthrough = True

    if persistent._choice_tooltips == None:
        persistent._choice_tooltips = True

    if persistent._custom_savename == None:
        persistent._custom_savename = True

    if persistent._textbox_visible == None:
        persistent._textbox_visible = True

    if persistent._textbox_alpha == None:
        persistent._textbox_alpha = 0.5

    bypass_list = [
        "ADVCharacter", "ADVSpeaker", "Action", "AddToSet", "Alpha", "AlphaBlend", "AlphaDissolve", "AlphaMask", 
        "AnimatedValue", "Animation", "At", "Attribute", "AudioData", "AudioPositionValue", "Bar", "BarValue", 
        "Borders", "BrightnessMatrix", "Button", "Call", "Camera", "CaptureFocus", "Character", "ClearFocus", "Color", 
        "ColorMatrix", "ColorizeMatrix", "ComposeTransition", "Composite", "Condition", "ConditionGroup", "ConditionSwitch", 
        "Confirm", "Continue", "ContrastMatrix", "CopyToClipboard", "Crop", "CropMove", "CurrentScreenName", "CycleDict", 
        "CycleField", "CycleLocalVariable", "CycleScreenVariable", "CycleVariable", "DictEquality", "DictInputValue", 
        "DictValue", "DisableAllInputValues", "Dissolve", "DownloadSync", "Drag", "DragGroup", "DynamicCharacter", 
        "DynamicDisplayable", "DynamicImage", "EditFile", "EndReplay", "ExecJS", "FactorZoom", "Fade", "FieldEquality", 
        "FieldInputValue", "FieldValue", "FileAction", "FileCurrentPage", "FileCurrentScreenshot", "FileDelete", "FileJson", 
        "FileLoad", "FileLoadable", "FileNewest", "FilePage", "FilePageName", "FilePageNameInputValue", "FilePageNext", 
        "FilePagePrevious", "FileSave", "FileSaveName", "FileScreenshot", "FileSlotName", "FileTakeScreenshot", "FileTime", 
        "FileUsedSlots", "Fixed", "Flatten", "FontGroup", "Frame", "Function", "Gallery", "GamepadCalibrate", "GamepadExists", 
        "GetCharacterVolume", "GetFocusRect", "GetMixer", "GetTooltip", "Grid", "HBox", "Help", "Hide", "HideInterface", 
        "HueMatrix", "IdentityMatrix", "If", "Image", "ImageButton", "ImageDissolve", "ImageReference", "IncrementDict", 
        "IncrementField", "IncrementLocalVariable", "IncrementScreenVariable", "IncrementVariable", "Input", "InputValue", 
        "InvertMatrix", "InvertSelected", "JSONDB", "Jump", "Language", "Layer", "LayeredImage", "LayeredImageProxy", 
        "Live2D", "LiveComposite", "LiveCrop", "LiveTile", "LocalVariableInputValue", "LocalVariableValue", "MainMenu", 
        "Matrix", "Max", "MixerValue", "Model", "Motion", "MouseDisplayable", "MouseMove", "Move", "MoveFactory", "MoveIn", 
        "MoveOut", "MoveTransition", "Movie", "MultiPersistent", "MultiRevertable", "MultipleTransition", "MusicRoom", 
        "NVLCharacter", "NVLSpeaker", "NoRollback", "Notify", "Null", "NullAction", "OffsetMatrix", "OldMoveTransition", 
        "OpacityMatrix", "OpenDirectory", "OpenURL", "PY2", "Pan", "ParameterizedText", "Particles", "Pause", "PauseAudio", 
        "Pixellate", "Placeholder", "Play", "PlayCharacterVoice", "Position", "Preference", "PushMove", "Queue", "QueueEvent", 
        "QuickLoad", "QuickSave", "Quit", "RemoveFromSet", "Replay", "RestartStatement", "Return", "Revolve", "RevolveInOut", 
        "RollForward", "Rollback", "RollbackToIdentifier", "RotateMatrix", "RotoZoom", "RoundRect", "SaturationMatrix", 
        "ScaleMatrix", "ScreenVariableInputValue", "ScreenVariableValue", "Screenshot", "Scroll", "SelectedIf", "SensitiveIf", 
        "SepiaMatrix", "Set", "SetCharacterVolume", "SetDict", "SetField", "SetLocalVariable", "SetMixer", "SetMute", 
        "SetScreenVariable", "SetVariable", "SetVoiceMute", "Show", "ShowMenu", "ShowTransient", "ShowingSwitch", "SideImage", 
        "SizeZoom", "Skip", "SlottedNoRollback", "SnowBlossom", "Solid", "Speaker", "SplineMatrix", "SplineMotion", "Sprite", 
        "SpriteManager", "Start", "StaticValue", "Stop", "Style", "StylePreference", "SubTransition", "Swing", "Text", 
        "TextButton", "Tile", "TintMatrix", "ToggleDict", "ToggleField", "ToggleFocus", "ToggleLocalVariable", "ToggleMute", 
        "ToggleScreen", "ToggleScreenVariable", "ToggleSetMembership", "ToggleVariable", "ToggleVoiceMute", "Tooltip", 
        "Transform", "TransformMatrix", "UploadSync", "VBox", "VariableInputValue", "VariableValue", "Viewport", "VoiceInfo", 
        "VoiceReplay", "Window", "With", "XScrollValue", "YScrollValue", "Zoom", "ZoomInOut", 'absolute', 'color', 'defaultdict', 
        'dict', 'list', 'object', 'position', 'pystr', 'python_dict', 'python_list', 'python_object', 'python_set', 'set', 
        'str', 'unicode', 'xrange', 'alt', 'bchr', 'bord', 'eval', 'hyperlink_function', 'hyperlink_sensitive', 
        'hyperlink_styler', 'input', 'menu', 'nvl_clear', 'nvl_clear_next', 'nvl_erase', 'nvl_hide', 'nvl_menu', 'nvl_show', 
        'nvl_show_core', 'nvl_window', 'predict_menu', 'predict_say', 'print', 'range', 'raw_input', 'say', 'set_reload', 
        'sorted', 'sv', 'time_check', 'tobytes', 'toggle_skipping', 'var_search', 'voice', 'voice_can_replay', 'voice_replay', 
        'voice_sustain', "achievement", "audio", "bubble", "build", "director", "gui", "iap", "icon", "layeredimage", 
        "store", "textshader", "updater", "alicefade", "blinds", "buffbertfade", "dissolve", "downrightfade", "ease", 
        "easeinbottom", "easeinleft", "easeinright", "easeintop", "easeoutbottom", "easeoutleft", "easeoutright", 
        "easeouttop", "fade", "fadeslash", "fastfade", "fastredfade", "firefade", "flash", "hallofade", "healfade", 
        "holyfade", "hpunch", "in_03", "in_08", "in_09", "in_18", "in_24", "irisin", "irisout", "lightfade", 
        "longfade", "lucyfade", "lucyquickfade", "move", "moveinbottom", "moveinleft", "moveinright", "moveintop", 
        "moveoutbottom", "moveoutleft", "moveoutright", "moveouttop", "out_03", "out_08", "out_09", "out_18", "out_24", 
        "pinkfade", "pinkflash", "pixellate", "portalfade", "pushdown", "pushleft", "pushright", "pushup", "redfade", 
        "slideawaydown", "slideawayleft", "slideawayright", "slideawayup", "slidedown", "slideleft", "slideright", "slideup", 
        "slowyellowfade", "squares", "upleftfade", "virginfade", "vpunch", "wipedown", "wipeleft", "wiperight", "wipeup", 
        "yorikofade", "zoomin", "zoominout", "zoomout", "bypass_list", "center", "default", "delayed_blink", "left", 
        "notify_appear", "offscreenleft", "offscreenright", "reset", "right", "swing", "top", "topleft", "topright", 
        "truecenter", "config", "anim ", "basestring ", "chr", "default_transition", "define", "division", "extend", 
        "im", "inspect", "layout", "library", "nvl_list", "nvl_variant", "open", "os", "persistent", "preferences", 
        "print_function", "pygame_sdl2", "quick_menu", "random", "renpy", "round", "style", "suppress_overlay", "sys", 
        "theme", "ui", "unicode_literals", "vldf_timer", "with_statement", "mouse_visible", "absolute_import", "main_menu", 
        "small", "touch", "AlwaysEffectChange", "AutoForwardTime", "EffectDelayDisplay", "FancyCheck", "FancyText", "SlowEffectChange", 
        "TextSpeed", "ToggleFancyText", "VolumeDisplay", "always_pulse", "always_shake", "save_name", "slow_fade", 
        "slow_nonsense", "slow_rotate", "slow_shake", "slow_shaking_slide", "slow_slide_down", "slow_slide_left", 
        "slow_slide_right", "slow_slide_up", "slow_typewriter",
        ]
    
    bypass_list = [i.strip() for i in bypass_list]

    def fix_multiline(string, count=12):
        return string.replace(" "*count,"")

    def adjust_brightness(hex_color, levels):
        def clamp(value):
            return max(0, min(255, value))

        # Convert hex to RGB(A)
        try:
            hex_color = hex_color.lstrip('#')
        except:
            hex_color = hex_color.hexcode.lstrip('#')

        # Handle different hex lengths
        if len(hex_color) == 3:  # #RGB
            r, g, b = [int(c*2, 16) for c in hex_color]
            a = None
        elif len(hex_color) == 4:  # #RGBA
            r, g, b, a = [int(c*2, 16) for c in hex_color]
        elif len(hex_color) == 6:  # #RRGGBB
            r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
            a = None
        elif len(hex_color) == 8:  # #RRGGBBAA
            r, g, b, a = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16), int(hex_color[6:8], 16)
        else:
            raise ValueError("Invalid hex color format")

        # Adjust brightness
        r = clamp(r + levels)
        g = clamp(g + levels)
        b = clamp(b + levels)

        # Convert RGB(A) back to hex
        if a is None:
            return '#{:02X}{:02X}{:02X}'.format(r, g, b)
        else:
            return '#{:02X}{:02X}{:02X}{:02X}'.format(r, g, b, a)

    def var_search(name="", default=store):
        for i in dir(default):
            if not i.startswith(("_","__")):
                if name:
                    if name in i:
                        print("VAR:{} | VALUE:{}".format(i, eval(i)))
                else:
                    if isinstance(eval(i),renpy.character.ADVCharacter):
                        pass
                    elif i in bypass_list:
                        pass
                    else:
                        print("VAR:{} | VALUE:{}".format(i, eval(i)))

    def set_reload():
        print(config.reload)
        if config.autoreload:
            config.autoreload = False
        else:
            config.autoreload = True

    def TextSpeed():
        _cps_value = int(round(preferences.text_cps))
        _cps_value = '200' if _cps_value == 0 else _cps_value
        return _cps_value

    def AutoForwardTime():
        _auto_forward_time = int(round(preferences.afm_time))
        _auto_forward_time = '1' if _auto_forward_time == 0 else _auto_forward_time
        return _auto_forward_time
    
    def TextBoxAlpha():
        _alpha = float(round(persistent._textbox_alpha,2))
        _alpha = _alpha*100
        _alpha = round(_alpha,0)
        _alpha_out = str(_alpha)
        _alpha_out = _alpha_out.replace(".0"," %")
        return _alpha_out

    def VolumeDisplay(value):
        '''
        Returns the Value Volume Level to Ren'Py.
        '''
        try:
            _volume = float(round(preferences.get_mixer(value),2))
        except:
            _volume = float(round(preferences.get_volume(value),2))
        _volume = _volume*100
        _volume = round(_volume,0)
        _volume_out = str(_volume)
        _volume_out = _volume_out.replace(".0"," %")
        return _volume_out

    def FancyCheck():
        if getattr(persistent, "_fancy_text"):
            if preferences.text_cps == 200 or preferences.text_cps == 0:
                preferences.text_cps = 120
        else:
            preferences.text_cps = 0

    config.after_load_callbacks.append(FancyCheck)

    def WideRatio(width):
        # Take the width of your screen or any size for that matter
        # and you will get an output of width x height
        height = width * 9.0 / 16.0
        return int(width), int(height)

    class SlowEffectChange(Action):
        def __init__(self, bypass=False):
            self.bypass = bypass
            self.effects = {
                "Fade" : slow_fade,
                "Slide Up" : slow_slide_up(20),
                "Slide Down" : slow_slide_down(20),
                "Slide Left" : slow_slide_left(20),
                "Slide Right" : slow_slide_right(20),
                "Shake Slide" : slow_shaking_slide(10,10,20,20),
                "Shake" : slow_shake(10, 10),
                "Typewriter" : slow_typewriter,
                "Rotate" : slow_rotate,
                "Nonsense" : slow_nonsense
            }

            # Convert the dictionary keys to a list for cycling through effects
            self.effect_names = list(self.effects.keys())

            # Initialize the current effect index
            initial_effect_name = persistent._slow_effect_title if hasattr(persistent, '_slow_effect_title') else self.effect_names[0]
            self.current_index = self.effect_names.index(initial_effect_name)

        def __call__(self):
            if main_menu and not self.bypass:
                return
            # Move to the next effect
            self.current_index = (self.current_index + 1) % len(self.effect_names)

            # Get the current effect name
            current_effect_name = self.effect_names[self.current_index]

            # Get the current effect function
            current_effect = self.effects[current_effect_name]

            # Apply the current effect
            persistent._slow_effect = current_effect
            persistent._slow_effect_title = current_effect_name

            # Restart interaction if needed
            renpy.restart_interaction()
            if main_menu and not self.bypass:
                renpy.notify("Changed Effect to: %s"%persistent._slow_effect_title)
            if not main_menu:
                renpy.notify("Changed Effect to: %s"%persistent._slow_effect_title)

            #return persistent._slow_effect_title

    class AlwaysEffectChange(Action):
        def __init__(self, bypass=False):
            self.bypass = bypass
            self.effects = {
                "None" : None,
                "Fade" : slow_fade,
                "Always Shake" : always_shake(1, 1),
                "Always Pulse" : always_pulse
            }

            # Convert the dictionary keys to a list for cycling through effects
            self.effect_names = list(self.effects.keys())

            # Initialize the current effect index
            initial_effect_name = persistent._always_effect_title if hasattr(persistent, '_always_effect_title') else self.effect_names[0]
            self.current_index = self.effect_names.index(initial_effect_name)

        def __call__(self):
            if main_menu and not self.bypass:
                return
            # Move to the next effect
            self.current_index = (self.current_index + 1) % len(self.effect_names)

            # Get the current effect name
            current_effect_name = self.effect_names[self.current_index]

            # Get the current effect function
            current_effect = self.effects[current_effect_name]

            # Apply the current effect
            persistent._always_effect = current_effect
            persistent._always_effect_title = current_effect_name

            # Restart interaction if needed
            renpy.restart_interaction()
            if main_menu and not self.bypass:
                renpy.notify("Changed Always Effect to: %s"%persistent._always_effect_title)
            if not main_menu:
                renpy.notify("Changed Always Effect to: %s"%persistent._always_effect_title)
                

            #return persistent._always_effect_title

    def ToggleFancyText():
        if main_menu:
            return
        if persistent._fancy_text:
            if preferences.text_cps == 200 or preferences.text_cps == 0:
                preferences.text_cps = 120
        else:
            preferences.text_cps = 0
        persistent._fancy_text = not persistent._fancy_text
        renpy.run(With(dissolve))
        renpy.notify(_("Fancy Text: %s")%(_("On") if persistent._fancy_text else _("Off")))
        renpy.restart_interaction()

    def EffectDelayDisplay():
        _alpha = float(round(persistent._effect_delay,2))
        _alpha = _alpha*100
        _alpha = round(_alpha,0)
        _alpha_out = str(_alpha)
        _alpha_out = _alpha_out.replace(".0","")
        if _alpha_out == "0":
            _alpha_out = "Off"
        if _alpha_out != "100":
            _alpha_out = _alpha_out.replace("0","")
        else:
            _alpha_out = _alpha_out.replace("00","0")
        return _alpha_out

    def QuickPositions():
        buttons = {
            "bottom_center"  : "Bottom Center",
            "top_center"     : "Top Center"
            }
        return buttons.get(persistent._quick_menu_layout)

    class CycleQuickStates(Action):
        def __init__(self, bypass=False):
            self.bypass = bypass

        def __call__(self):
            #if main_menu and not self.bypass:
            #    return
            if not getattr(store, "quick_menu"):
                setattr(store, "quick_menu", True)
            if persistent._quick_menu_state == "visible":
                persistent._quick_menu_state = "hover"
            elif persistent._quick_menu_state == "hover":
                persistent._quick_menu_state = "hidden"
            elif persistent._quick_menu_state == "hidden":
                persistent._quick_menu_state = "visible"
            renpy.run(With(dissolve))
            if not main_menu and not self.bypass:
                renpy.notify(_("Quick Menu is: %s")%(persistent._quick_menu_state.title()))
            renpy.restart_interaction()

    class CycleQuickMenu(Action):
        def __init__(self, bypass=False):
            self.bypass = bypass
            self.buttons = ["bottom_center", "top_center"]

            self.current_position = self.buttons.index(persistent._quick_menu_layout)

        def __call__(self):
            #if main_menu and not self.bypass:
            #    return
            current_index = self.buttons.index(persistent._quick_menu_layout)
            next_index = (current_index + 1) % len(self.buttons)
            self.current_position = self.buttons[next_index]
            persistent._quick_menu_layout = self.current_position
            renpy.run(With(dissolve))
            if not main_menu and not self.bypass:
                renpy.notify(_("Quick Menu Position: %s")%(QuickPositions()))
            renpy.restart_interaction()

    def ToggleChoiceHotkeys():
        persistent._choice_hotkeys = not persistent._choice_hotkeys
        renpy.run(With(dissolve))
        renpy.notify(_("%sHotkeys: %s")%(_("Choice ") if not main_menu else "",_("On") if persistent._choice_hotkeys else _("Off")))
        renpy.restart_interaction()

    def WalkthroughData(line, caption):
        choices = walkthrough_dict().get(line, None)
        if choices:
            valid = choices.get(caption, None)
            if valid:
                _choice_wt    = valid.get("wt"  , "")
                _choice_hint  = valid.get("hint", "")
                _choice_color = valid.get("color", None)
                _choice_size  = valid.get("size", None)

                try:
                    _choice_color = _choice_color.hexcode
                except:
                    _choice_color = _choice_color

                if _choice_color in [None, "None", "none"]:
                    _choice_color = gui.text_color

                if _choice_size in [None, "None", "none"]:
                    _choice_size = gui.text_size

                if _choice_hint in [None, "None", "none"]:
                    _choice_hint = ""

                return _choice_wt, _choice_hint, _choice_color, _choice_size
        return None, None, None, None

    class GetText(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)

    def toggle_callstack():
        if not jgs_develop:
            return
        if main_menu:
            return
        renpy.run(ToggleScreen("callstack", transition=dissolve))

    def ToggleWalkthrough():
        persistent._walkthrough = not persistent._walkthrough
        renpy.run(With(dissolve))
        renpy.notify(_("Walkthrough: %s")%(("On") if persistent._walkthrough else _("Off")))
        renpy.restart_interaction()

    def ToggleSavename():
        persistent._custom_savename = not persistent._custom_savename
        renpy.run(With(dissolve))
        renpy.notify(_("Custom Savenames: %s")%(("On") if persistent._custom_savename else _("Off")))
        renpy.restart_interaction()

    def ToggleChoiceToolTips():
        persistent._choice_tooltips = not persistent._choice_tooltips
        renpy.run(With(dissolve))
        renpy.notify(_("Choice Tooltips: %s")%(("On") if persistent._choice_tooltips else _("Off")))
        renpy.restart_interaction()

    def ToggleTextbox():
        persistent._textbox_visible = not persistent._textbox_visible
        renpy.run(With(dissolve))
        renpy.notify(_("Textbox: %s")%(("On") if persistent._textbox_visible else _("Off")))
        renpy.restart_interaction()

    def custom_join(items, join_param="\n"):
        fix = []
        for i in items:
            if i:
                fix.append(i)

        return "{}".format(join_param).join(fix)

    def _adjust_dialogue(direction="+"):
        txt = "Textbox Visibility"
        if direction == "+":
            if persistent._textbox_alpha <= 0.99 :
                persistent._textbox_alpha += 0.01
            else:
                persistent._textbox_alpha = 1.0
                txt = "Textbox Is Completely Visible"
        elif direction == "-":
            if persistent._textbox_alpha > 0.01:
                persistent._textbox_alpha -= 0.01
            else:
                persistent._textbox_alpha = 0.0
                txt = "Textbox Is Completely Invisible"
        renpy.notify("%s: %s"%(txt, TextBoxAlpha()))

    def add_notify_message(msg=None):

        if not msg:
            return

        global notify_messages

        add_time = time.time()

        # Just in case multiple notifications are added really really 
        # fast, this gives them minorly different time values so they 
        # do not steal displayables meant for other notifications
        if notify_messages and notify_messages[-1][1] >= add_time:

            add_time = notify_messages[-1][1] + 0.01

        notify_messages.append((msg, add_time))

        # just keep notify_history_length number of messages
        notify_messages = notify_messages[-notify_history_length:]

        renpy.show_screen("notify_container")
        renpy.restart_interaction()

    def finish_notify(trans, st, at):

        max_start = time.time() - notify_duration

        if not [k for k in notify_messages if k[1] > max_start]:

            # If the notification list is now empty, hide the screen
            renpy.hide_screen("notify_container")
            renpy.restart_interaction()

        return None

    def toggle_notify_type():
        if persistent._notify_custom:
            persistent._notify_custom = False
            config.notify = renpy.display_notify
            renpy.notify("Custom Notifications Off")
        else:
            persistent._notify_custom = True
            config.notify = add_notify_message
            renpy.notify("Custom Notifications On")
        
        renpy.restart_interaction()

    @renpy.pure
    class CreateScreenVariableData(Action):
        """
        :doc: data_action

        Gets the value of the variable called `name` in the current screen.
        In a ``use``\ d screen, this action accesses and sets the given variable
        in the context of the screen containing the ``use``\ d one(s).
        """
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __call__(self):
            cs = renpy.current_screen()
            if cs is None:
                return
            if not self.name in cs.scope:
                cs.scope[self.name] = self.value

    def CreateScreenVariable(name,value):
        return renpy.run(CreateScreenVariableData(name,value))

    @renpy.pure
    class GetScreenVariableData(Action):
        """
        :doc: data_action

        Gets the value of the variable called `name` in the current screen.
        In a ``use``\ d screen, this action accesses and sets the given variable
        in the context of the screen containing the ``use``\ d one(s).
        """
        def __init__(self, name):
            self.name = name

        def __call__(self):
            cs = renpy.current_screen()
            if cs is None:
                return
            return(cs.scope[self.name])

    def GetScreenVariable(val):
        return renpy.run(GetScreenVariableData(val))

    def safe_eval(attr_string):
        import ast
        try:
            # Parse the string to an AST node
            tree = ast.parse(attr_string, mode='eval')
            
            # Ensure the tree only contains an attribute chain or name
            if isinstance(tree.body, ast.Attribute):
                return _resolve_attr(tree.body)
            elif isinstance(tree.body, ast.Name):
                return globals().get(tree.body.id)
            else:
                raise ValueError("Unsupported expression")
        
        except Exception as e:
            print("Error: {}".format(e))
            return None

    def _resolve_attr(node):
        import ast
        """Helper function to recursively resolve attributes."""
        if isinstance(node, ast.Attribute):
            # Recursively resolve the value of the base object
            base_value = _resolve_attr(node.value)
            if base_value:
                return getattr(base_value, node.attr, None)
        elif isinstance(node, ast.Name):
            # Retrieve the base object from globals
            return globals().get(node.id)
        return None

    def autosave_override():
        global disable_saves

        if not disable_saves:
            renpy.run(QuickSave())

    def dump_data(data, name):
        import os, json
        path = os.path.join(config.gamedir, "mod", "json", "{}.json".format(name))

        # Ensure data is a dictionary or list before saving
        if isinstance(data, (dict, list, OrderedDict)):
            with open(path, "w") as f:
                json.dump(data, f, indent=4)
        else:
            raise TypeError("Data must be a dictionary or list.")

    def load_data(name):
        import os, json
        path = os.path.join(config.gamedir, "mod", "json", "{}.json".format(name))
        with open(path, "r") as f:
            data = json.load(f, object_pairs_hook=OrderedDict)
        return data

    def dump_data_all():
        dump_data(ignore_dic, "z_walkthrough_ignore")
        dump_data(_overwrite_dictionary, "z_overwrite_dictionary")
        dump_data(_disable_autosave, "z_disable_list")
        dump_data(_enable_autosave, "z_enable_list")
        dump_data(_mc_data, "z_mc_data")
        dump_data(_save_names, "z_savenames")
        dump_data(replay_dict, "z_replays")
    
    #load_data("z_walkthrough_ignore")
    #load_data("z_overwrite_dictionary")
    #load_data("z_disable_list")
    #load_data("z_enable_list")
    #load_data("z_mc_data")
    #load_data("z_savenames")
    #load_data("z_replays")

    config.keymap[ 'quick_save_button' ] = [ 'K_F5' ]
    config.underlay.append(renpy.Keymap(quick_save_button = autosave_override))

    config.keymap[ 'quick_load_button' ] = [ 'K_F6' ]
    config.underlay.append(renpy.Keymap(quick_load_button = QuickLoad()))

    config.keymap[ 'toggle_quick_menu_state' ] = [ 'noshift_K_q' ]
    config.underlay.append(renpy.Keymap(toggle_quick_menu_state = CycleQuickStates()))

    config.keymap[ 'toggle_quick_menu_position' ] = [ 'shift_K_q' ]
    config.underlay.append(renpy.Keymap(toggle_quick_menu_position = CycleQuickMenu()))

    config.keymap[ 'toggle_always_effect' ] = [ 'noshift_K_r' ]
    config.underlay.append(renpy.Keymap(toggle_always_effect = AlwaysEffectChange()))

    config.keymap[ 'toggle_slow_effect' ] = [ 'noshift_K_e' ]
    config.underlay.append(renpy.Keymap(toggle_slow_effect = SlowEffectChange()))

    config.keymap[ 'toggle_fancy_text' ] = [ 'shift_K_f' ]
    config.underlay.append(renpy.Keymap(toggle_fancy_text = Function(ToggleFancyText)))

    config.keymap[ 'toggle_choice_hotkeys' ] = [ 'noshift_K_c' ]
    config.underlay.append(renpy.Keymap(toggle_choice_hotkeys = Function(ToggleChoiceHotkeys)))

    config.keymap[ 'toggle_walkthrough' ] = [ 'noshift_K_w' ]
    config.underlay.append(renpy.Keymap(toggle_walkthrough = Function(ToggleWalkthrough)))

    config.keymap[ 'toggle_savename' ] = [ 'shift_K_s' ]
    config.underlay.append(renpy.Keymap(toggle_savename = Function(ToggleSavename)))

    config.keymap[ 'toggle_choice_tooltips' ] = [ 'shift_K_t' ]
    config.underlay.append(renpy.Keymap(toggle_choice_tooltips = Function(ToggleChoiceToolTips)))

    config.keymap[ 'toggle_textbox' ] = [ 'noshift_K_t' ]
    config.underlay.append(renpy.Keymap(toggle_textbox = Function(ToggleTextbox)))

    config.keymap[ 'toggle_callstack' ] = [ 'K_HOME' ]
    config.underlay.append(renpy.Keymap(toggle_callstack = Function(toggle_callstack)))

    config.keymap[ 'toggle_visibility_up' ] = [ 'K_KP_PLUS', 'repeat_K_KP_PLUS' ]
    config.underlay.append(renpy.Keymap(toggle_visibility_up = Function(_adjust_dialogue, "+")))

    config.keymap[ 'toggle_visibility_down' ] = [ 'K_KP_MINUS', 'repeat_K_KP_MINUS' ]
    config.underlay.append(renpy.Keymap(toggle_visibility_down = Function(_adjust_dialogue, "-")))

    config.keymap[ 'toggle_notifications' ] = [ 'K_n' ]
    config.underlay.append(renpy.Keymap(toggle_notifications = Function(toggle_notify_type)))

    config.overlay_screens.append("shortcuts")
    config.overlay_screens.append("notice")


    if persistent._notify_custom == None:
        persistent._notify_custom = True

    if persistent._notify_custom:
        config.notify = add_notify_message
    else:
        config.notify = renpy.display_notify

    def NoneHandler(value=None):
        renpy.run(NullAction())

    config.hyperlink_handlers["#"] = NoneHandler

    def set_initial_volumes(mixer="music", v=.5):
        try:
            _preferences.set_mixer(mixer, v)
        except:
            _preferences.set_volume(mixer, v)

define config.label_overrides["splashscreen"] = "splashscreen_jgs"#???

label splashscreen_jgs:
    if not persistent._jgs_default_volumes:
        $ persistent._jgs_default_volumes = True
        $ set_initial_volumes("music")
        $ set_initial_volumes("sfx")
        $ set_initial_volumes("voice")
    
    stop music
    scene warning with fade
    pause
    show vw_opener with fade
    play sound "audio/sounds/intro/vwintro.ogg"
    pause
    stop sound


    scene black
    with Pause(1)

    show splashText with dissolve
    with Pause(15)

    hide text with dissolve
    with Pause(1)

    $ mod_updated = get_latest_mod()

    return

init 1:
    image splashText = Text(fix_multiline(shortcuts).strip(), style="splash")
    default preferences.text_cps = 120
    default persistent._unlocked_gallery = False
    default persistent._show_empty_gallery = False
    default persistent._sharing_content = False
    default persistent._use_overrides = True

    default _go_to_page = ""
    default jg_s = "{size=20}"
    default jg_1 = "{color=#FB4301}"
    default jg_2 = "{color=#000000}"
    default jg_3 = "{/color}"

    default notify_messages = []
    default notify_duration = 4.0
    default notify_history_length = 5
    default disable_saves = False
    
init python:
    class LabelOverrides(Action):# Update dictionary on customs
        def __init__(self, value=False, allow_call=False):
            global _overwrite_dictionary
            self.value = value
            self.allow = allow_call
            self.dic = _overwrite_dictionary

        def __call__(self):
            if self.allow:
                persistent._use_overrides = self.value

            for k, v in self.dic.items():
                if persistent._use_overrides:
                    config.label_overrides[k] = v
                else:
                    if k == "splashscreen":
                        config.label_overrides[k] = v
                    else:
                        config.label_overrides[k] = k

            renpy.restart_interaction()
                      
    renpy.run(LabelOverrides())

init python:
    if renpy.version_tuple[:-1] >= (7,5,0) or renpy.version_tuple[:-1] >= (8,0,0):
        preferences.audio_when_minimized = False
    
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

init python:
    import math

    def label_overwrites():
        labels = renpy.get_all_labels()

        labels = [i for i in labels if i.startswith("replay")]

        return labels    
    
    def get_prefix_choice():
        if four_choice == True:
            return "choice_four"

        elif two_choice == True:
            return "choice_two"

        elif sex_three_choice == True:
            return "choice_sex_three"

        elif sex_four_choice == True:
            return "choice_sex_four"

        else:
            return "choice"

    def bg_mod():
        return "mod/cheats/ep%s.jpg"%episode_end

    def mc_mod():
        return "mod/cheats/end%s.jpg"%episode_mc
    
    CallStackLabel = ""

    def labelCallback(name,abnormal):
        global CallStackLabel
        global episode_mc, save_name, current_episode, episode_end, _autosave, disable_saves, _game_menu_screen

        #title = ""
        #current = "Episode 0"
        #current_end = 1

        if not name.startswith("_"):
            if name != CallStackLabel and not name in _disable_autosave:
                _autosave = True
                disable_saves = False
                _game_menu_screen = "save_screen"
                config.autosave_on_quit = True
                config.autosave_on_input = True
                config.autosave_on_choice = True
                renpy.write_log("Autosave Unblocked")
            CallStackLabel = name
            for block_label in _disable_autosave:
                if name == block_label:
                    _autosave = False
                    disable_saves = True
                    _game_menu_screen = "preferences"
                    config.autosave_on_quit = False
                    config.autosave_on_input = False
                    config.autosave_on_choice = False
                    renpy.write_log("Autosave Blocked")


            for unblock_label in _enable_autosave:
                if name == unblock_label:
                    _autosave = True
                    disable_saves = False
                    _game_menu_screen = "save_screen"
                    config.autosave_on_quit = True
                    config.autosave_on_input = True
                    config.autosave_on_choice = True
                    renpy.write_log("Autosave Unblocked")


            for val, lst in _mc_data:
                for lbl in lst:
                    if name.startswith(lbl):
                        episode_mc = val

            for k, (episode_title, label, ender) in _save_names.items():
                if name.startswith(label):
                    save_name = episode_title
                    current_episode = k
                    episode_end = ender

    config.label_callback = labelCallback

    class SceneUnlockCheck(Action):
        def __call__(self):
            global Replays

            for var, (img, lbl, sel, episode, image, name, color, font) in Replays().items():
                if eval(var):
                    renpy.mark_image_seen(img)
                    renpy.mark_label_seen(lbl)
                    renpy.mark_label_seen(sel)
                    renpy.mark_label_seen("%s_jgs"%lbl)
                    renpy.mark_label_seen("%s_jgs"%sel)

                if renpy.seen_image(img):
                    renpy.mark_label_seen(lbl)
                    renpy.mark_label_seen(sel)
                    renpy.mark_label_seen("%s_jgs"%lbl)
                    renpy.mark_label_seen("%s_jgs"%sel)
                    setattr(store,var,True)

                if renpy.seen_label(lbl) or renpy.seen_label("%s_jgs"%lbl):
                    renpy.mark_image_seen(img)
                    setattr(store,var,True)
                    
                if renpy.seen_label(sel) or renpy.seen_label("%s_jgs"%sel):
                    renpy.mark_image_seen(img)
                    setattr(store,var,True)

            renpy.restart_interaction()

    class ReplayCustom(Action):
        def __init__(self, lbl, locked=False):
            self.lbl = lbl
            self.locked = locked
        
        def __call__(self):
            global replay_override, replay_override_label
            replay_override = True
            replay_override_label = self.lbl
            renpy.run(Replay(self.lbl, locked=self.locked))

    def AfterReplay(v=""):
        global Replays, replay_override, replay_override_label
        altlabel = "%s_jgs"%replay_override_label

        if not replay_override:
            return

        if v != "":
            img, lbl, sel, episode, image, name, color, font = Replays().get(v,"")
            renpy.mark_label_unseen(lbl)
            renpy.mark_label_unseen(sel)
            renpy.mark_image_unseen(img)
            setattr(store,v,False)
        if v == "":
            for var, (img, lbl, sel, episode, image, name, color, font) in Replays().items():
                if replay_override_label == lbl or replay_override_label == sel or replay_override_label == altlabel:
                    renpy.mark_label_unseen(lbl)
                    renpy.mark_label_unseen(sel)
                    renpy.mark_image_unseen(img)
                    setattr(store,var,False)

        replay_override = False
        replay_override_label = ""

    config.after_replay_callback = AfterReplay

    config.keymap[ 'toggle_cheat_j' ] = [ 'K_j' ]
    config.underlay.append(renpy.Keymap(toggle_cheat_j = (ShowMenu("cheatmod"),With(Dissolve(0.5)))))

    def Replays():
        import json
        from collections import OrderedDict
        replays = renpy.file("mod/replays.json")
        data = json.load(replays, object_pairs_hook=OrderedDict)
        return data

    def GenerateReplaysOBJ(data):
        for key, values in data.items():
            ReplayData(key, *values)

    class ReplayData():
        Replays = []
        def __init__(self, variable, trigger_img, init_label, start_label, episode, image, name, color, font, scope={}):
            self.var = variable
            self.trigger_image = trigger_img#???
            self.init_label = init_label
            self.label = start_label
            self.episode = episode
            self.idle = image + "_idle"
            self.hover = image + "_hover"
            self.color = color
            self.font = font
            self.name = name
            self.scope = scope
            ReplayData.Replays.append(self)

    GenerateReplaysOBJ(Replays())

init 2 python:#TODO Update Dictionary
    from collections import OrderedDict

    replay_dict = load_data("z_replays")

    def auto_populate():
        dictionary = {#TODO Update dictionary when new character is available
            "harlow" : ["har", "Harlow"],
            "kate" : ["kat", "Kate"],
            "irene" : ["seo", "Irene"],
            "marisa" : ["mar", "Marisa"],
            "sophia" : ["sop", "Sophia"],
            "lorelei" : ["lori", "Lorelei"],
            "erika" : ["eri", "Erika"],
            "grace" : ["gra", "Grace"],
            "jordan" : ["jor", "Jordan"],
            "threesome" : ["jor", "Jordan/Marisa"],
            "vanessa" : ["van", "Vanessa"],
            "riley" : ["ril", "Riley"]
            }
        
        output = []
        for key, (trigger_image, (episode_number, trigger_label, choice_label, replay_image)) in replay_dict.items():
            for kwarg_key, (who, name) in dictionary.items():
                if renpy.seen_label(trigger_label) or renpy.seen_label("%s_jgs"%trigger_label):
                    setattr(store, key, True)
                if kwarg_key in key:
                    output.append([
                        key, 
                        episode_number,
                        replay_image,
                        choice_label,
                        name,
                        '{}.who_args["color"]'.format(who),
                        '{}.who_args["font"]'.format(who),
                        ])
                    break

        return output

    replays = auto_populate()

    def new_replays_dict():
        import json
        import os
        from collections import OrderedDict
        out_dict = OrderedDict()

        current_dict = Replays()

        for persistent_variable, episode_title, replay_image, label, name, color, font in replays:
            if persistent_variable not in out_dict:
                out_dict[persistent_variable] = []
            trigger_image, (episode_number, trigger_label, choice_label, replay_image) = replay_dict.get(persistent_variable,'')

            try:
                out_dict[persistent_variable].extend([
                    trigger_image, 
                    trigger_label, 
                    choice_label, 
                    episode_title, 
                    replay_image, 
                    name, 
                    "#%s"%eval(color), 
                    eval(font)])
            except:
                out_dict[persistent_variable].extend([
                    trigger_image, 
                    trigger_label, 
                    choice_label, 
                    episode_title, 
                    replay_image, 
                    name, 
                    "#%s"%eval(color), 
                    gui.text_font])

        if out_dict != current_dict:
            with open(os.path.join(config.gamedir, "mod", "replays.json"), "w") as file:
                json.dump(out_dict, file, indent=4, ensure_ascii=False)

            print(os.path.join(config.gamedir, "mod", "replays.json"))

    new_replays_dict()

init -1 python:#TODO update list on overrides
    from collections import OrderedDict
    
    _overwrite_dictionary = load_data("z_overwrite_dictionary")

    _disable_autosave = load_data("z_disable_list")
    
    _enable_autosave = load_data("z_enable_list")

    _mc_data = load_data("z_mc_data")
    
    _save_names = load_data("z_savenames")