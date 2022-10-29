function appendCrowdfund(id, title, fundraiser_name, collected, target, deadline) {
    $("#crowdfunds").append(`
      <div class="col-sm-6 col-md-4 p-3">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">${title}</h5>
            <h6 class="card-subtitle text-muted">Digalang oleh ${fundraiser_name}</h6>
            <hr>
            <ul>
              <li>${collected} terkumpul</li>
              <li>${target} dibutuhkan</li>
              <li>Batas pengumpulan: ${deadline}</li>
            </ul>
            <a href="http://localhost:8000/crowdfund/${id}" class="btn border">Lihat Detail</a>
          </div>
        </div>
      </div>
    `)
}

$(document).ready(function() {
    $.get("http://localhost:8000/crowdfund/funds/json/ongoing/", function(crowdfunds) {
        if (crowdfunds.length != 0) {
            $("#no-crowdfunds").hide()
            for (const fund of crowdfunds) {
                appendCrowdfund(
                    fund["pk"],
                    fund["fields"]["title"],
                    fund["fields"]["fundraiser_name"],
                    fund["fields"]["collected"],
                    fund["fields"]["target"],
                    fund["fields"]["deadline"]
                )
            }
        }
    }, "json")
})