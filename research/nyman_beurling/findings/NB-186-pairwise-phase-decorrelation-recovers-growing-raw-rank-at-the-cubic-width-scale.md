# NB-186 — Pairwise phase decorrelation recovers growing raw rank at the cubic width scale

**Date:** 2026-09-17  
**Status:** `DERIVED + GROWING-RANK + FOURTH-MOMENT + SCHATTEN + PRIME-PHASE + DENSITY-ONE-FILTER + CUBIC-WIDTH + REPRESENTATION-BOUNDARY + NB-184/NB-185-REFINEMENT`.

`NB-185` shows that every fixed finite prime-phase Hadamard code survives the density-one `NB-184` acquisition filter, but its Kronecker--Weyl proof gives no useful dependence on growing rank: a prescribed `N`-dimensional phase box can have exponentially small Haar measure. That high-dimensional box-hitting problem is stronger than what the `NB-178` nuclear certificate actually needs. We do not need to realize prescribed rows. It is enough to find `N` good heights whose raw prime-phase matrix has nuclear norm of order `N^(3/2)`.

A fourth-moment selection argument does this from pairwise phase decorrelation alone. If `G subset [T,2T]` has relative complement `epsilon`, then deleting `[T,2T]\G` perturbs every nonzero normalized Fourier coefficient by at most `O(epsilon)`. For the first `N` prime logarithms, the remaining full-interval correlation is `O(p_N/T)`. Sampling `N` heights from `G` and computing the fourth Schatten moment of the resulting phase matrix therefore yields a deterministic selection with

\[
\boxed{
\|P\|_*
\ge
\frac{N^{3/2}}
{\sqrt{2+N\rho_{N,T,G}^2}},
\qquad
\rho_{N,T,G}
:=
\frac{\epsilon+2p_N/T}{1-\epsilon}.
}
\tag{1}
\]

Thus `N rho^2=O(1)` already gives Hadamard-scale **nuclear mass**, without any quantitative high-dimensional Kronecker theorem. Applying the quantitative exceptional-density bound of `NB-184` with `N asymp 1/a` shows that fixed-quality growing raw rank is available at the cubic width scale `T a^3 \gtrsim 1`. If `T a^3 -> infinity`, one can even let the acquisition threshold tend to zero slowly and obtain

\[
\boxed{
\|P\|_*
\ge
\left(\frac1{\sqrt2}-o(1)\right)N^{3/2}
}
\tag{2}
\]

on heights whose scalar Euler acquisition ratio is increasingly supercritical.

This removes the phase-box hitting bottleneck left by `NB-185`, but it does **not** solve the source-faithful rank problem. The columns of `P` are raw unit prime phases. Their true Euler amplitudes `log p / p^(1+a)` and the cost of exposing channels separately are precisely the load-bearing information isolated by `NB-180`--`NB-182`. The new result says that growing phase coherence itself is already present at a quantitative scale; the remaining obstruction is amplitude-balanced acquisition, not high-dimensional recurrence.

## Claim

Let `G subset [T,2T]` be measurable with

\[
|G|=(1-\epsilon)T,
\qquad 0\le\epsilon<1.
\tag{3}
\]

Let `p_1<...<p_N` be the first `N` primes and put

\[
\omega_j:=\log p_j,
\qquad
v(t):=(e^{-it\omega_1},...,e^{-it\omega_N})\in\mathbb C^N.
\tag{4}
\]

Define

\[
\rho_{N,T,G}
:=
\frac{\epsilon+2p_N/T}{1-\epsilon}.
\tag{5}
\]

Then there exist distinct heights `t_1,...,t_N in G` such that the raw prime-phase matrix

\[
P_{ij}:=e^{-it_i\log p_j}
\tag{6}
\]

satisfies

\[
\boxed{
\|P\|_*
\ge
\frac{N^{3/2}}
{\sqrt{2+N\rho_{N,T,G}^2}}.
}
\tag{7}
\]

In particular, if

\[
N\rho_{N,T,G}^2=O(1),
\tag{8}
\]

then

\[
\|P\|_*\gg N^{3/2}.
\tag{9}
\]

If instead

\[
\sqrt N\,\rho_{N,T,G}\to0,
\tag{10}
\]

then

\[
\boxed{
\|P\|_*
\ge
\left(\frac1{\sqrt2}-o(1)\right)N^{3/2}.
}
\tag{11}
\]

Now specialize to the `NB-184` acquisition-good set

\[
G_T(\eta)
:=
\left\{
 t\in[T,2T]:
 \sqrt a\,\mathcal H_{a,B}(t)\le\eta
\right\}.
\tag{12}
\]

The proof of `NB-184` gives the quantitative form

\[
\epsilon_T(\eta)
:=1-\frac{|G_T(\eta)|}{T}
\ll_B
\eta^{-2}
\left(
 a+(Ta^2)^{-1/2}+(Ta^2)^{-1}
\right).
\tag{13}
\]

Take

\[
N=\lfloor c/a\rfloor
\tag{14}
\]

for any fixed `c>0`. Using the classical prime-number-theorem consequence `p_N \ll N log(2N)`, already within the Davenport/PNT source anchor of this line, one obtains

\[
\sqrt N\,\rho_{N,T,G_T(\eta)}
\ll_{B,c}
\eta^{-2}
\left(
 \sqrt a
 +\frac1{\sqrt{Ta^3}}
 +\frac1{Ta^{5/2}}
\right)
+
\frac{\log(2/a)}{Ta^{3/2}}.
\tag{15}
\]

Consequently:

1. if `a->0`, `T a^3 >= c_0>0`, and `eta>0` is fixed, then `N rho^2=O_{B,c,c_0,eta}(1)` and there are `N asymp 1/a` acquisition-good heights with `||P||_* \gg N^(3/2)`;
2. if `a->0` and `T a^3 -> infinity`, one may choose `eta=eta_T ->0` slowly enough that the right-hand side of (15) tends to zero, so (11) holds while every selected height also satisfies `sqrt(a) mathcal H_(a,B)(t_i) <= eta_T ->0`.

Thus the full generic raw phase rank `N asymp 1/a` is quantitatively accessible at the **cubic** width scale. This is narrower than the quadratic scalar-acquisition range of `NB-184`, but it is a genuine growing-rank theorem rather than the fixed-rank recurrence statement of `NB-185`.

## Derivation

### 1. A large-measure height set retains pairwise prime-phase decorrelation

For `xi in R`, define the normalized Fourier coefficient of `G`

\[
\mu_G(\xi)
:=
\frac1{|G|}
\int_G e^{-it\xi}\,dt.
\tag{16}
\]

For `xi !=0`, subtract the missing part from the full dyadic interval:

\[
\int_G e^{-it\xi}dt
=
\int_T^{2T}e^{-it\xi}dt
-
\int_{[T,2T]\setminus G}e^{-it\xi}dt.
\]

The first integral has modulus at most `2/|xi|`; the second has modulus at most `epsilon T`. Therefore

\[
\boxed{
|\mu_G(\xi)|
\le
\frac{2}{(1-\epsilon)T|\xi|}
+
\frac{\epsilon}{1-\epsilon}.
}
\tag{17}
\]

For distinct primes `p_j<p_k<=p_N`,

\[
\log\frac{p_k}{p_j}
\ge
\frac{p_k-p_j}{p_k}
\ge
\frac1{p_N},
\tag{18}
\]

where `log(1+x)>=x/(1+x)` was used. Hence for every `j != k`,

\[
\boxed{
|\mu_G(\omega_j-\omega_k)|
\le
\rho_{N,T,G}.
}
\tag{19}
\]

This is the only phase input needed below. In contrast with `NB-185`, no simultaneous approximation of an `N`-dimensional target box appears.

### 2. The row Gram fourth moment only sees pair correlations

Let `t` and `s` be independent, uniformly distributed on `G` with respect to normalized Lebesgue measure. Then

\[
\langle v(t),v(s)\rangle
=
\sum_{j=1}^N e^{-i(t-s)\omega_j}.
\]

Expanding the square and using independence gives

\[
\begin{aligned}
\mathbb E
|\langle v(t),v(s)\rangle|^2
&=
\sum_{j,k}
|\mu_G(\omega_j-\omega_k)|^2\\
&\le
N+N(N-1)\rho_{N,T,G}^2.
\end{aligned}
\tag{20}
\]

Now sample `t_1,...,t_N` independently from `G` and form `P` by (6). Since Lebesgue measure has no atoms, the sampled heights are distinct almost surely. Moreover

\[
\|P\|_{S_4}^4
=
\operatorname{tr}((PP^*)^2)
=
\sum_{i,i'=1}^N
|\langle v(t_i),v(t_{i'})\rangle|^2.
\tag{21}
\]

The `i=i'` terms contribute exactly `N^3`. Applying (20) to the off-diagonal pairs yields

\[
\begin{aligned}
\mathbb E\|P\|_{S_4}^4
&\le
N^3
+N(N-1)
\left[N+N(N-1)\rho_{N,T,G}^2\right]\\
&\le
2N^3+N^4\rho_{N,T,G}^2.
\end{aligned}
\tag{22}
\]

Therefore at least one distinct selection of heights satisfies the deterministic bound

\[
\boxed{
\|P\|_{S_4}^4
\le
2N^3+N^4\rho_{N,T,G}^2.
}
\tag{23}
\]

### 3. A fourth-moment bound forces Hadamard-scale nuclear mass

Every entry of `P` has modulus one, so

\[
\|P\|_F^2=N^2,
\qquad
\|P\|_F=N.
\tag{24}
\]

If `s_1,...,s_N` are the singular values, Holder applied directly to

\[
\sum_j s_j^2
=
\sum_j s_j^{2/3}s_j^{4/3}
\]

gives

\[
\|P\|_F
\le
\|P\|_*^{1/3}\|P\|_{S_4}^{2/3},
\]

or equivalently

\[
\boxed{
\|P\|_*
\ge
\frac{\|P\|_F^3}{\|P\|_{S_4}^2}.
}
\tag{25}
\]

Combining (23)--(25) gives

\[
\|P\|_*
\ge
\frac{N^3}
{N^{3/2}\sqrt{2+N\rho_{N,T,G}^2}},
\]

which is exactly (7). Equations (9) and (11) follow immediately.

The logic is worth separating from `NB-185`. Kronecker--Weyl asks for a very specific point in a high-dimensional torus. The nuclear certificate only asks that the selected rows collectively retain enough spectral mass. The latter is a low-moment property, and low moments are already controlled by pairwise Fourier decorrelation.

### 4. The `NB-184` deletion tariff creates the cubic scale

Let

\[
F_T(a)
:=
 a+(Ta^2)^{-1/2}+(Ta^2)^{-1}.
\tag{26}
\]

Equation (13) says `epsilon_T(eta) <<_B eta^(-2) F_T(a)`. With `N asymp 1/a`,

\[
\sqrt N\,F_T(a)
\asymp
\sqrt a
+
\frac1{\sqrt{Ta^3}}
+
\frac1{Ta^{5/2}}.
\tag{27}
\]

This explains the new width boundary. `NB-184` only needed `epsilon_T ->0`, which occurs under `T a^2 -> infinity`. Growing raw rank needs the stronger condition `sqrt(N) epsilon_T=O(1)`, because a common deleted set can create an `O(epsilon_T)` correlation in every off-diagonal frequency pair. At the full packing rank `N asymp 1/a`, that becomes the cubic requirement `T a^3 \gtrsim 1`.

The frequency-spacing term is cheaper. The PNT bound `p_N << N log(2N)` gives

\[
\frac{p_N\sqrt N}{T}
\ll
\frac{\log(2/a)}{Ta^{3/2}},
\tag{28}
\]

which tends to zero throughout the cubic regime as `a->0`. Thus the loss from quadratic to cubic width comes from intersecting with the acquisition-good set, not from crowding among the first `N` prime logarithms.

If `T a^3 -> infinity`, the right side of (27) tends to zero. We may then choose `eta_T ->0` sufficiently slowly that

\[
\eta_T^{-2}\sqrt N\,F_T(a)\to0.
\tag{29}
\]

Together with (28), this gives `sqrt(N) rho ->0`, hence (11). At the same selected heights,

\[
\sqrt a\,\mathcal H_{a,B}(t_i)\le\eta_T\to0.
\tag{30}
\]

So growing raw phase nuclear mass and increasingly cheap scalar Euler acquisition can be made simultaneous. What is still missing is a source-faithful map that preserves that raw nuclear mass after the true Euler amplitudes and channel-exposure tariff are restored.

## Representation audit

The generic part of the argument is a low-moment matrix-selection lemma: a family of unit-modulus vectors with small pairwise coordinate correlations contains `N` rows whose Schatten-fourth moment is `O(N^3)`, and Frobenius/Schatten interpolation converts this into `Theta(N^(3/2))` nuclear mass. Random Vandermonde moment methods are classical; no novelty is claimed for that matrix technology.

The representation-specific part is the phase family `e^{-it log p}` and the fact that the `NB-184` good set is defined by the actual capped-Poisson seminorm of the local Euler kernel. The prime-log spacing estimate then turns the generic Fourier-correlation lemma into the explicit `p_N/T` term.

The source-specific conclusion is deliberately limited. The rows are selected at genuine Euler-good heights, but the columns of `P` are **unweighted prime phases**. The actual logarithmic derivative contains amplitudes

\[
\frac{\log p}{p^{1+a}},
\]

and `NB-180`--`NB-182` show that exposing weak characters independently must be charged. Therefore (7) is a quantitative raw phase-accessibility theorem, not yet a lower bound for the source-faithful approximate complexity `mathfrak L_T(epsilon)` and not a Nyman approximation theorem.

Indeed, inserting the true square-summable prime amplitudes directly would reintroduce the compactness mechanism identified around `NB-176`--`NB-177`. The useful new information is narrower: **growing coherent phase geometry is not what fails first**. Any remaining negative theorem must use the amplitude/acquisition budget, target coupling, the quadratic-to-cubic simultaneous-selection gap, or some stronger arithmetic restriction.

## Prior-art boundary

Moment methods for random Vandermonde matrices with unit-circle phases are classical. A close generic reference is O. Ryan and M. Debbah, *Asymptotic Behaviour of Random Vandermonde Matrices with Entries on the Unit Circle*, arXiv:0802.3570, together with their 2008 work on limiting moments of Vandermonde random matrices. Those works study random Vandermonde Gram moments in much greater generality than the elementary fourth-moment calculation used here.

No external random-matrix theorem is load-bearing: equations (17)--(25) prove the needed selection statement directly. The only asymptotic prime input in the cubic specialization is the standard PNT consequence `p_N << N log N`, already covered by the existing Davenport/PNT anchor in `SOURCES.md`; the `NB-184` exceptional-density estimate is internal. No new durable source entry is therefore required.

## Self-adversarial review and limits

### The fourth moment certifies nuclear mass, not uniform conditioning

Equation (7) does not imply that every singular value is of order `sqrt N`, unlike the fixed-rank Hadamard approximation in `NB-185`. A matrix can have the required nuclear mass while still possessing a nontrivial poorly conditioned tail. This is enough for the coordinatewise nuclear certificate of `NB-178`, but it is a weaker spectral statement than a full frame bound.

### The cubic boundary belongs to this selection argument, not necessarily to the source

The `T a^3` scale comes from the crude but robust estimate that deleting an `epsilon T` set can perturb **every** nonzero Fourier coefficient by `O(epsilon)`. The bad set generated by `NB-184` is not arbitrary; it may have additional arithmetic structure that yields smaller average correlations. Therefore the result does not prove that cubic width is an intrinsic phase transition. It proves that no high-dimensional box-hitting theorem is needed above that scale.

### Raw prime phases are still not independently free source coordinates

The main limitation from `NB-180`--`NB-182` remains. Normalizing each prime character separately would hide the true Euler amplitude tariff. The theorem must not be used as `mathfrak L_T \gtrsim N` for the physical scalar Euler source without an additional amplitude-balanced acquisition argument.

### Sparse adversarial heights and the quadratic endpoint remain untouched

The selection is existential inside a large-measure good set. It neither gives pointwise control on an externally prescribed sparse sequence nor improves the `NB-184` scalar acquisition theorem at `T a^2=O(1)`.

## Updated frontier

`NB-185` left two apparently coupled tasks: quantitative growing-dimensional phase hitting and source-faithful amplitude acquisition. `NB-186` separates them. For the nuclear-scale notion of coherent rank relevant to `NB-178`, prescribed high-dimensional phase boxes are unnecessary; pairwise decorrelation already yields growing raw rank `N asymp 1/a` on `NB-184`-good heights at cubic width.

The immediate source-side question is now sharper: can one preserve a positive fraction of this `N^(3/2)` nuclear mass after multiplying by true Euler amplitudes and charging the acquisition map in the Wiener/capped-Poisson currency of `NB-182`, perhaps by a non-coordinatewise mixture that reuses weak channels coherently? A negative result should show that every such amplitude-balanced extraction collapses the raw fourth-moment rank. A positive result would have to bridge precisely that gap rather than solve a high-dimensional Kronecker recurrence problem.