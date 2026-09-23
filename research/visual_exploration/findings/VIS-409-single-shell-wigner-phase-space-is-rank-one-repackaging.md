# VIS-409 — full single-shell Wigner phase space is the rank-one shell state in new coordinates

## Claim

Let `h` be one nonzero shell profile in the Haar space

`H = L^2(R_+, dx/x)`,

and pass to logarithmic coordinates

`f(u)=h(e^u) in L^2(R,du)`.

The full Wigner phase-space portrait

`W_f(u,xi)=int_R f(u+tau/2) conjugate(f(u-tau/2)) exp(-2 pi i xi tau) d tau`

is not an additional information carrier beyond the single shell. Fourier inversion in `xi` recovers exactly

`A_f(u,tau)=f(u+tau/2) conjugate(f(u-tau/2))`,

and the change of variables

`x=u+tau/2`, `y=u-tau/2`

gives the complete rank-one kernel

`K_f(x,y)=f(x) conjugate(f(y))`.

Thus `W_f` is the Weyl symbol of the rank-one operator `|f><f|`. Conversely that rank-one operator determines the ray of `f`, hence `f` up to a single global unimodular phase. A visually rich Wigner portrait therefore re-encodes the complete one-shell state but does not create a second arithmetic channel or an interaction absent from that state.

The same statement survives finite descendant phase-space constructions. If `f_m=C_m f` and `f_n=C_n f` are obtained from the same shell by fixed source-independent descendant operators, then the cross-Wigner distribution `W(f_m,f_n)` is exactly the Weyl symbol of `|f_m><f_n|`, so every finite family of such cross-portraits is determined by `f` together with the already specified operators `C_m,C_n`.

Fixed-window spectrograms and standard fixed-kernel Cohen/localization representations cannot improve this information boundary. They are deterministic transforms of the Wigner distribution; in the standard localization calculus the relevant phase-space symbol is a convolution of the underlying Wigner symbol with a fixed window Wigner distribution. Such a transform may preserve enough information to reconstruct the original state for a favorable window, or may lose information, but it cannot add source information that was not already present in `f`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-WEYL-WIGNER-IDENTITY + DECISIVE-NEGATIVE/REPRESENTATION-CONTROL + NO-NOVELTY-CLAIM`.

This does not say that Wigner or spectrogram geometry is useless. It says that any genuinely new theorem found in such a portrait must be a theorem about the underlying one-shell state or about an independently introduced operator/coupling; visual phase space by itself does not evade a one-carrier obstruction.

## 1. Logarithmic coordinates make the proposed phase space ordinary time-frequency space

The map

`U : H -> L^2(R,du)`, `Uh(u)=h(e^u)`

is unitary because `dx/x=du`. Multiplicative dilation of the original shell becomes translation in `u`, while the Mellin transform becomes the ordinary Fourier transform in `u` up to convention. This is exactly the setting in which a position-frequency or scale-Mellin portrait is naturally represented by the Wigner distribution.

For `f in L^2(R)`, define

`W_f(u,xi)=int f(u+tau/2) conjugate(f(u-tau/2)) exp(-2 pi i xi tau) d tau`.

For general `L^2` data this identity is interpreted in the usual `L^2`/distributional sense. The prime-circle shell profiles behind `PC-416` have substantially better decay, so no extra pathology is needed for the present representation control.

The visually attractive feature is immediate: `u` resolves logarithmic position/scale while `xi` resolves Mellin frequency, so interference, concentration, chirp-like phase structure, and multiscale localization can all become visible in one two-dimensional object. The question is whether that extra visual geometry is extra mathematics or only a change of coordinates on the same state.

## 2. Fourier inversion recovers the entire rank-one shell kernel

Take the inverse Fourier transform of `W_f` in its frequency coordinate. With the normalization above,

`int_R W_f(u,xi) exp(2 pi i xi tau) d xi`
` = f(u+tau/2) conjugate(f(u-tau/2))`

in the standard weak/`L^2` sense. Define

`A_f(u,tau)=f(u+tau/2) conjugate(f(u-tau/2))`.

Now set

`u=(x+y)/2`, `tau=x-y`.

Then

`A_f((x+y)/2,x-y)=f(x) conjugate(f(y))=K_f(x,y)`.

But `K_f` is exactly the integral kernel of the rank-one Hilbert-Schmidt operator

`P_f psi = <psi,f> f`.

So there is an exact chain

`full Wigner portrait <-> rank-one kernel K_f <-> rank-one operator P_f`.

Nothing asymptotic, numerical, or source-specific enters this equivalence.

If `W_f=W_g` for nonzero `f,g`, then `K_f=K_g` and therefore `P_f=P_g`. Equality of nonzero rank-one operators forces `g=e^{i alpha} f` for one constant phase `alpha`. The only information forgotten by the auto-Wigner representation is precisely the physically irrelevant global phase. The norm is not lost: it is encoded in the trace/integral of the rank-one state.

Accordingly a complete Wigner image can be informationally complete for a single shell while still failing to add any new carrier. Informational completeness and information creation are different claims.

## 3. Cross-Wigner descendants do not manufacture cross-source information

Suppose a family of descendants is generated from the same shell by fixed operators

`f_m=C_m f`.

For two descendants define

`W(f_m,f_n)(u,xi)`
` = int f_m(u+tau/2) conjugate(f_n(u-tau/2)) exp(-2 pi i xi tau) d tau`.

Fourier inversion again gives the kernel

`f_m(x) conjugate(f_n(y))`,

which is the rank-one operator `|f_m><f_n|`. Since `f_m` and `f_n` are already deterministic functions of `f` and the specified `C_m,C_n`, the cross-Wigner surface is likewise deterministic from the original shell plus those operators.

This matters for the phase-sensitive escape left open around the prime-circle Mellin analysis. `PC-416` proves that finite words in the log-position operator and descendant dilations collapse to finite Mellin jets of one shell; it deliberately does not cover genuinely infinite-order/nonlocal phase-space representations. The present result addresses a natural visual candidate outside that finite-jet theorem: the **full** Wigner surface uses all off-diagonal correlations of the shell, not merely finitely many Mellin derivatives. Nevertheless, those correlations assemble exactly into `|f><f|`. They retain the whole one-shell state but still do not supply an independent source, a new source-to-response law, or a cross-shell coupling.

Thus Wigner phase space escapes the *finite-jet truncation* while not escaping the more basic *single-shell information boundary*.

## 4. Spectrograms and fixed Cohen/localization portraits are downstream transforms

A common practical response to Wigner interference is to replace `W_f` by a short-time Fourier magnitude or spectrogram with a fixed window `g`. Standard time-frequency analysis relates these objects to Wigner/Weyl calculus: up to the chosen normalization/reflection convention, the spectrogram or localization symbol is obtained from the source Wigner distribution by a fixed phase-space convolution involving the window Wigner distribution.

For the present question, the exact convention is secondary. The decisive information direction is

`f -> W_f -> fixed-window/fixed-kernel phase-space representation`.

The final portrait is a deterministic function of `W_f` and the predeclared window/kernel. A convolution may be injective on a restricted class if its transfer function permits deconvolution, or it may erase structure; neither case creates source information. Likewise choosing a window after seeing the target can manufacture visual emphasis but cannot count as an intrinsic arithmetic mechanism.

This gives a clean falsification control for future visual work: changing from Wigner to a spectrogram, a smoothed Wigner surface, or another fixed Cohen-class portrait is not by itself an escape from a representation-level obstruction. The proposed gain must survive translation back to a representation-independent statement about the underlying shell or must identify additional mathematical input not already contained in that shell.

## 5. Matched-control consequence

Let `g` be any nonzero matched profile in the same logarithmic `L^2` class. Its Wigner portrait obeys the identical inversion law

`W_g <-> |g><g|`.

If the same fixed descendant operators, windows, smoothing kernels, or plotting coordinates are applied to `g`, the complete phase-space architecture is reproduced with `g` substituted for `f`. Universal Wigner interference geometry, marginals, translation/dilation covariance, smoothing behavior, or apparent phase-space localization therefore cannot by themselves distinguish the arithmetic shell from an arbitrary matched source.

A source-specific claim needs an additional discriminant. Examples would include a theorem that a quantitatively defined Wigner functional has a property forced by the arithmetic source but absent on a mathematically specified control class, or an independently justified operator coupling several source objects in a way not reconstructible from one rank-one state. Merely observing a striking ridge, interference pattern, concentration island, or self-similar texture is not such a discriminant.

## 6. Prior art and novelty boundary

The mathematics used here is standard Weyl-Wigner/time-frequency analysis. Nuno Costa Dias, Maurice A. de Gosson, and Joao Nuno Prata, *A Refinement of the Robertson-Schrodinger Uncertainty Principle and a Hirschman-Shannon Inequality for Wigner Distributions*, Journal of Fourier Analysis and Applications 25 (2019), 210-241, DOI `10.1007/s00041-018-9602-x`, explicitly identifies the cross-Wigner function as the Weyl symbol of a rank-one operator with kernel `f(x) conjugate(g(y))`.

Luis Daniel Abreu, Karlheinz Grochenig, and Jose Luis Romero, *Harmonic Analysis in Phase Space and Finite Weyl-Heisenberg Ensembles*, Journal of Statistical Physics 174 (2019), 1104-1136, DOI `10.1007/s10955-019-02226-2`, records the uniqueness of the Weyl symbol, the Wigner/STFT relation, and the phase-space convolution form of localization operators. Patrick Flandrin, *Explorations in Time-Frequency Analysis*, Cambridge University Press (2018), Chapter 9, DOI `10.1017/9781108363181.012`, treats spectrograms explicitly as smoothed Wigner distributions.

No novelty is claimed for any of those identities. The Mathia-specific contribution of this finding is the exact **representation audit**: after the current one-shell/finite-jet obstruction, moving to a visually richer full Wigner or fixed-window phase-space portrait does not add the missing carrier. It either re-encodes the same rank-one shell state or applies a deterministic downstream transform to it.

## 7. Research consequence

Do not open a visual branch whose sole proposed advance is to draw the prime-circle single-shell source, or finitely many deterministic descendants of it, as Wigner, spectrogram, smoothed-Wigner, or other fixed-kernel time-frequency portraits and then interpret newly visible geometry as a new arithmetic coupling.

Such portraits remain useful exploratory instruments. If they expose a precise invariant, obstruction, or quantitative law, formulate that law independently of the picture and ask whether it distinguishes the arithmetic source from matched source profiles. If the law factors entirely through `|f><f|`, it is a theorem about the existing single-shell state. If it requires an additional source-dependent operator, a genuinely multi-shell/cross-object relation, an incidence structure discarded before scalarization, or a nonlinear state construction, that additional structure is the real research object and needs its own audit.

This finding therefore closes **standard single-shell phase-space visualization as an information escape**, not phase-space analysis as a method and not the broader nonlocal/source-dependent routes explicitly left open by `PC-416`.