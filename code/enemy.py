import pygame
from settings import *
from entity import Entity
from support import *

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites, damage_player,trigger_death_particles, add_exp):
        super().__init__(groups)
        self.sprite_type = 'enemy'

        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]

        self.rect = self.image.get_rect(topleft = pos)
        self.hit_box = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 1600
        self.damage_player = damage_player
        self.trigger_death_particles = trigger_death_particles
        self.add_exp = add_exp

        self.vulnerable = True
        self.been_hit = False
        self.hit_time = None
        self.invincibility_duration = 500

        self.death_sound = pygame.mixer.Sound('../audio/death.wav')
        self.hit_sound = pygame.mixer.Sound('../audio/Hit.wav')
        self.attack_sound = pygame.mixer.Sound(monster_info['attack_sound'])
        self.death_sound.set_volume(0.2)
        self.hit_sound.set_volume(0.2)
        self.attack_sound.set_volume(0.2)

    def import_graphics(self, name):
        self.animations = {'idle': [], 'attack': [], 'move': [], 'hit': []}
        main_path = f'../graphics/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return distance, direction

    def get_status(self, player):
        if self.been_hit:
            self.status = 'hit'
        else:
            distance = self.get_player_distance_direction(player)[0]
            if distance <= self.attack_radius and self.can_attack:
                if self.status != 'attack':
                    self.frame_index = 0
                self.status = 'attack'
            elif distance <= self.notice_radius:
                self.status = 'move'
            else:
                self.status = 'idle'

    def actions(self, player):
        if self.status == 'attack':
            if self.monster_name == 'tengu':
                self.attack_cooldown = 1900
            self.direction = pygame.math.Vector2()
            attack_animation_length = len(self.animations['attack'])
            middle_frame = attack_animation_length // 2

            if int(self.frame_index) == middle_frame and self.can_attack:
                self.attack_time = pygame.time.get_ticks()
                self.direction = pygame.math.Vector2()
                self.damage_player(self.attack_damage, self.attack_type)
                self.attack_sound.play()
        elif self.status == 'move':
            if self.can_attack:
                self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            elif self.status == 'hit':
                self.been_hit = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)].convert_alpha()
        if self.monster_name == 'tengu':
            self.image = pygame.transform.scale(self.image, (320,320))
        elif self.monster_name == 'giant_slime':
            self.image = pygame.transform.scale2x(self.image)
        else:
            self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(center=self.hit_box.center)

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True

    def get_damage(self, player, attack_type):
        if self.vulnerable:
            self.hit_sound.play()
            self.direction = self.get_player_distance_direction(player)[1]
            self.been_hit = True
            self.status = 'hit'

            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
            else:
                self.health -= player.get_full_magic_damage()

            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False

    def check_death(self):
        if self.health <= 0:
            self.death_sound.play()
            self.kill()
            self.trigger_death_particles(self.rect.center, self.monster_name)
            self.add_exp(self.exp)

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance

    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.cooldowns()
        self.check_death()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)
