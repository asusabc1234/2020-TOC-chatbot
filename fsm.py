from transitions.extensions import GraphMachine

from utils import *


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_picture(self, event):
        text = event.message.text
        return text.lower() == "picture"

    def is_going_to_west_team(self, event):
        text = event.message.text
        return text.lower() == "west"

    def is_going_to_northwest_divition(self, event):
        text = event.message.text
        return text.lower() == "northwest divition"

    def is_going_to_jazz(self, event):
        text = event.message.text
        return text.lower() == "jazz"

    def is_going_to_nuggets(self, event):
        text = event.message.text
        return text.lower() == "nuggets"

    def is_going_to_thunders(self, event):
        text = event.message.text
        return text.lower() == "thunders"   

    def is_going_to_timberwolves(self, event):
        text = event.message.text
        return text.lower() == "timberwolves"

    def is_going_to_trail_blazers(self, event):
        text = event.message.text
        return text.lower() == "trail blazers"            

    def is_going_to_pacific_divition(self, event):
        text = event.message.text
        return text.lower() == "pacific divition" 

    def is_going_to_clippers(self, event):
        text = event.message.text
        return text.lower() == "clippers"

    def is_going_to_kings(self, event):
        text = event.message.text
        return text.lower() == "kings"

    def is_going_to_lakers(self, event):
        text = event.message.text
        return text.lower() == "lakers"   

    def is_going_to_suns(self, event):
        text = event.message.text
        return text.lower() == "suns"

    def is_going_to_warriors(self, event):
        text = event.message.text
        return text.lower() == "warriors" 

    def is_going_to_southwest_divition(self, event):
        text = event.message.text
        return text.lower() == "southwest divition"       

    def is_going_to_mavericks(self, event):
        text = event.message.text
        return text.lower() == "mavericks"

    def is_going_to_grizzles(self, event):
        text = event.message.text
        return text.lower() == "grizzles"

    def is_going_to_pelicans(self, event):
        text = event.message.text
        return text.lower() == "pelicans"   

    def is_going_to_rockets(self, event):
        text = event.message.text
        return text.lower() == "rockets"

    def is_going_to_spurs(self, event):
        text = event.message.text
        return text.lower() == "spurs" 

    def is_going_to_east_team(self, event):
        text = event.message.text
        return text.lower() == "east"  

    def is_going_to_atalantic_divition(self, event):
        text = event.message.text
        return text.lower() == "atalantic divition"

    def is_going_to_raptors(self, event):
        text = event.message.text
        return text.lower() == "raptors"

    def is_going_to_celtics(self, event):
        text = event.message.text
        return text.lower() == "celtics"

    def is_going_to_76ers(self, event):
        text = event.message.text
        return text.lower() == "76ers"   

    def is_going_to_nets(self, event):
        text = event.message.text
        return text.lower() == "nets"

    def is_going_to_knics(self, event):
        text = event.message.text
        return text.lower() == "knics" 

    def is_going_to_central_divition(self, event):
        text = event.message.text
        return text.lower() == "central divition"

    def is_going_to_bucks(self, event):
        text = event.message.text
        return text.lower() == "bucks"

    def is_going_to_pacers(self, event):
        text = event.message.text
        return text.lower() == "pacers"

    def is_going_to_pistons(self, event):
        text = event.message.text
        return text.lower() == "pistons"   

    def is_going_to_bulls(self, event):
        text = event.message.text
        return text.lower() == "bulls"

    def is_going_to_caveliers(self, event):
        text = event.message.text
        return text.lower() == "caveliers" 

    def is_going_to_southeast_divition(self, event):
        text = event.message.text
        return text.lower() == "southeast divition"                 

    def is_going_to_heats(self, event):
        text = event.message.text
        return text.lower() == "heats"

    def is_going_to_magic(self, event):
        text = event.message.text
        return text.lower() == "magic"

    def is_going_to_hornets(self, event):
        text = event.message.text
        return text.lower() == "hornets"   

    def is_going_to_wizards(self, event):
        text = event.message.text
        return text.lower() == "wizards"

    def is_going_to_hawks(self, event):
        text = event.message.text
        return text.lower() == "hawks" 

    def is_going_to_highlight(self, event):
        text = event.message.text
        return text.lower() == "highlight"

    def restart(self, event):
        text = event.message.text
        return text.lower() == "restart"    

    def on_enter_picture(self, event):
        print("I'm entering state picture")
        reply_token = event.reply_token
        send_team(reply_token)

    def on_enter_west_team(self, event):
        print("I'm entering state west_team")
        reply_token = event.reply_token
        send_west_team(reply_token)

    def on_enter_northwest_divition(self, event):
        print("I'm entering state northwest_divition")
        reply_token = event.reply_token
        send_northwest_divition_team(reply_token)

    def on_enter_jazz(self, event):
        print("I'm entering state jazz")
        reply_token = event.reply_token
        send_jazz(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_nuggets(self, event):
        print("I'm entering state nuggets")
        reply_token = event.reply_token
        send_nuggets(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_thunders(self, event):
        print("I'm entering state thunders")
        reply_token = event.reply_token
        send_thunders(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_timberwolves(self, event):
        print("I'm entering state timberwolves")
        reply_token = event.reply_token
        send_timberwolves(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_trail_blazers(self, event):
        print("I'm entering state trail blazers")
        reply_token = event.reply_token
        send_trail_blazers(reply_token)
        event.message.text = "restart"
        self.advance(event)                

    def on_enter_pacific_divition(self, event):
        print("I'm entering state pacific_divition")
        reply_token = event.reply_token
        send_pacific_divition_team(reply_token)

    def on_enter_clippers(self, event):
        print("I'm entering state clippers")
        reply_token = event.reply_token
        send_clippers(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_kings(self, event):
        print("I'm entering state kings")
        reply_token = event.reply_token
        send_kings(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_lakers(self, event):
        print("I'm entering state lakers")
        reply_token = event.reply_token
        send_lakers(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_suns(self, event):
        print("I'm entering state suns")
        reply_token = event.reply_token
        send_suns(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_warriors(self, event):
        print("I'm entering state warriors")
        reply_token = event.reply_token
        send_warriors(reply_token)
        event.message.text = "restart"
        self.advance(event) 

    def on_enter_southwest_divition(self, event):
        print("I'm entering state southwest_divition")
        reply_token = event.reply_token
        send_southwest_divition_team(reply_token)    

    def on_enter_mavericks(self, event):
        print("I'm entering state mavericks")
        reply_token = event.reply_token
        send_mavericks(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_grizzles(self, event):
        print("I'm entering state grizzles")
        reply_token = event.reply_token
        send_grizzles(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_pelicans(self, event):
        print("I'm entering state pelicans")
        reply_token = event.reply_token
        send_pelicans(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_rockets(self, event):
        print("I'm entering state rockets")
        reply_token = event.reply_token
        send_rockets(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_spurs(self, event):
        print("I'm entering state spurs")
        reply_token = event.reply_token
        send_spurs(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_east_team(self, event):
        print("I'm entering state east_team")
        reply_token = event.reply_token
        send_east_team(reply_token)

    def on_enter_atalantic_divition(self, event):
        print("I'm entering state atalantic_divition")
        reply_token = event.reply_token
        send_atalantic_divition_team(reply_token)

    def on_enter_raptors(self, event):
        print("I'm entering state raptors")
        reply_token = event.reply_token
        send_raptors(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_celtics(self, event):
        print("I'm entering state celtics")
        reply_token = event.reply_token
        send_celtics(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_76ers(self, event):
        print("I'm entering state 76ers")
        reply_token = event.reply_token
        send_76ers(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_nets(self, event):
        print("I'm entering state nets")
        reply_token = event.reply_token
        send_nets(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_knics(self, event):
        print("I'm entering state knics")
        reply_token = event.reply_token
        send_knics(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_central_divition(self, event):
        print("I'm entering state central_divition")
        reply_token = event.reply_token
        send_central_divition_team(reply_token) 

    def on_enter_bucks(self, event):
        print("I'm entering state bucks")
        reply_token = event.reply_token
        send_bucks(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_pacers(self, event):
        print("I'm entering state pacers")
        reply_token = event.reply_token
        send_pacers(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_pistons(self, event):
        print("I'm entering state pistons")
        reply_token = event.reply_token
        send_pistons(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_bulls(self, event):
        print("I'm entering state bulls")
        reply_token = event.reply_token
        send_bulls(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_caveliers(self, event):
        print("I'm entering state caveliers")
        reply_token = event.reply_token
        send_caveliers(reply_token)
        event.message.text = "restart"
        self.advance(event) 

    def on_enter_southeast_divition(self, event):
        print("I'm entering state southeas_divition")
        reply_token = event.reply_token
        send_southeast_divition_team(reply_token)                    

    def on_enter_heats(self, event):
        print("I'm entering state heats")
        reply_token = event.reply_token
        send_heats(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_magic(self, event):
        print("I'm entering state magic")
        reply_token = event.reply_token
        send_magic(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_hornets(self, event):
        print("I'm entering state hornets")
        reply_token = event.reply_token
        send_hornets(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_wizards(self, event):
        print("I'm entering state wizards")
        reply_token = event.reply_token
        send_wizards(reply_token)
        event.message.text = "restart"
        self.advance(event)

    def on_enter_hawks(self, event):
        print("I'm entering state hawks")
        reply_token = event.reply_token
        send_hawks(reply_token)
        event.message.text = "restart"
        self.advance(event)
   
    def on_enter_highlight(self, event):
        print("I'm entering highlight")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=l0sSxqSUXJY")
        self.go_back()

    def on_exit_highlight(self):
        print("Leaving highlight")
