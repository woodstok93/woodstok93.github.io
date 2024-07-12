(function(){
    
    const sliders = [...document.querySelectorAll('.pueblos__body')];
    const buttonNext = document.querySelector('#next');
    const buttonBefore = document.querySelector('#before');
    let value;   

    buttonNext.addEventListener('click', ()=>{
        changePosition(1);
    });
 
    buttonBefore.addEventListener('click', ()=>{
        changePosition(-1);
    });

    const changePosition = (add)=>{
        const currentPueblos = document.querySelector('.pueblos__body--show').dataset.id;
        value = Number(currentPueblos);
        value+= add;


        sliders[Number(currentPueblos)-1].classList.remove('pueblos__body--show');
        if(value === sliders.length+1 || value === 0){
            value = value === 0 ? sliders.length  : 1;
        }

        sliders[value-1].classList.add('pueblos__body--show');

    }

})();