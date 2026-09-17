# MI-042 — Euler Fourier fingerprints give a source-native complexity certificate

**Evidence level:** exact synthesis from [NB-175](../../findings/NB-175-joint-capped-transport-witnesses-certify-source-resolved-linear-complexity.md) and [NB-176](../../findings/NB-176-euler-weighted-fourier-fingerprints-certify-source-complexity.md), with the capped-Poisson source resolution of NB-167 and the approximate-complexity currency of NB-174.

NB-175 turns a jointly contractive family of capped-Poisson probes into a nuclear-response lower bound for the approximate stationary source complexity `mathfrak L_T(epsilon)`. Its remaining freedom is the probe family: a large certificate could in principle depend on an artificial observable chosen after seeing the templates.

NB-176 supplies a canonical family from the arithmetic source itself. On the exterior line `Re s=1+a`, write

`c_(n,a)=Lambda(n)n^(-1-a)`

and normalize the real sine/cosine feature map at frequencies `log n` by

`Z_a=max{2 sqrt(sum c_(n,a)^2), a sqrt(sum c_(n,a)^2(log n)^2)}`.

The normalization satisfies `Z_a=Theta(1)` uniformly for `0<a<=1`, and the resulting infinite Hilbert feature map `F_a(u)` obeys

`||F_a(u)-F_a(v)||_2 <= min{1,|u-v|/a}`.

Thus the complete collection of Euler modes fits inside one capped-Poisson dual budget; adding more Euler frequencies does not create free witness power.

For realized templates `nu_1,...,nu_N`, let `G^Eul` be the Gram matrix of their normalized responses to those Euler features. Explicitly its entries are the squared-Euler-amplitude sum

`G^Eul_(ij)=(q^2 Z_a^2)^(-1) sum_(n>=2) Lambda(n)^2 n^(-2-2a) Re(hat nu_i(log n) overline(hat nu_j(log n)))`.

Applying NB-175 to finite truncations and passing to the limit gives

`mathfrak L_T(epsilon) >= (tr sqrt(G^Eul)-epsilon N)_+^2/N`.

In particular, `G^Eul >= alpha^2 I_N` forces `mathfrak L_T(epsilon) >= N(alpha-epsilon)_+^2`. Many mutually nondegenerate fingerprints at the source resolution therefore certify linearly growing approximate source complexity without optimizing over an arbitrary Lipschitz witness.

The source-native point is exact. For every stationary zero-mass template, the same Fourier coefficients occur term by term in the absolutely convergent Euler expansion of `zeta'/zeta` on `Re s>1`. The certificate is therefore measuring the individual mode amplitudes that the actual source coherently sums, including prime powers automatically through `Lambda`.

The conceptual split remains important. **Source-visible geometric complexity is not yet coherent arithmetic rescue.** `G^Eul` measures the `ell^2` geometry of Euler fingerprints, whereas the logarithmic derivative combines those amplitudes with the scalar phases `n^(-it)`. A large Gram certificate proves that no low-complexity stationary representation can approximate the realized template family at the declared source resolution; it does not prove that the surviving directions align at the relevant heights or yield Nyman--Beurling approximation.

The next decisive test is therefore two-stage. First determine whether natural adaptive Nyman families actually realize many Euler-fingerprint singular values above `epsilon_T=Theta(log T/H_T)`. If they do, separately test whether those many source-visible directions can contribute coherent scalar phase alignment rather than only Hilbert-space diversity.

**Boundary.** The Euler Gram is a one-sided lower certificate. Small `G^Eul` does not imply small `mathfrak L_T(epsilon)` because another capped-Lipschitz witness may see distinctions suppressed by the Euler frequencies. Large `G^Eul` does not remove the sparse-height escape, the ultra-thin stationary-theorem limitation, or the final global Nyman approximation gate.