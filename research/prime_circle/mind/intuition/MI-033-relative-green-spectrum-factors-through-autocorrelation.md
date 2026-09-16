# MI-033 — Relative Green spectrum factors through source autocorrelation

**Evidence level:** exact synthesis from [PC-323](../../findings/PC-323-cross-level-green-operator-is-hilbert-plus-trace-class.md), [PC-324](../../findings/PC-324-one-residue-green-controls-have-classical-hilbert-edge-zeros.md), and [PC-325](../../findings/PC-325-green-relative-spectrum-is-phase-gauge-and-autocorrelation-only.md).

Retaining the full cross-level Green operator does preserve more than its universal Hilbert band, but it does not preserve independent Fourier phase. For periodic source masks `a,b`, the PC-323 operator has the separable form

`X_(a,b)=D_a K_1 D_b`.

Writing each source as phase times modulus gives `X_(a,b)=U_a X_(|a|,|b|) U_b`. The self-adjoint dilation is therefore unitarily equivalent to the modulus version. PC-325 strengthens this from the absolute operator to the **relative pair**: the same block unitary simultaneously conjugates the full Green operator and its Hilbert comparison core.

Consequently the complete self-adjoint spectrum and every invariant of the relative pair that respects simultaneous unitary conjugacy — including the perturbation determinant, spectral shift and scattering conjugacy class where defined — factor through `(|a|,|b|)`. The trace-class defect may retain detailed periodic information, but not the phases removed by this gauge.

For the PC-316 finite Fourier sources, this quotient has an exact source interpretation. Finite Wiener--Khinchin identifies `|a|^2` with the cyclic autocorrelation of the first source and `|b|^2` with the cyclic autocorrelation of the second. Thus the complete Green/relative spectral package considered here factors through the two pair-autocorrelation functions.

This is stronger than saying one selected scalar is phase-blind. Conjugate-symmetric phase twists produce distinct real centered sources with exactly the same autocorrelation and therefore exactly the same Green spectrum and relative spectral invariants. Generic twists are not translations or reflections. The phase-sensitive multi-residue escape left after PC-323--PC-324 is therefore closed **inside the separable `D_a K_1 D_b` architecture**.

The surviving information is now sharply located. A useful invariant inside this Green branch must distinguish arithmetic sources using their magnitude/autocorrelation data themselves. If the desired discriminator genuinely needs oriented Fourier phase, the operator must couple phases nonseparably before the unitary quotient — for example through higher-order polyspectral products, source-dependent index coupling, or another kernel not reducible to independent left/right diagonal factors.

This also tightens the matched-control standard. It is not enough to compare with one-residue generalized-Hilbert controls. Any magnitude-sensitive claim should be tested against non-arithmetic sources with the same cyclic autocorrelation, while any phase-sensitive proposal must first prove that its construction is not simultaneously gauge-equivalent to its modulus version.

**Boundary.** PC-325 does not show that Prime-Circle autocorrelations are trivial, does not classify magnitude-sensitive multi-residue spectrum, and does not cover source classes in which phase-twisted controls are forbidden by additional discrete constraints. Nor does it cover genuinely nonseparable operators. The exact conclusion is that the full PC-323 Green operator and its canonical relative Hilbert pair cannot use independent source Fourier phase as an RH carrier.