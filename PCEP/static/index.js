const grade_test = async () => {

    const result = []
    
    const question_divs = Array(...document.querySelector("#test").getElementsByClassName("box")); //los tres ... son como el * en Python para desempaquetar
    question_divs.forEach((question) => {
        const radios = Array(...question.getElementsByTagName("input"));
        const q_id = radios[0].name;
       
        let radio_check = false;
        for (radio of radios) {
            if (radio.checked) {radio_check = radio.value};

        };
        result.push([q_id, radio_check])
        
        // console.log(radio_filter)
        // radio_map=[]
        // for (radio of radio_filter) {radio_map.push(radio.value)};
        // result.push([q_id,radio_map[0]])
        
        // const radio_check = radios.filter((radio) => radio.checked).map((radio) => radio.value);
        // result.push([q_id, radios[0].name, radio_check[0] ? radio_check[0] : false])
    });
   

    const res = await fetch("http://localhost:5000/tests/api/grade" , {
        headers: {
            "content-type": "application/json",
        },
        method:"POST",
        body: JSON.stringify(result),
    });

    const data = await res.json();
    // console.log(data)
    // Object.entries(data.answers).forEach((opID_bool))  ó below
    // console.log(data.answers)
    for (qID_bool of Object.entries(data.answers)) {
        // console.log(qID_bool)
        radio = document.getElementById(qID_bool[0]);
       
        
        let radio_container = radio.parentElement;
        
        qID_bool[1] ? radio_container.style.backgroundColor = "#69ff69"  : radio_container.style.backgroundColor = "#ff6464";
    };
    
    document.getElementById("grade").innerText = `Grade: ${data.grade}`;
    const try_a = document.getElementById("try");
    try_a.innerText = "Try again!"

};

function alert_f() {
    alert("You will be logged out");
};
// var countdown = (Date().now) + fifteen_mins
// const count_down = () => {
    
//     const starting = setInterval(() => {
//         var distance = (15 * 60 * 1000)
//         var mins =  Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
//         var seconds = Math.floor((distance % (1000 * 60)) / 1000);
//         document.getElementById("start").innerText = mins + "mins" + seconds + "secs" 
//         if (distance < 0) {
//             clearInterval(starting);
//             document.getElementById("start").innerText = "TIME UP"
//         }
        
//         }, 1000);
// };

   
        

const count_down = () => {
    var test_time = 60*15;//
    var start_timer = setInterval(() =>{
        test_time -- ;
        var minutes = Math.floor((test_time % ( 60 * 60)) / ( 60)); 
        var seconds = Math.floor((test_time % ( 60)) / 1);
        console.log(seconds)
        document.getElementById("start").innerText = `${minutes} mins ${seconds} secs`
        if (test_time < 0) {
            clearInterval(start_timer); 
            document.getElementById("start").innerText = "TIME's UP!"
        }
    },1000)
};

