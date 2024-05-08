import util
from nicegui import ui, run

cs_path = util.get_cs_path() + '\\game\\csgo\\'
log_dir = cs_path + 'console.log'

display_angles = None


async def update_angles():
    global display_angles
    angles = await run.io_bound(util.get_last_angles, log_dir)

    if angles:
        display_angles = '{:.2f}   {:.2f}'.format(angles[0], angles[1])

with ui.row().classes('bg-black text-white px-3 p-y2 rounded-md text-3xl items-center font-mono shadow shadow-black whitespace-pre-wrap'):
    ui.icon('explore')
    ui.label().bind_text_from(globals(), 'display_angles')

ui.timer(0.05, update_angles)

if util.is_condebug_in_steam_args():
    ui.notify('Could not find <b>-condebug</b> in Steam CS2 launch arguments.', html=True, close_button='Close',
              timeout=0, type='warning')


ui.run()
