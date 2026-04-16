import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Music Player")

done = False
clock = pygame.time.Clock()

volume = 0.5
pygame.mixer.music.set_volume(volume)

base_dir = os.path.dirname(__file__)
images_dir = os.path.join(base_dir, "images")
music_dir = os.path.join(base_dir, "music", "01_sample_tracks")

tracks = [
    {
        "music": os.path.join(music_dir, "Bruno_Mars_-_Risk_It_All_80946687.mp3"),
        "image": os.path.join(images_dir, "brunomars-riskitall.jpg")
    },
    {
        "music": os.path.join(music_dir, "BTS - Mikrokosmos.mp3"),
        "image": os.path.join(images_dir, "mikrokosmos.png")
    },
    {
        "music": os.path.join(music_dir, "BTS - Pied Piper.mp3"),
        "image": os.path.join(images_dir, "piedpiper.jpg")
    },
    {
        "music": os.path.join(music_dir, "BTS - SWIM.mp3"),
        "image": os.path.join(images_dir, "swimbts.png")
    },
    {
        "music": os.path.join(music_dir, "Darkhan Juzz - Bylygyp.mp3"),
        "image": os.path.join(images_dir, "djuzz.jpg")
    },
    {
        "music": os.path.join(music_dir, "Darkhan Juzz - Eń Sulý.mp3"),
        "image": os.path.join(images_dir, "djuzz.jpg")
    },
    {
        "music": os.path.join(music_dir, "Darkhan Juzz - Úıde.mp3"),
        "image": os.path.join(images_dir, "djuzz.jpg")
    }
]

current_track = 0

current_image = pygame.image.load(tracks[current_track]["image"])
current_image = pygame.transform.scale(current_image, (400, 300))

MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)

pygame.mixer.music.load(tracks[current_track]["music"])
pygame.mixer.music.play()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.unpause()

            if event.key == pygame.K_s:
                pygame.mixer.music.pause()

            if event.key == pygame.K_n:
                current_track = (current_track + 1) % len(tracks)
                pygame.mixer.music.load(tracks[current_track]["music"])
                current_image = pygame.image.load(tracks[current_track]["image"])
                current_image = pygame.transform.scale(current_image, (400, 300))
                pygame.mixer.music.play()

            if event.key == pygame.K_b:
                current_track = (current_track - 1) % len(tracks)
                pygame.mixer.music.load(tracks[current_track]["music"])
                current_image = pygame.image.load(tracks[current_track]["image"])
                current_image = pygame.transform.scale(current_image, (400, 300))
                pygame.mixer.music.play()

            if event.key == pygame.K_UP:
                volume = min(1.0, volume + 0.1)
                pygame.mixer.music.set_volume(volume)

            if event.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.1)
                pygame.mixer.music.set_volume(volume)

            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        if event.type == MUSIC_END:
            current_track = (current_track + 1) % len(tracks)
            pygame.mixer.music.load(tracks[current_track]["music"])
            current_image = pygame.image.load(tracks[current_track]["image"])
            current_image = pygame.transform.scale(current_image, (400, 300))
            pygame.mixer.music.play()

    screen.fill((255, 255, 255))
    rect = current_image.get_rect(center=(800 // 2, 600 // 2))
    screen.blit(current_image, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()