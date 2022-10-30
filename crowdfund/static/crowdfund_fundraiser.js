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
            </div>
            <div class="p-3 flex-fill">
              <h5>Pengaju Galangan Dana</h5>
              ${fund[0]["fields"]["fundraiser_name"]}
              <br><br>
              <h5>Jumlah Dana Terkumpul</h5>
              ${fund[0]["fields"]["collected"]}
              <br><br>
              <h5>Target Dana Terkumpul</h5>
              ${fund[0]["fields"]["target"]}
              <br><br>
              <h5>Batas Waktu Pengumpulan Dana</h5>
              ${fund[0]["fields"]["deadline"]}
              <br><br>
              <a class="btn border" data-bs-toggle="modal" data-bs-target="#history">Donasi Terkumpul</a>
            </div>
          </div>
        `)
    }, "json")

    $.get(donationUrl, function(donations) {
        if (donations.length != 0) {
            $("#no-donations").hide()
            for (const donation of donations) {
                $("#donations").append(`
                  <h6>${donation["fields"]["donator_name"]} mendonasikan ${donation["fields"]["amount"]}</h6>
                  <p>${donation["fields"]["comment"]}</p>
                `)
            }
        }
    }, "json")
})