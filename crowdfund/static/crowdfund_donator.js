function updateCollected(collected) {
    $("#collected").text(`${collected}`)
    $("#update").html(`<br>Donasi telah diberikan kepada penggalang. Terima kasih!`)
}

$(document).ready(function() {
    $.get(crowdfundUrl, function(fund) {
        $("head").append(`
          <title>${fund[0]["fields"]["title"]}</title>
        `)

        $("body").append(`
          <h1 class="text-center p-3">${fund[0]["fields"]["title"]}</h1>
          <div class="d-flex flex-row">
            <div class="p-3 flex-fill">
              <h5>Informasi Lebih Lanjut</h5>
              ${fund[0]["fields"]["description"]}
              <div class="text-success" id="update"></div>
            </div>
            <div class="p-3 flex-fill">
              <h5>Pengaju Galangan Dana</h5>
              ${fund[0]["fields"]["fundraiser_name"]}
              <br><br>
              <h5>Jumlah Dana Terkumpul</h5>
              <div id="collected">${fund[0]["fields"]["collected"]}</div>
              <br>
              <h5>Target Dana Terkumpul</h5>
              ${fund[0]["fields"]["target"]}
              <br><br>
              <h5>Batas Waktu Pengumpulan Dana</h5>
              ${fund[0]["fields"]["deadline"]}
              <br><br>
              <a class="btn border" data-bs-toggle="modal" data-bs-target="#form">Kumpulkan Donasi</a>
            </div>
          </div>
        `)
    })

    $("form").submit(function(event) {
      event.preventDefault()
      var form = {
          amount: $("#amount").val(),
          comment: $("#comment").val(),
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      }
    
      $.post(addDonationUrl, form, function(crowdfund) {
          if (!("error" in crowdfund)) {
              updateCollected(crowdfund[0]["fields"]["collected"])
              $("#form").modal("hide")
              $("form").trigger("reset")
              $("#error").html(``)
          } else {
              $("#error").html(`Pastikan isian formulir memenuhi ketentuan.<br><br>`)
          }
      }, "json")
    
      $("#form").on("hidden.bs.modal", function() {
          $("form").trigger("reset")
          $("#error").html(``)
      })
  })
})