const deleteButtons = document.querySelectorAll('.delete-btn');
    
deleteButtons.forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault();
        const confirmDelete = confirm('¿Desea borrar la reserva?');

        if (confirmDelete) {
            const reservaId = button.getAttribute('data-id');
            const deleteUrl = `/reservas/destroy/${reservaId}`;
            window.location.href = deleteUrl;
        }
    });
});