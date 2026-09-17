# MI-038 — Green excess is a dyadic Hardy-square energy of Fourier magnitudes

**Evidence level:** exact synthesis from [PC-325](../../findings/PC-325-green-relative-spectrum-is-phase-gauge-and-autocorrelation-only.md), [PC-327](../../findings/PC-327-band-normalized-green-defect-has-universal-schatten-divergence.md), [PC-330](../../findings/PC-330-smooth-li-profile-subtraction-preserves-canonical-green-hilbert-band.md), [PC-331](../../findings/PC-331-band-normalized-green-defect-is-log-floor-plus-hardy-energy.md), and [PC-332](../../findings/PC-332-green-hardy-excess-is-dyadic-low-frequency-square-function.md).

PC-327 gives a universal logarithmic lower floor for the band-normalized Green offset defect. PC-330 shows that subtracting the smooth Li/PNT profile does not remove the sparse source Hilbert channel. PC-331 identifies what measures the source-dependent excess above that floor.

For comparable conductors, the normalized Hilbert--Schmidt defect is equivalent up to absolute constants to

`log q + E_(q,r)(a,b)`,

with

`E_(q,r)(a,b) = [1/(mu(a)mu(b))] sum_(i,j) |a_hat(i)|^2 |b_hat(j)|^2/(i+j)^2`.

The kernel `(i+j)^(-2)` has a positive moment representation, so `E` is a Hankel/Hardy-square bilinear energy of the normalized Fourier magnitude-square profiles. It measures how strongly both sources concentrate near the low-frequency corner. Diffuse profiles contribute only logarithmic scale; concentrated profiles can create much larger excess.

PC-332 makes this concentration statement exact at dyadic resolution. Define

`Gamma_a(H)=[1/(H mu(a))] sum_(1<=i<=H)|a_hat(i)|^2`.

Then, up to absolute constants,

`E_(q,r)(a,b) asymp sum_m Gamma_a(2^m) Gamma_b(2^m)`.

The Hardy excess is therefore a positive low-frequency square function. If every dyadic cumulative magnitude profile is uniformly bounded, the entire excess is only `O(log q)`. Any superlogarithmic excess must force at least one dyadic scale where normalized Fourier energy is anomalously concentrated. This turns a global double sum into a concrete multiscale diagnostic.

The reduction is useful because it separates three resources: the source-independent Hilbert floor, source-sensitive magnitude concentration, and the distribution of that concentration across scales. But PC-325 remains decisive: all of these quantities are phase blind. A source or matched control with the same Fourier magnitude profile has the same `Gamma` sequence and the same Hardy excess.

The next selectivity question can therefore be asked scale by scale: does the prime source force a dyadic magnitude-concentration law that matched sparse non-arithmetic controls cannot reproduce, or does every observed excess remain inside the autocorrelation quotient? Any proposed renormalization should remove the universal logarithmic floor before interpreting `E`, and any arithmetic claim must compare against controls matching the relevant dyadic magnitude profile rather than only the smooth density.

**Boundary.** PC-331--PC-332 do not derive a zeta-zero restriction from `E`, recover phase information, or prove prime-specific asymptotics for the dyadic concentration profile. They identify the exact positive source-sensitive coordinate controlling excess Green energy above the universal floor and the scales on which any superlogarithmic excess must live.