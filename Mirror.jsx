// Mirror horizontal antar dokumen (1 loop saja, tanpa loop pages, dengan deklarasi awal)
var refDoc = app.activeDocument;
var targetDoc = app.documents[1];

// Ambil lebar halaman dari halaman pertama (asumsi semua sama)
var pageWidth = targetDoc.pages[0].bounds[3] - targetDoc.pages[0].bounds[1];

// Ambil semua group dari ref dan target
var refGroups = refDoc.groups;
var targetGroups = targetDoc.groups;

// Deklarasi variabel di awal untuk efisiensi
var i, refGroup, targetGroup;
var refPos, targetPos;
var refRight, mirroredLeft, moveX, originalY;

// Pastikan jumlahnya sama
if (refGroups.length !== targetGroups.length) {
    alert("Jumlah group berbeda antara dokumen!");
} else {
    for (i = 0; i < refGroups.length; i++) {
        refGroup = refGroups[i];
        targetGroup = targetGroups[i];

        // Abaikan jika tidak ada nama
        if (!refGroup.name || !targetGroup.name) continue;

        // Hitung posisi mirror
        refPos = refGroup.geometricBounds;
        targetPos = targetGroup.geometricBounds;

        refRight = refPos[3];
        mirroredLeft = pageWidth - refRight;

        // Hitung jarak X yang perlu digeser
        moveX = mirroredLeft;

        // Simpan posisi Y asli agar tidak bergeser vertikal
        originalY = targetPos[0];

        // Pindahkan group
        targetGroup.move([moveX, originalY]);
    }
    alert("Done - Mirror dengan 1 loop dan deklarasi awal.");
}