<?php
require_once 'config.php';

$json = array();
$email = isset( $_POST['email'] ) ? $_POST['email'] : '';
$name = isset( $_POST['name'] ) ? $_POST['name'] : '';
$message = isset( $_POST['message'] ) ? $_POST['message'] : '';

if( !$name ) {
    $json['error']['name'] = 'Please enter your full name.';
}
if( !$message ) {
    $json['error']['message'] = 'Please enter your message.';
}
if( !$email || !preg_match('/^[^\@]+@.*\.[a-z]{2,6}$/i', $email ) ) {
    $json['error']['email'] = 'Please enter your email address.';
}


// If no errors
if( !isset( $json['error'] ) ) {
    // Email text
    $mail_message = $name . "\r\n\r\n";
    $mail_message .= $message;
    // Email title
    $mail_headers  = "Content-type: text/plain; charset=utf-8\r\n";
    $mail_headers .= "From: {$email}\r\n";
    // Sending email
    mail( $to_email, $mail_subject, $mail_message, $mail_headers );
    $json['success'] = 'Your message was sent successfully!';
}

echo json_encode( $json );
?>