import uiScriptLocale
import app

ROOT_PATH = "d:/ymir work/ui/public/"

TEMPORARY_X = +13
TEXT_TEMPORARY_X = -10
BUTTON_TEMPORARY_X = 5
PVP_X = -10

if app.ENABLE_MULTI_LANGUAGE_SYSTEM:
    GRAPHIC_ON_OFF_WINDOW_Y = 270
    MULTI_LANGUAGE_WINDOW_Y = 395

window = {
    "name" : "SystemOptionDialog",
    "style" : ("movable", "float",),
    "x" : 0,
    "y" : 0,
    "width" : 305,
    "height" : 255,
    "children" : (
        {
            "name" : "board",
            "type" : "board",
            "x" : 0,
            "y" : 0,
            "width" : 305,
            "height" : 255,
            "children" : (
                ## Title
                {
                    "name" : "titlebar",
                    "type" : "titlebar",
                    "style" : ("attach",),
                    "x" : 8,
                    "y" : 8,
                    "width" : 284,
                    "color" : "gray",
                    "children" : (
                        { 
                        "name":"titlename", "type":"text", "x":0, "y":3, 
                        "horizontal_align":"center", "text_horizontal_align":"center",
                        "text": uiScriptLocale.SYSTEMOPTION_TITLE, 
                         },
                    ),
                },
				## Music
				{
					"name" : "music_name",
					"type" : "text",

					"x" : 30,
					"y" : 75,

					"text" : uiScriptLocale.OPTION_MUSIC,
				},
				
				{
					"name" : "music_volume_controller",
					"type" : "sliderbar",

					"x" : 110,
					"y" : 75,
				},
				
				{
					"name" : "bgm_button",
					"type" : "button",

					"x" : 20,
					"y" : 100,

					"text" : uiScriptLocale.OPTION_MUSIC_CHANGE,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				
				{
					"name" : "bgm_file",
					"type" : "text",

					"x" : 100,
					"y" : 102,

					"text" : uiScriptLocale.OPTION_MUSIC_DEFAULT_THEMA,
				},
				
				## Sound
				{
					"name" : "sound_name",
					"type" : "text",

					"x" : 30,
					"y" : 50,

					"text" : uiScriptLocale.OPTION_SOUND,
				},
				
				{
					"name" : "sound_volume_controller",
					"type" : "sliderbar",

					"x" : 110,
					"y" : 50,
				},	

				## ī�޶�
				{
					"name" : "camera_mode",
					"type" : "text",

					"x" : 40 + TEXT_TEMPORARY_X,
					"y" : 135+2,

					"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE,
				},
				
				{
					"name" : "camera_short",
					"type" : "radio_button",

					"x" : 110,
					"y" : 135,

					"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE_SHORT,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				
				{
					"name" : "camera_long",
					"type" : "radio_button",

					"x" : 110+70,
					"y" : 135,

					"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE_LONG,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

				## �Ȱ�
				{
					"name" : "fog_mode",
					"type" : "text",

					"x" : 30,
					"y" : 160+2,

					"text" : uiScriptLocale.OPTION_FOG,
				},
				
				{
					"name" : "fog_level0",
					"type" : "radio_button",

					"x" : 110,
					"y" : 160,

					"text" : uiScriptLocale.OPTION_FOG_DENSE,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				
				{
					"name" : "fog_level1",
					"type" : "radio_button",

					"x" : 110+50,
					"y" : 160,

					"text" : uiScriptLocale.OPTION_FOG_MIDDLE,
					
					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				
				{
					"name" : "fog_level2",
					"type" : "radio_button",

					"x" : 110 + 100,
					"y" : 160,

					"text" : uiScriptLocale.OPTION_FOG_LIGHT,
					
					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},

				## Ÿ�� ����
				{
					"name" : "tiling_mode",
					"type" : "text",

					"x" : 40 + TEXT_TEMPORARY_X,
					"y" : 185+2,

					"text" : uiScriptLocale.OPTION_TILING,
				},
				
				{
					"name" : "tiling_cpu",
					"type" : "radio_button",

					"x" : 110,
					"y" : 185,

					"text" : uiScriptLocale.OPTION_TILING_CPU,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				
				{
					"name" : "tiling_gpu",
					"type" : "radio_button",

					"x" : 110+50,
					"y" : 185,

					"text" : uiScriptLocale.OPTION_TILING_GPU,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				
				{
					"name" : "tiling_apply",
					"type" : "button",

					"x" : 110+100,
					"y" : 185,

					"text" : uiScriptLocale.OPTION_TILING_APPLY,

					"default_image" : ROOT_PATH + "middle_Button_01.sub",
					"over_image" : ROOT_PATH + "middle_Button_02.sub",
					"down_image" : ROOT_PATH + "middle_Button_03.sub",
				},

                ## Additional language selection window (added for multi-language support)
                {
                    "name" : "language_change_window",
                    "type" : "window",
                    "x" : 0,
                    "y" : MULTI_LANGUAGE_WINDOW_Y,
                    "width" : 305,
                    "height" : 22+20,
                    "children" : (
                        {
                            "name" : "language_select_text",
                            "type" : "text",
                            "x" : 40 + TEXT_TEMPORARY_X,
                            "y" : 0,
                            "text" : uiScriptLocale.OPTION_LANGUAGE_SELECT,
                        },
                        {
                            "name" : "language_select_img",
                            "type" : "image",
                            "x" : 40 + TEXT_TEMPORARY_X,
                            "y" : 20,
                            "image" : ROOT_PATH + "middle_button_02.sub",
                        },
                        {
                            "name" : "cur_language_text_window",
                            "type" : "window",
                            "x" : 40 + TEXT_TEMPORARY_X,
                            "y" : 20,
                            "width" : 210-16,
                            "height" : 16,
                            "children" : (
                                {"name":"cur_language_text", "type":"text", "x":0, "y":0, "text": "-", "all_align" : "center"},
                            ),
                        },
                        {
                            "name" : "language_select_button",
                            "type" : "button",
                            "x" : 40 + TEXT_TEMPORARY_X + 210 -16,
                            "y" : 20,
                            "default_image" : "d:/ymir work/ui/game/party_match/arrow_default.sub",
                            "over_image" : "d:/ymir work/ui/game/party_match/arrow_over.sub",
                            "down_image" : "d:/ymir work/ui/game/party_match/arrow_down.sub",
                        },
                        {
                            "name" : "language_change_button",
                            "type" : "button",
                            "x" : 40 + TEXT_TEMPORARY_X + 210 + 10,
                            "y" : -3 + 20,
                            "text" : uiScriptLocale.OPTION_LANGUAGE_CHANGE,
                            "default_image" : ROOT_PATH + "small_Button_01.sub",
                            "over_image" : ROOT_PATH + "small_Button_02.sub",
                            "down_image" : ROOT_PATH + "small_Button_03.sub",
                            "disable_image" : ROOT_PATH + "small_Button_03.sub",
                        },
                        {
                            "name" : "language_select_pivot_window",
                            "type" : "window",
                            "x" : 40 + TEXT_TEMPORARY_X,
                            "y" : 16+20,
                            "width" : 210,
                            "height" : 0,
                        },
                    ),
                },
            ),
        },
    ),
}

if app.ENABLE_MULTI_LANGUAGE_SYSTEM:
    # Update the height of the main window and its child
    window["height"] += 35
    window["children"][0]["height"] += 35

# The rest of your script remains unchanged
