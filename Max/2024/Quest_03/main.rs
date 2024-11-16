use std::fs;

fn main()
{
    println!("<<< This is Quest 03 >>>");

    //let file_path = "../../../Input/Examples/Quest_03.txt";
    //let file_path = "../../../Input/Max/everybody_codes_e2024_q03_p1.txt";
    //let file_path = "../../../Input/Max/everybody_codes_e2024_q03_p2.txt";
    let file_path = "../../../Input/Max/everybody_codes_e2024_q03_p3.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Error regarding read_to_string");

   
    let rows = contents.split("\n").collect::<Vec<_>>();
    let row_len = rows.len();
    let column_len = &rows[0].chars().collect::<Vec<_>>().len();

    let mut matrix: Vec<Vec<char>> = Vec::with_capacity(row_len);

    //<<< create matrix >>>
    for i in 0..(row_len)
    {
        matrix.push(rows[i].chars().collect::<Vec<_>>());
    }
    
    //<<< print matrix >>>
    //print_matrix(&matrix);

    let mut print_flag = true;
    let mut print_iteration = 0;

    let mut count_removed = 0;

    // <<< edit matrix >>>
    while true == print_flag
    {
        if true == print_flag
        {           
            println!("Iteration: {}", print_iteration);
            print_matrix(&matrix);
            
            print_flag = false;
            print_iteration += 1;
        }

        for i in 0..(row_len)
        {
            for j in 0..(*column_len)
            {
                if '#' == matrix[i][j]
                {
                    matrix[i][j] = '1';
                    print_flag = true;

                    count_removed += 1;
                }
                else if 'f' == matrix[i][j]
                {
                    continue;
                }
                else if matrix[i][j].is_ascii_digit()
                {
                    if 0 == i || 0 == j
                    {
                        continue;
                    }
                    else if (row_len-1) == i || (*column_len-1) == j
                    {
                        continue;
                    } 

                    let mut number_deep = matrix[i][j].to_digit(16);

                    if matrix[i+1][j].is_ascii_digit()
                    {
                        let number_other = matrix[i+1][j].to_digit(16);
                        if number_other < number_deep
                        {
                            continue;
                        }
                    }
                    else
                    {
                        continue;
                    }
                    if matrix[i-1][j].is_ascii_digit()
                    {
                        let number_other = matrix[i-1][j].to_digit(16);
                        if number_other < number_deep
                        {
                            continue;
                        }
                    }
                    else
                    {
                        continue;
                    }
                    if matrix[i][j+1].is_ascii_digit()
                    {
                        let number_other = matrix[i][j+1].to_digit(16);
                        if number_other < number_deep
                        {
                            continue;
                        }
                    }
                    else
                    {
                        continue;
                    }
                    if matrix[i][j-1].is_ascii_digit()
                    {
                        let number_other = matrix[i][j-1].to_digit(16);
                        if number_other < number_deep
                        {
                            continue;
                        }
                    }
                    else
                    {
                        continue;
                    }
                    if matrix[i+1][j+1].is_ascii_digit()
                    {
                        let number_other = matrix[i+1][j+1].to_digit(16);
                        if number_other < number_deep
                        {
                            continue;
                        }
                    }
                    else
                    {
                        continue;
                    }
                    if matrix[i+1][j-1].is_ascii_digit()
                    {
                        let number_other = matrix[i+1][j-1].to_digit(16);
                        if number_other < number_deep
                        {
                            continue;
                        }
                    }
                    else
                    {
                        continue;
                    }
                    if matrix[i-1][j+1].is_ascii_digit()
                    {
                        let number_other = matrix[i-1][j+1].to_digit(16);
                        if number_other < number_deep
                        {
                            continue;
                        }
                    }
                    else
                    {
                        continue;
                    }
                    if matrix[i-1][j-1].is_ascii_digit()
                    {
                        let number_other = matrix[i-1][j-1].to_digit(16);
                        if number_other < number_deep
                        {
                            continue;
                        }
                    }
                    else
                    {
                        continue;
                    }

                    number_deep = number_deep.expect("Char conversion gone wrong!").checked_add(1);
                    let number_char = char::from_digit(number_deep.expect("Char conversion gone wrong!"), 16);

                    matrix[i][j] = number_char
                        .expect("Char conversion gone wrong!");
                        
                    print_flag = true;

                    count_removed += 1;
                }
            }
        }
    }
    
    //<<< print matrix >>>
    //print_matrix(&matrix);
    println!("Dirt removed: {}", count_removed);
}

fn print_matrix(matrix: & Vec<Vec<char>>)
{
    let row_len = matrix.len();
    let column_len = matrix[0].len();

    //<<< print matrix >>>
    for i in 0..(row_len)
    {
        for j in 0..(column_len)
        {
            print!("{}", matrix[i][j]);
        }
        println!("");
    }
}