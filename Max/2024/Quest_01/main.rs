use std::fs;

fn main()
{
    println!("<<< This is Quest 01 >>>");

    //let file_path = "../../../Input/Examples/Quest_01.txt";
    //let file_path = "../../../Input/Max/everybody_codes_e2024_q01_p1.txt";
    //let file_path = "../../../Input/Max/everybody_codes_e2024_q01_p2.txt";
    let file_path = "../../../Input/Max/everybody_codes_e2024_q01_p3.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Error regarding read_to_string");

    let mut result = 0;

    let mut fight = 0;
    let mut monster_counter = 0;
    let mut x_count = 0;

    for letter in contents.chars()
    {
        // track potion usage
        if 'A' == letter
        {
            fight += 0;
        }
        else if 'B' == letter
        {
            fight += 1;
        }
        else if 'C' == letter
        {
            fight += 3;
        }
        else if 'D' == letter
        {
            fight += 5;
        }
        else if 'x' == letter
        {
            x_count += 1;
        }

        // track monsters for a fight
        monster_counter += 1;

        // conlcude fight if 2 monsters added to fight (or an x and a monster)
        if 3 == monster_counter
        {
            if 0 == x_count
            {
                fight += 6;
            }
            else if 1 == x_count
            {
                fight += 2;
            }
            else if 2 == x_count
            {
                fight += 0;
            }

            if 0 > fight
            {
                fight = 0;
            }

            result += fight;

            fight = 0;
            monster_counter = 0;
            x_count = 0;
        }

    }

    println!{"Solution: {result}"};
}