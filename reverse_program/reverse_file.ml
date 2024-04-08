class word_reverser =
  object (self)
    method reverse_word word =
      let len = String.length word in
      let rec reverse_chars i rev_s =
        if i < 0 then rev_s
        else reverse_chars (i - 1) (rev_s ^ (String.make 1 word.[i]))
      in reverse_chars (len - 1) ""

    method reverse_line line =
      let words = String.split_on_char ' ' line in
      let reversed_words = List.map self#reverse_word words in
      String.concat " " reversed_words

    method process_line line =
      if String.length line = 0 then line (* Keep empty lines as they are *)
      else self#reverse_line line

    method process_input () =
      try
        while true do
          let line = input_line stdin in
          let processed_line = self#process_line line in
          print_endline processed_line
        done
      with End_of_file -> ()
  end

(* Entry point *)
let () =
  let reverser = new word_reverser in
  reverser#process_input ()
