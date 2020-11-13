function sendMail(contactForm){
    emailjs.send("gmail", "Holiday in Ireland", {
        "from_name":contactForm.from_name.value,
        "from_email": contactForm.from_email.value, 
        "holiday_ire": contactForm.holiday_ire.value,
        "message_ire": contactForm.message_ire.value,
        "gridRadios1": contactForm.gridRadios1.value,
        "number_people": contactForm.number_people.value,
        "transport_mode": contactForm.transport_mode.value
    })
    .then(
        function(response){
            console.log("SUCCESS", response);
            $('#contactForm').trigger("reset");
        },
        function(error){
            console.log("FAILED", error);
        });
return false;
}