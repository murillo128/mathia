# MI-033 — Relative Green spectrum factors through source autocorrelation

**Evidence level:** exact synthesis from [PC-323](../../findings/PC-323-cross-level-green-operator-is-hilbert-plus-trace-class.md), [PC-324](../../findings/PC-324-one-residue-green-controls-have-classical-hilbert-edge-zeros.md), [PC-325](../../findings/PC-325-green-relative-spectrum-is-phase-gauge-and-autocorrelation-only.md), and [PC-334](../../findings/PC-334-complemented-li-control-is-an-exact-binary-green-hardy-match.md).

Retaining the full cross-level Green operator does preserve more than its universal Hilbert band, but it does not preserve independent Fourier phase. For periodic source masks `a,b`, the PC-323 operator has the separable form

`X_(a,b)=D_a K_1 D_b`.

Writing each source as phase times modulus gives `X_(a,b)=U_a X_(|a|,|b|) U_b`. The self-adjoint dilation is therefore unitarily equivalent to the modulus version. PC-325 strengthens this from the absolute operator to the **relative pair**: the same block unitary simultaneously conjugates the full Green operator and its Hilbert comparison core.

Consequently the complete self-adjoint spectrum and every invariant of the relative pair that respects simultaneous unitary conjugacy — including the perturbation determinant, spectral shift and scattering conjugacy class where defined — factor through `(|a|,|b|)`. The trace-class defect may retain detailed periodic information, but not the phases removed by this gauge.

For the PC-316 finite Fourier sources, this quotient has an exact source interpretation. Finite Wiener--Khinchin identifies `|a|^2` with the cyclic autocorrelation of the first source and `|b|^2` with the cyclic autocorrelation of the second. Thus the complete Green/relative spectral package considered here factors through the two pair-autocorrelation functions.

This is stronger than saying one selected scalar is phase-blind. Conjugate-symmetric phase twists produce distinct real centered sources with exactly the same autocorrelation and therefore exactly the same Green spectrum and relative spectral invariants. Generic twists are not translations or reflections. The phase-sensitive multi-residue escape left after PC-323--PC-324 is therefore closed **inside the separable `D_a K_1 D_b` architecture**.

PC-334 closes an additional discrete-source loophole for the normalized magnitude branch. For a binary support mask and its literal complement, subtraction of the correspondingly complemented Li baseline makes the centered normalized residuals exact scalar negatives. Their normalized Fourier power is therefore identical. The same equality propagates to the band energies, dyadic Green--Hardy profile, cyclic window variance and the source-normalized two-level Green/Hilbert spectral data. A matched control need not leave the binary category: the literal nonprime complement already reproduces the entire normalized magnitude-only package.

The surviving information is now sharply located. A useful invariant inside this Green branch must either retain source information that is not annihilated by the autocorrelation quotient, such as genuinely nonseparable phase coupling, or use an amplitude/normalization that the complemented control cannot match. In either case it still needs an independent zero-sensitive destination theorem; spectral richness or a hard band estimate alone is not enough.

This tightens the matched-control standard. Magnitude-sensitive claims must survive exact autocorrelation controls, including the complemented binary control when the normalization admits it. Any phase-sensitive proposal must first prove that its construction is not simultaneously gauge-equivalent to its modulus version.

**Boundary.** PC-334 closes the literal binary/complement loophole only for the normalized magnitude branch. It does not rule out unnormalized source amplitude, source constraints that prevent the required complemented normalization, or genuinely nonseparable operators. Nor does any result here turn surviving source distinguishability into an RH zero selector.