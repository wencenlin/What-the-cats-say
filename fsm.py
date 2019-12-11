from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_choose(self, event):
        text = event.message.text
        return text.lower() == "start"

    def on_enter_choose(self, event):
        print("I'm entering choose")

        reply_token = event.reply_token
        send_text_message(reply_token, "貓咪總是「喵喵」叫，好想知道牠在說什麼！")
        self.go_back()

    def on_exit_choose(self):
        print("Leaving choose")

    def is_going_to_hulu(self, event):
        text = event.message.text
        return text.lower() == "呼嚕呼嚕"

    def on_enter_hulu(self, event):
        print("I'm entering hulu")

        reply_token = event.reply_token
        send_text_message(reply_token, "是「幼貓」?是「成貓撒嬌」?還是「緊張不舒服」?")
        self.go_back()

    def on_exit_hulu(self):
        print("Leaving hulu")

    def is_going_to_kitty1(self, event):
        text = event.message.text
        return text.lower() == "幼貓"

    def on_enter_kitty1(self, event):
        print("I'm entering kitty1")

        reply_token = event.reply_token
        send_text_message(reply_token, "在幼貓還沒睜開眼的時候,會透過呼嚕的振動頻率讓母貓找到自己")
        self.go_back()

    def on_exit_kitty1(self):
        print("Leaving kitty1")

    def is_going_to_kitty2(self, event):
        text = event.message.text
        return text.lower() == "貓咪說什麼？"

    def on_enter_kitty2(self, event):
        print("I'm entering kitty2")

        reply_token = event.reply_token
        send_text_message(reply_token, "喵:「媽媽，我在這裡!」")
        self.go_back()

    def on_exit_kitty2(self):
        print("Leaving kitty2")

    def is_going_to_flighty1(self, event):
        text = event.message.text
        return text.lower() == "成貓撒嬌"

    def on_enter_flighty1(self, event):
        print("I'm entering flighty1")

        reply_token = event.reply_token
        send_text_message(reply_token, "貓咪在放鬆狀態下主動接近飼主，發出呼嚕聲")
        self.go_back()

    def on_exit_flighty1(self):
        print("Leaving flighty1")

    def is_going_to_flighty2(self, event):
        text = event.message.text
        return text.lower() == "貓咪說什麼？"

    def on_enter_flighty2(self, event):
        print("I'm entering flighty2")

        reply_token = event.reply_token
        send_text_message(reply_token, "喵:「摸摸我嘛!」「跟我玩~」「我餓了!要吃飯!」")
        self.go_back()

    def on_exit_flighty2(self):
        print("Leaving flighty2")
    

    def is_going_to_nervous1(self, event):
        text = event.message.text
        return text.lower() == "緊張不舒服"

    def on_enter_nervous1(self, event):
        print("I'm entering nervous1")

        reply_token = event.reply_token
        send_text_message(reply_token, "貓咪在外出緊張或是身體不舒服的時候，會發出呼嚕聲來自我安慰")
        self.go_back()

    def on_exit_nervous1(self):
        print("Leaving nervous1")

    def is_going_to_nervous2(self, event):
        text = event.message.text
        return text.lower() == "貓咪說什麼？"

    def on_enter_nervous2(self, event):
        print("I'm entering nervous2")

        reply_token = event.reply_token
        send_text_message(reply_token, "喵:「我好緊張!」「嗚~我有點不舒服!」")
        self.go_back()

    def on_exit_nervous2(self):
        print("Leaving nervous2")

    def is_going_to_Miaow(self, event):
        text = event.message.text
        return text.lower() == "Miaow~"

    def on_enter_Miaow(self, event):
        print("I'm entering Miaow")

        reply_token = event.reply_token
        send_text_message(reply_token, "貓咪只有在對人類的時候才會發出「miaow~」的叫聲")
        send_text_message(reply_token, "引起人類注意，用叫聲來取得食物或滿足其他需求。")
        self.go_back()

    def on_exit_Miaow(self):
        print("Leaving Miaow")

    def is_going_to_watch1(self, event):
        text = event.message.text
        return text.lower() == "貓咪說什麼？"

    def on_enter_watch1(self, event):
        print("I'm entering watch1")

        reply_token = event.reply_token
        send_text_message(reply_token, "喵:「注意我!朕需要關注!」")
        self.go_back()

    def on_exit_watch1(self):
        print("Leaving watch1")

    def is_going_to_ke(self, event):
        text = event.message.text
        return text.lower() == "咯咯"

    def on_enter_ke(self, event):
        print("I'm entering ke")

        reply_token = event.reply_token
        send_text_message(reply_token, "貓咪在於活躍狀態或想與其他貓咪、同住的室友互動時，會發出這樣的聲音")
        self.go_back()

    def on_exit_ke(self):
        print("Leaving ke")

    def is_going_to_act1(self, event):
        text = event.message.text
        return text.lower() == "貓咪說什麼？"

    def on_enter_act1(self, event):
        print("I'm entering act1")

        reply_token = event.reply_token
        send_text_message(reply_token, "喵:「哈囉~朋友，要一起玩嗎?」")
        self.go_back()

    def on_exit_act1(self):
        print("Leaving act1")
    
    def is_going_to_ss(self, event):
        text = event.message.text
        return text.lower() == "嘶嘶"

    def on_enter_ss(self, event):
        print("I'm entering ss")

        reply_token = event.reply_token
        send_text_message(reply_token, "是「遇到敵人」還是「處在陌生的環境」呢?")
        self.go_back()

    def on_exit_ss(self):
        print("Leaving ss")

    def is_going_to_enemy1(self, event):
        text = event.message.text
        return text.lower() == "遇到敵人"

    def on_enter_enemy1(self, event):
        print("I'm entering enemy1")

        reply_token = event.reply_token
        send_text_message(reply_token, "貓會因為害怕而張大嘴巴，露出一嘴牙齒，試圖嚇退敵人、想要與敵人保持距離，也是攻擊前的最後警告。")
        self.go_back()

    def on_exit_enemy1(self):
        print("Leaving enemy1")

    def is_going_to_enemy2(self, event):
        text = event.message.text
        return text.lower() == "貓咪說什麼？"

    def on_enter_enemy2(self, event):
        print("I'm entering enemy2")

        reply_token = event.reply_token
        send_text_message(reply_token, "喵:「走開！別靠近我」")
        send_text_message(reply_token, "遇到貓咪哈氣的時候，最好拉開彼此間的距離，眼睛避開避免看牠，身體也不正面面對")
        self.go_back()

    def on_exit_enemy2(self):
        print("Leaving enemy2")

    def is_going_to_new1(self, event):
        text = event.message.text
        return text.lower() == "處在陌生的環境"

    def on_enter_new1(self, event):
        print("I'm entering new1")

        reply_token = event.reply_token
        send_text_message(reply_token, "因為聞到不熟悉味道，或是剛到陌生、未知的新環境裡，感覺到擔憂、不安")
        self.go_back()

    def on_exit_new1(self):
        print("Leaving new1")

    def is_going_to_new2(self, event):
        text = event.message.text
        return text.lower() == "貓咪說什麼？"

    def on_enter_new2(self, event):
        print("I'm entering new2")

        reply_token = event.reply_token
        send_text_message(reply_token, "喵:「拉開距離、離我遠點」")
        send_text_message(reply_token, "遇到貓咪哈氣的時候，最好拉開彼此間的距離，眼睛避開避免看牠，身體也不正面面對")
        self.go_back()

    def on_exit_new2(self):
        print("Leaving new2")

    def is_going_to_ho(self, event):
        text = event.message.text
        return text.lower() == "低吼"

    def on_enter_ho(self, event):
        print("I'm entering ho")

        reply_token = event.reply_token
        send_text_message(reply_token, "聲音或氣味讓貓咪感覺到被威脅")
        self.go_back()

    def on_exit_ho(self):
        print("Leaving ho")

    def is_going_to_threat1(self, event):
        text = event.message.text
        return text.lower() == "貓咪說什麼？"

    def on_enter_threat1(self, event):
        print("I'm entering threat1")

        reply_token = event.reply_token
        send_text_message(reply_token, "喵:「危險靠近!我要躲起來~」")
        self.go_back()

    def on_exit_threat1(self):
        print("Leaving threat1")

    def is_going_to_ou(self, event):
        text = event.message.text
        return text.lower() == "低鳴"

    def on_enter_ou(self, event):
        print("I'm entering ou")

        reply_token = event.reply_token
        send_text_message(reply_token, "通常發生在牠咬住獵物或嘴裡有非常在意的食物時")
        self.go_back()

    def on_exit_ou(self):
        print("Leaving ou")

    def is_going_to_protect1(self, event):
        text = event.message.text
        return text.lower() == "貓咪說什麼？"

    def on_enter_protect1(self, event):
        print("I'm entering protect1")

        reply_token = event.reply_token
        send_text_message(reply_token, "喵:「這是我的!才不分給你~」")
        self.go_back()

    def on_exit_protect1(self):
        print("Leaving protect1")

    def is_going_to_y(self, event):
        text = event.message.text
        return text.lower() == "大聲尖叫"

    def on_enter_y(self, event):
        print("I'm entering y")

        reply_token = event.reply_token
        send_text_message(reply_token, "貓感受到威脅程度爆表卻無路可逃，打算用盡力氣與敵人做最後的搏鬥")
        send_text_message(reply_token, "通常家貓在接受美容（如洗澡）或醫療的時候，或是貓咪在地盤被入侵，僵持不下、互相對峙的時候，都會發出這樣的叫聲。")
        self.go_back()

    def on_exit_y(self):
        print("Leaving y")

    def is_going_to_bloom1(self, event):
        text = event.message.text
        return text.lower() == "go to bloom1"

    def on_enter_bloom1(self, event):
        print("I'm entering bloom1")

        reply_token = event.reply_token
        send_text_message(reply_token, "喵:「救命啊~」「跟你拚了~」")
        self.go_back()

    def on_exit_bloom1(self):
        print("Leaving bloom1")