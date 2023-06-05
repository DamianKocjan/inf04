using System;
using System.CodeDom;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace desktopowa
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private string password;

        public MainWindow()
        {
            InitializeComponent();

            Position.Items.Add("Kierownik");
            Position.Items.Add("Starszy programista");
            Position.Items.Add("Młodszy programista");
            Position.Items.Add("Tester");
        }

        /**********************************************
        nazwa funkcji: GeneratePassword
        opis funkcji: generuje hasło na podstawie wybranych opcji
        parametry: -
        zwracany typ i opis: void
        autor: 11111111111
        ***********************************************/
        private void GeneratePassword()
        {
            if (NumOfChars.Text.Length == 0)
            {
                return;
            }

            string chars = "";

            if ((bool)LowerAndUpperChars.IsChecked)
            {
                chars += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
            }

            if ((bool)Digits.IsChecked)
            {
                chars += "0123456789";
            }

            if ((bool)SpecialChars.IsChecked)
            {
                chars += "!@#$%^&*()_+-=";
            }

            string password = "";
            int length = int.Parse(NumOfChars.Text);

            Random random = new Random();
            
            for (int i = 0; i < length; i++)
            {
                password += chars[random.Next(chars.Length)];
            }

            this.password = password;
        }

        /**********************************************
        nazwa funkcji: Button_ClickGeneratePassword
        opis funkcji: obsługuje kliknięcie przycisku "Generuj hasło"
                      Wyświetla hasło w MessageBoxie.
        parametry: sender - obiekt, który wywołał funkcję
                   e - argumenty zdarzenia
        zwracany typ i opis: void
        autor: 11111111111
        ***********************************************/
        private void Button_ClickGeneratePassword(object sender, RoutedEventArgs e)
        {
            GeneratePassword();

            if (string.IsNullOrEmpty(password))
            {
                return;
            }
            
            MessageBox.Show(password, "", MessageBoxButton.OK);
        }

        /**********************************************
        nazwa funkcji: Button_ClickSubmit
        opis funkcji: obsługuje kliknięcie przycisku "Zatwierdź".
                      Wyświetla dane pracownika i hasło w MessageBoxie.
        parametry: sender - obiekt, który wywołał funkcję
                   e - argumenty zdarzenia
        zwracany typ i opis: void
        autor: 11111111111
        ***********************************************/
        private void Button_ClickSubmit(object sender, RoutedEventArgs e)
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("Dane pracownika: ");
            sb.Append(FirstName.Text);
            sb.Append(" ");
            sb.Append(LastName.Text);
            sb.Append(" ");
            sb.Append(Position.SelectedItem);
            sb.Append(" Hasło: ");
            sb.Append(password);

            MessageBox.Show(sb.ToString(), "", MessageBoxButton.OK);
        }
    }
}
