#################################
# 在以下区域，将账号密码修改为你自己的
define persistent._MCloudBackup = {
    'a':"ni_de_zhang_hao@email.com",#你的莫盘账号
    'pwd':"mo_pan_sheng_cheng_de_mi_ma"#莫盘生成的密码
}
#################################


default persistent._MCloudBackup_time = None
default persistent._MCloudBackup_no = 0

init python:
    import subprocess
    import store
    import datetime
    def mc_bak():
        dir = renpy.config.basedir.replace('\\', '/')+"/game/Submods/MCloudBackup/py3/dist/MCloudbak.exe"
        cmd = "\"{}\" -a \"{}\" -p \"{}\" -n {}".format(
            dir,
            persistent._MCloudBackup['a'],
            persistent._MCloudBackup['pwd'],
            persistent._MCloudBackup_no
        )
        st=subprocess.STARTUPINFO
        st.dwFlags=subprocess.STARTF_USESHOWWINDOW
        st.wShowWindow=subprocess.SW_HIDE
        subprocess.Popen(cmd, startupinfo=st)
        persistent._MCloudBackup_no = persistent._MCloudBackup_no + 1
        persistent._MCloudBackup_time = datetime.datetime.now()
        
    mc_bak()

init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="云端备份 莫盘版",
        description=(
            "将你的游戏存档备份至莫盘"
        ),
        version="1.0.0",
        settings_pane="mc_info",
    )
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Netease Music",
            user_name="MAS-Submod-MoyuTeam",
            repository_name="MAS-MCloudBackup",
            update_dir="",
            attachment_id=None
        )
screen mc_info():
    vbox:
        xmaximum 800
        xfill True
        style_prefix "check"
    text "上次备份于：[persistent._MCloudBackup_time]":
                xalign 1.0 yalign 0.0
                xoffset -10
                style "main_menu_version"
    textbutton "> 立刻备份":
        action Function(mc_bak)
