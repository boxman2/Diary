
        $(document).ready(function () {
            show_order();
        });

        function generateRandomId() {
            return '_' + Math.random().toString(36).substr(2, 9)
        }

        function show_order() {
            $.ajax({
                type: 'GET',
                url: '/post',
                data: {},
                success: function (response) {
                    let rows = response['diary']
                    for (let i = 0; i < rows.length; i++) {
                        let date = rows[i]['date']
                        let id = rows[i]['id']
                        let title = rows[i]['title']
                        let state = rows[i]['state']
                        let img = rows[i]['img']
                        let write = rows[i]['write']
                        let isSecret = rows[i]['isSecret']

                        let temp_html = `<tr>
                                    <td>${date}</td>
                                    <td>${id}</td>
                                    <td>${title}</td>
                                    <td>${state}</td>
                                    <td>${img}</td>
                                    <td>${write}</td>
                                    <td>${isSecret}</td>
                                  </tr>`
                        $('#order-box').append(temp_html)
                    }
                }
            });
        }


        function save_comment() {

                let id = $('#id').val()
                let state = $('#state').val()
                let title = $('#title').val()
                let write = $('#write').val()
                let img = $('#img').val()
                let isSecret = $('#isSecret').is(":checked")
                let date = $('#date').val()
                let like = $('#like').val()
                let num = generateRandomId

                $.ajax({
                    type: 'POST',
                    url: '/post',
                    data: {
                        num_give: num,
                        date_give: date,
                        id_give: id,
                        state_give: state,
                        title_give: title,
                        write_give: write,
                        img_give: img,
                        isSecret_give: isSecret,
                        like_give: like
                    },
                    success: function (response) {
                        alert(response['msg'])
                        window.location.reload()
                    }
                });
        }
