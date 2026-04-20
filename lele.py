import random

def pull_signal_search():
    roll = random.uniform(0, 100)
    
    s_rank_agents = [
        "Von Lycaon", "Nekomata", "Grace Howard", "Alexandrina (Rina)", "Koleda Belobog", "Soldier 11",
        # Limited Banner
        "Ellen Joe", "Zhu Yuan", "Qingyi", "Jane Doe", "Caesar King", "Burnice White", 
        "Tsukishiro Yanagi", "Lighter", "Hoshimi Miyabi", "Asaba Harumasa", "Evelyn Chevalier", "Astra Yao", "Soldier 0 Anby", "Trigger", "Vivian Banshee", "Hugo Vlad", "Yixuan", "Ju Fufu", "Ukinami Yuzuha", "Alice Thymefield", "Seed", "Orphie & Magus", "Lucia", "Yidhari", "Dialyn", "Banyue", "Ye Shunguang", "Zhao", "Sunna", "Aria", "Nangong Yu", "Cissia"
    ]
    
    a_rank_agents = [
        "Anby Demara", "Nicole Demara", "Billy Kid", "Corin Wickes", 
        "Soukaku", "Anton Ivanov", "Ben Bigger", "Lucy", "Piper Wheel", "Seth Lowell", "Pan Yinhu", "Komano Manato"
    ]
    
    if roll <= 0.6:
        result = random.choice(s_rank_agents)
        return f"S-Rank: {result} !!!"
    elif roll <= 10.0:
        result = random.choice(a_rank_agents)
        return f"A-Rank: {result}"
    else:
        return "B-Rank: W-Engine Biasa"

def main():
    print("=== Terminal Signal Search ZZZ ===")
    while True:
        print("\n1. Tarik 1x")
        print("2. Tarik 10x")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '3':
            print("Meninggalkan terminal...")
            break
            
        if pilihan == '1':
            print(f"\nHasil: {pull_signal_search()}")
        elif pilihan == '2':
            print("\nHasil Pull 10x:")
            for _ in range(10):
                print(pull_signal_search())
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
