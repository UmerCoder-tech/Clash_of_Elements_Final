import pygame as pg

# Funktion zum Laden und Skalieren von Animationsframes
def load_animation_frames(base_path, frame_count, scale_factor):
    frames = []
    for i in range(1, frame_count + 1):  # Startet bei 1 und geht bis frame_count
        frame = pg.image.load(f"{base_path}_{i}.png")  # Lade das Bild
        # Skalierung anwenden
        scaled_frame = pg.transform.scale(
            frame,
            (int(frame.get_width() * scale_factor), int(frame.get_height() * scale_factor))
        )
        frames.append(scaled_frame)
    return frames

# Animationen laden und direkt skalieren
scale_factor = 3.5  

animations_zuko = {
    "idle": load_animation_frames("Zuko/idle_frames/idle", 8, scale_factor),
    "run": load_animation_frames("Zuko/run_frames/run", 8, scale_factor),
    "jump": load_animation_frames("Zuko/jump_frames/jump", 20, scale_factor),
    "defend": load_animation_frames("Zuko/defend_frames/defend", 10, scale_factor),
    "atk1": load_animation_frames("Zuko/atk1_frames/air_atk", 8, scale_factor),
    "atk2": load_animation_frames("Zuko/atk2_frames/2_atk", 19, scale_factor),
    "atk3": load_animation_frames("Zuko/sp_atk_frames/sp_atk", 18, scale_factor),
    "take_hit": load_animation_frames("Zuko/take_hit_frames/take_hit", 6, scale_factor),
    "death": load_animation_frames("Zuko/death_frames/death", 13, scale_factor)
}

animations_susanoo = {
    "idle": load_animation_frames("Susanoo/idle_frames/idle", 10, scale_factor),
    "run": load_animation_frames("Susanoo/run_frames/run", 8, scale_factor),
    "jump": load_animation_frames("Susanoo/jump_frames/jump_full", 20, scale_factor),
    "defend": load_animation_frames("Susanoo/defend_frames/defend", 8, scale_factor),
    "atk1": load_animation_frames("Susanoo/atk1_frames/air_atk", 8, scale_factor),
    "atk2": load_animation_frames("Susanoo/atk2_frames/2_atk", 10, scale_factor),
    "atk3": load_animation_frames("Susanoo/sp_atk_frames/sp_atk", 20, scale_factor),
    "take_hit": load_animation_frames("Susanoo/take_hit_frames/take_hit", 6, scale_factor),
    "death": load_animation_frames("Susanoo/death_frames/death_uncen", 20, scale_factor)
}


