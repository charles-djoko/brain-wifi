from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import jnius
from jnius import autoclass

Context = autoclass('android.content.Context')
WifiP2pManager = autoclass('android.net.wifi.p2p.WifiP2pManager')

class BrainWiFiDirectApp(App):
    def build(self):
        self.title = "Brain Wi-Fi Direct"
        root = BoxLayout(orientation='vertical', padding=25, spacing=15)
        
        title_label = Label(text="🧠 Brain Wi-Fi Direct", font_size=22, bold=True, color=(0.53, 0.7, 0.98, 1), size_hint_y=None, height=40)
        root.add_widget(title_label)

        self.status_label = Label(text="Statut : Inactif (Prêt à émettre)", font_size=14, color=(0.95, 0.7, 0.7, 1), size_hint_y=None, height=30)
        root.add_widget(self.status_label)

        root.add_widget(Label(text="Nom du Réseau Direct (SSID) :", font_size=12, color=(0.65, 0.68, 0.78, 1), size_hint_y=None, height=20))
        self.ssid_input = TextInput(text="DIRECT-Brain-WiFi", font_size=14, multiline=False, size_hint_y=None, height=40)
        root.add_widget(self.ssid_input)

        btn_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        self.btn_start = Button(text="Lancer le Tunnel P2P", background_color=(0.65, 0.89, 0.63, 1), bold=True)
        self.btn_start.bind(on_press=self.start_wifi_direct)
        btn_layout.add_widget(self.btn_start)

        self.btn_stop = Button(text="Couper", background_color=(0.95, 0.54, 0.65, 1), bold=True)
        self.btn_stop.bind(on_press=self.stop_wifi_direct)
        btn_layout.add_widget(self.btn_stop)
        root.add_widget(btn_layout)

        root.add_widget(Label(text="Journal du Tunnel :", font_size=12, color=(0.65, 0.68, 0.78, 1), size_hint_y=None, height=20))
        self.log_box = TextInput(text="[INFO] Application Brain Wi-Fi Direct initialisée.\n", font_size=11, readonly=True)
        root.add_widget(self.log_box)

        self.wifi_p2p_manager = None
        self.channel = None
        return root

    def log(self, message):
        self.log_box.text += f"{message}\n"

    def start_wifi_direct(self, instance):
        self.log("[START] Activation du point d'accès Wi-Fi Direct...")
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = PythonActivity.mActivity
            self.wifi_p2p_manager = activity.getSystemService(Context.WIFI_P2P_SERVICE)
            self.channel = self.wifi_p2p_manager.initialize(activity, activity.getMainLooper(), None)
            if self.wifi_p2p_manager and self.channel:
                self.wifi_p2p_manager.createGroup(self.channel, None)
                self.status_label.text = "Statut : Actif (Passerelle 192.168.43.1)"
                self.log("[SUCCÈS] Tunnel Wi-Fi Direct ouvert.")
            else:
                self.log("[ERREUR] Échec de l'initialisation P2P.")
        except Exception as e:
            self.log(f"[ERREUR] {e}")

    def stop_wifi_direct(self, instance):
        self.log("[STOP] Fermeture du tunnel...")
        try:
            if self.wifi_p2p_manager and self.channel:
                self.wifi_p2p_manager.removeGroup(self.channel, None)
            self.status_label.text = "Statut : Inactif"
            self.log("[SUCCÈS] Connexion fermée.")
        except Exception as e:
            self.log(f"[ERREUR] {e}")

if __name__ == '__main__':
    BrainWiFiDirectApp().run()
