# MI-038 — Green excess is Hardy-square energy of Fourier magnitudes

**Evidence level:** exact synthesis from [PC-325](../../findings/PC-325-green-relative-spectrum-is-phase-gauge-and-autocorrelation-only.md), [PC-327](../../findings/PC-327-band-normalized-green-defect-has-universal-schatten-divergence.md), [PC-330](../../findings/PC-330-smooth-li-profile-subtraction-preserves-canonical-green-hilbert-band.md), and [PC-331](../../findings/PC-331-band-normalized-green-defect-is-log-floor-plus-hardy-energy.md).

PC-327 gives a universal logarithmic lower floor for the band-normalized Green offset defect. PC-330 shows that subtracting the smooth Li/PNT profile does not remove the sparse source Hilbert channel. PC-331 identifies what measures the source-dependent excess above that floor.

For comparable conductors, the normalized Hilbert--Schmidt defect is equivalent up to absolute constants to

`log q + E_(q,r)(a,b)`,

with

`E_(q,r)(a,b) = [1/(mu(a)mu(b))] sum_(i,j) |a_hat(i)|^2 |b_hat(j)|^2/(i+j)^2`.

The kernel `(i+j)^(-2)` has a positive moment representation, so `E` is a Hankel/Hardy-square bilinear energy of the normalized Fourier magnitude-square profiles. It measures how strongly both sources concentrate near the low-frequency corner. Diffuse profiles contribute only logarithmic scale; concentrated profiles can create much larger excess.

This is a useful structural reduction because it separates the Green defect into two resources: a source-independent Hilbert floor and a positive source-sensitive concentration energy. But the source-sensitive term is still phase blind. It depends only on Fourier magnitudes, exactly as predicted by the PC-325 phase-gauge/autocorrelation quotient.

The next selectivity question can therefore be asked directly on `E`: is the prime-source magnitude profile constrained in a way that matched sparse non-arithmetic controls cannot reproduce, or does the Hardy-square excess remain another autocorrelation statistic with no zero-selective content? Any proposed renormalization should remove the universal logarithmic floor before interpreting `E`, and any arithmetic claim must compare against controls matching the relevant magnitude profile rather than only the smooth density.

**Boundary.** PC-331 does not derive a zeta-zero restriction from `E`, recover phase information, or prove prime-specific asymptotics for the Hardy-square energy. It identifies the exact positive source-sensitive coordinate controlling excess Green energy above the universal floor.