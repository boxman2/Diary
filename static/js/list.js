// 함수 정의
        <!--카드 붙이는 ajax -->
        function q1() {
            $("#cards-box").empty();
            $("#MDALBOX").empty();



            $.ajax({
                type: "GET",
                url: "/api/post",
                data: {},
                success: function (response) {
                    let rows = response['Diary'];

                    for (let i = 0; i < rows.length; i++) {
                        let Id = rows[i]["id"];
                        let IsSecret = rows[i]["isSecret"];
                        let Likes = rows[i]["like"];
                        let write = rows[i]["write"];
                        let WriteDate = rows[i]["date"];
                        let State = rows[i]["state"];
                        let image = rows[i]["img"];
                        let title = rows[i]["title"];


                        if (IsSecret == 0 || IsSecret == "false") {
                            let cards_html = `<div class="col">
                                                            <div class="card">

                                                                  <div class="btn1" onclick="" >(${Likes})❤</div>
                                                                  <img src="${image}" class="card-img-top" alt="...">
                                                                  <div class="card-body">
                                                                    <h5 class="card-title">${title} / ${State}</h5>
                                                                    <p class="card-text">${write} <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal${i}">click+</button></p>

                                                                    <div class="info-User">별명: ${Id} / 날짜: ${WriteDate}</div>

                                                                  </div>



                                                            </div>
                                                          </div>`;

                            let MD_html = `            <div class="modal fade" id="exampleModal${i}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                                          <div class="modal-dialog modal-dialog-scrollable">
                                                            <div class="modal-content">
                                                              <div class="modal-header">
                                                                <h1 class="modal-title fs-5" id="exampleModalLabel">${title}</h1>
                                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                                              </div>
                                                              <div class="modal-body">
                                                                ${write}
                                                              </div>
                                                              <div class="modal-footer">

                                                              </div>
                                                            </div>
                                                          </div>
                                                        </div>`;




                            $("#cards-box").append(cards_html);
                            $("#MDALBOX").append(MD_html);

                        }


                    }
                },
            });
        }



         <!--카드 붙이는 ajax -->
        function myq1() {
            $("#cards-box").empty();
            $("#MDALBOX").empty();



            $.ajax({
                type: "GET",
                url: "/api/post",
                data: {},
                success: function (response) {
                    let rows = response['Diary'];

                    for (let i = 0; i < rows.length; i++) {
                        let Id = rows[i]["id"];
                        //if(ID != ~~~){ continue; };
                        let IsSecret = rows[i]["isSecret"];
                        let Likes = rows[i]["like"];
                        let write = rows[i]["write"];
                        let WriteDate = rows[i]["date"];
                        let State = rows[i]["state"];
                        let image = rows[i]["img"];
                        let title = rows[i]["title"];



                        let cards_html = `<div class="col">
                                                        <div class="card">

                                                              <div class="btn1" onclick="" >(${Likes})❤</div>
                                                              <img src="${image}" class="card-img-top" alt="...">
                                                              <div class="card-body">
                                                                <h5 class="card-title">${title} / ${State}</h5>
                                                                <p class="card-text">${write} <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal${i}">click+</button></p>

                                                                <div class="info-User">별명: ${Id} / 날짜: ${WriteDate}</div>

                                                              </div>



                                                        </div>
                                                      </div>`;

                        let MD_html = `            <div class="modal fade" id="exampleModal${i}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                                      <div class="modal-dialog modal-dialog-scrollable">
                                                        <div class="modal-content">
                                                          <div class="modal-header">
                                                            <h1 class="modal-title fs-5" id="exampleModalLabel">${title}</h1>
                                                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                                          </div>
                                                          <div class="modal-body">
                                                            ${write}
                                                          </div>
                                                          <div class="modal-footer">

                                                          </div>
                                                        </div>
                                                      </div>
                                                    </div>`;




                        $("#cards-box").append(cards_html);
                        $("#MDALBOX").append(MD_html);




                    }
                },
            });
        }








        <!--함수 호출 -->
        q1()
