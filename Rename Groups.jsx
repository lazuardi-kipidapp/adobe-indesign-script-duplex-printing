/*
Rename Outer Groups in Active InDesign Document
by ChatGPT (GPT-5)
*/

(function() {
    if (app.documents.length === 0) {
        alert("Tidak ada dokumen terbuka.");
        return;
    }

    var doc = app.activeDocument;
    var allGroups = doc.groups;
    if (allGroups.length === 0) {
        alert("Tidak ada group di dokumen ini.");
        return;
    }

    // Fungsi untuk cek apakah group ini terluar (tidak berada di dalam group lain)
    function isTopLevelGroup(g) {
        return !(g.parent instanceof Group);
    }

    var count = 0;
    for (var i = 0; i < allGroups.length; i++) {
        var g = allGroups[i];
        if (isTopLevelGroup(g)) {
            count++;
            // Nama unik, misal "Card_001", "Card_002", dst
            var newName = "Card_" + ("000" + count).slice(-3);
            g.name = newName;
        }
    }

    alert("Selesai! " + count + " group terluar telah dinamai ulang.");
})();
