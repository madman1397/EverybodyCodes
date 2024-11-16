use std::fs;
use std::collections::HashMap;

fn main()
{
    println!("<<< This is Quest 02 >>>");

    let file_path = "../../../Input/Examples/Quest_02.txt";
    //let file_path = "../../../Input/Max/everybody_codes_e2024_q02_p1.txt";
    //let file_path = "../../../Input/Max/everybody_codes_e2024_q02_p2.txt";
    //let file_path = "../../../Input/Max/everybody_codes_e2024_q02_p3.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Error using read_to_string");

    //println!("{contents}");

    let mut runes_flag = false;
    let mut runes = String::from("");
    let mut runes_hash : HashMap<String, i32> = HashMap::new();

    let mut text_flag = false;
    let mut three_char_buffer = String::from("000");
    //let mut two_char_buffer;

    let mut count_runes = 0;

    for letter in contents.chars()
    {
        // <<< collect the possible runes >>>
        if false == text_flag
        {
            if ('#' == letter) && (true == runes_flag)
            {
                runes_hash.insert(runes.clone(), 0);
                runes.clear();

                runes_flag = false;
                text_flag = true;

                break;
            }
            else if (':' == letter) && (false == runes_flag)
            {
                runes_flag = true;
            }
            else if true == runes_flag
            {
                if ',' == letter
                {
                    runes_hash.insert(runes.clone(), 0);
                    runes.clear();
                }
                else
                {
                    //println!("Test:\n{letter}");
                    runes.push(letter);
                }
            }
        }

        // <<< check for runes in text >>>
        /*
        if true == text_flag
        {
            three_char_buffer.remove(0);
            three_char_buffer.push(letter);
            two_char_buffer = three_char_buffer[1..].to_string();

            //println!("{two_char_buffer}");
            //println!("{three_char_buffer}");

            if let Some(count) = runes_hash.get_mut(&three_char_buffer.to_string()) 
            { 
                *count += 1
            }
            if let Some(count) = runes_hash.get_mut(&two_char_buffer.to_string()) 
            { 
                *count += 1
            }
        }
        */

    }
    
    let mut skip_flag = false;
    let lines = contents.split("\n");
    for line in lines
    {
        if false == skip_flag
        {
            skip_flag = true;
            continue;
        }
        //println!("{line}");

        // <<< search line forwards >>>
        for (key, value) in &mut runes_hash
        {
            runes.clear();
            let rune_len = key.len();
            let mut rune_count = 0;
            
            for letter in line.chars()
            {
                runes.push(letter);
                rune_count += 1;

                if rune_count >= rune_len
                {
                    //println!("{runes}");
                    if runes == *key
                    {
                        *value += 1;
                    }

                    runes.remove(0);
                }
            }
        }

        // <<< search line reversed >>>
        let line_rev = line.chars().rev().collect::<String>();
        println!("{line}");
        println!("{line_rev}");
        for (key, value) in &mut runes_hash
        {
            runes.clear();
            let rune_len = key.len();
            let mut rune_count = 0;
            
            for letter in line_rev.chars()
            {
                runes.push(letter);
                rune_count += 1;

                if rune_count >= rune_len
                {
                    //println!("{runes}");
                    if runes == *key
                    {
                        *value += 1;
                    }

                    runes.remove(0);
                }
            }
        }
    }

    for (key, value) in &runes_hash 
    {
        println!("{key}: {value}");
        count_runes += *value;
    }
    println!("{count_runes}");

}