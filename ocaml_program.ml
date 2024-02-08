(* RISC-V Cryptography Example: Caesar Cipher in OCaml *)
let shift_char c shift =
  if Char.code 'a' <= Char.code c && Char.code c <= Char.code 'z' then
    Char.chr (((Char.code c - Char.code 'a' + shift + 26 * 1000) mod 26) + Char.code 'a')
  else if Char.code 'A' <= Char.code c && Char.code c <= Char.code 'Z' then
    Char.chr (((Char.code c - Char.code 'A' + shift + 26 * 1000) mod 26) + Char.code 'A')
  else
    c

let caesar_cipher str shift =
  String.map (fun c -> shift_char c shift) str

let () =
  let plaintext = "RISC-V Cryptography program" in
  let shift_amount = 4 in

  (* Encryption *)
  let ciphertext = caesar_cipher plaintext shift_amount in
  Printf.printf "Original: %s\n" plaintext;
  Printf.printf "Encrypted: %s\n" ciphertext;

  (* Decryption *)
  let decrypted_text = caesar_cipher ciphertext (-shift_amount) in
  Printf.printf "Decrypted: %s\n" decrypted_text


  (* test class *)
  module CaesarCipherTests = struct
    let run_tests () =
      let assert_equal expected actual message =
        if expected = actual then
          Printf.printf "PASS: %s\n" message
        else
          Printf.printf "FAIL: %s\nExpected: %s\nActual: %s\n" message expected actual
      in
  
      let test_encrypt_decrypt plaintext shift_amount =
        let ciphertext = caesar_cipher plaintext shift_amount in
        let decrypted_text = caesar_cipher ciphertext (-shift_amount) in
        assert_equal plaintext decrypted_text "Encryption/Decryption test"
      in
      (* test cases *)
      let test_edge_cases () =
        test_encrypt_decrypt "" 5;
  
        test_encrypt_decrypt "Hello" 0;
  
        test_encrypt_decrypt "Testing" 40;
  
        test_encrypt_decrypt "Testing" (-100);
  
        test_encrypt_decrypt "AbCdEfGhIjK" 3;
      in
  
      let test_invalid_characters () =
        (* Test with non-alphabetic characters *)
        let ciphertext = caesar_cipher "123!@#" 2 in
        assert_equal "123!@#" ciphertext "Encryption of non-alphabetic characters";
      in
  
      (* Run the tests *)
      test_edge_cases ();
      test_invalid_characters ();
    end
  ;;
  
  (* Run the tests when the module is loaded *)
  CaesarCipherTests.run_tests ();
  