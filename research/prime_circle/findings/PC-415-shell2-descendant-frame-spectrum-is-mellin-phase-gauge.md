# PC-415 — shell-2 descendant frame spectrum is Mellin-phase gauge over a universal kernel

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the canonical Dirichlet-weighted full descendant frame/Gram/Fredholm spectralization built from the PC-405--PC-408 shell-2 descendant family. In the native trace-class regime, the complete infinite descendant orbit defines a positive trace-class frame operator. Mellin diagonalization shows that its two-frequency kernel is the PC-408 degree-two universal conductor symbol multiplied by the outer one-shell source amplitudes. Arbitrary Mellin phase changes of the base source act by unitary conjugacy on the full frame operator and leave the conductor Gram operator exactly unchanged. Thus the entire nonzero spectrum, all Schatten traces, and the Fredholm determinant depend on the source only through its one-shell Mellin power spectrum, while the conductor interaction is the already universal descendant kernel.

This closes the natural route in which one keeps the whole infinite descendant family as an operator rather than evaluating scalar energies. It does **not** rule out operators derived from angular/chord/old-new geometry before the PC-405 scalar descendant reduction, source-dependent product/state laws, or independently forced renormalized topologies outside the trace-class regime.

## 1. The full descendant orbit defines a canonical trace-class operator

Use the Hilbert representation of PC-407,

\[
\mathcal H=L^2(\mathbb R_+,dx/x),
\qquad
h_{nm}=C_{n,m}h_n,
\tag{1}
\]

where each `C_{n,m}` is a product of the source-forced dilation/fresh-prime operators from PC-405--PC-407. For real `sigma>1`, define the weighted synthesis operator

\[
T_{n,\sigma}:\ell^2(\mathbb N)\to\mathcal H,
\qquad
T_{n,\sigma}e_m=m^{-\sigma/2}h_{nm}.
\tag{2}
\]

PC-407 proves absolute convergence of the canonical quadratic descendant energy

\[
\sum_{m\ge1}m^{-\sigma}\|h_{nm}\|_{\mathcal H}^2<\infty.
\tag{3}
\]

Therefore `T_{n,sigma}` is Hilbert--Schmidt. The associated physical-space frame operator and conductor Gram operator,

\[
F_{n,\sigma}:=T_{n,\sigma}T_{n,\sigma}^*,
\qquad
G_{n,\sigma}:=T_{n,\sigma}^*T_{n,\sigma},
\tag{4}
\]

are positive trace-class operators, and their nonzero eigenvalues agree with multiplicity. In particular the Fredholm determinant

\[
\det(I-zF_{n,\sigma})
\tag{5}
\]

is canonically defined in this regime; no zeta regularization or externally chosen spectral wrapper is needed.

This is stronger than the scalar energy of PC-407: the complete mutual geometry of all weighted descendants is retained in `F` or, equivalently, in `G`.

## 2. Its Mellin kernel is exactly the PC-408 degree-two descendant symbol

With the Mellin convention of PC-407,

\[
\widehat{h_{nm}}(t)=c_{n,m}(t)\widehat h_n(t),
\qquad
c_{n,m}(t)
=
m^{it}\prod_{\substack{p\mid m\\p\nmid n}}(1-p^{-it}).
\tag{6}
\]

Relative to the Plancherel measure `dt/(2 pi)`, the kernel of `F_{n,sigma}` is therefore

\[
\boxed{
K_{n,\sigma}^{h}(t,u)
=
\widehat h_n(t)\overline{\widehat h_n(u)}
Q_{n,\sigma}(t,u),
}
\tag{7}
\]

where

\[
\boxed{
Q_{n,\sigma}(t,u)
:=
\sum_{m\ge1}m^{-\sigma}
 c_{n,m}(t)\overline{c_{n,m}(u)}
=
D_{n,2}(\sigma;t,-u).
}
\tag{8}
\]

The series in (8) converges absolutely for `sigma>1`. PC-408 has already classified `D_{n,2}` exactly. Its universal shifted-zeta divisor is

\[
\boxed{
Z_2(\sigma;t,-u)
=
\frac{
\zeta(\sigma)\zeta(\sigma-i(t-u))
}{
\zeta(\sigma-it)\zeta(\sigma+iu)
},
}
\tag{9}
\]

multiplied by the PC-408 universal Euler correction and a finite correction over primes dividing the parent `n`.

Thus passing from scalar descendant energies to the full trace-class frame operator does not reveal a new conductor interaction hidden by PC-407. The whole two-frequency interaction is precisely the already classified degree-two descendant kernel. In the native operator regime `sigma>1`, every zeta argument in (9) has real part greater than one. Any continuation in `sigma` toward the critical strip is continuation of the universal PC-408 conductor symbol, not new spectral data forced by the frame construction.

## 3. Exact Mellin-phase gauge theorem

The stronger obstruction is independent of the explicit Euler product. Let `theta:R->R` be measurable and let `U_theta` be the unitary Mellin multiplier

\[
\widehat{U_\theta f}(t)=e^{i\theta(t)}\widehat f(t).
\tag{10}
\]

Every descendant operator `C_{n,m}` is itself a Mellin multiplier by (6), hence

\[
U_\theta C_{n,m}=C_{n,m}U_\theta
\qquad\text{for every }m.
\tag{11}
\]

Put `g_n=U_theta h_n` and propagate it by exactly the same descendant law. Then

\[
g_{nm}=C_{n,m}g_n=U_\theta h_{nm},
\tag{12}
\]

so the synthesis operators satisfy

\[
\boxed{
T_{g,\sigma}=U_\theta T_{h,\sigma}.
}
\tag{13}
\]

Consequently

\[
\boxed{
F_{g,\sigma}
=U_\theta F_{h,\sigma}U_\theta^*,
\qquad
G_{g,\sigma}=G_{h,\sigma}.
}
\tag{14}
\]

Equation (14) is exact. Therefore the complete nonzero frame spectrum, the conductor Gram spectrum, every Schatten trace `tr(F^k)`, and the Fredholm determinant `det(I-zF)` are invariant under arbitrary Mellin phase changes of the source.

The same statement is visible directly in (7): replacing `hat h_n(t)` by `e^{i theta(t)}hat h_n(t)` multiplies the kernel by `e^{i(theta(t)-theta(u))}`, which is precisely unitary kernel conjugacy rather than new spectral information.

For rigor at infinite conductor depth, let `T_N` contain only `m<=N`. Equation (14) is exact at every finite `N`, while (3) gives `T_N -> T` in Hilbert--Schmidt norm. Hence

\[
\|T_NT_N^*-TT^*\|_1
\le
\|T_N-T\|_2(\|T_N\|_2+\|T\|_2)
\longrightarrow0,
\tag{15}
\]

so the infinite-depth conjugacy is the trace-norm limit of finite-rank identities rather than a formal interchange of divergent sums.

## 4. The actual cyclotomic source enters only through one-shell power spectrum

PC-407 gives, away from the removable/cancelled zero-frequency presentation,

\[
\widehat h_n(t)
=
-\Gamma(1-it)\zeta(1-it)n^{it}
\prod_{p\mid n}(1-p^{-it}).
\tag{16}
\]

Therefore the source dependence that can survive in any invariant of `F_{n,sigma}` is contained in

\[
\boxed{
|\widehat h_n(t)|^2
=
|\Gamma(1-it)\zeta(1-it)|^2
\prod_{p\mid n}|1-p^{-it}|^2,
}
\tag{17}
\]

with the value at `t=0` understood by continuous extension of the combined expression. The phase `n^{it}` and every other Mellin phase of the one-shell profile are invisible to the full frame spectrum.

This supplies a direct matched-control falsification. Choose a nonconstant odd real phase `theta` so that `g_n=U_theta h_n` remains real under inverse Mellin transform. Then `g_n` has exactly the same Mellin power spectrum as the cyclotomic source, and by (14) it has exactly the same full descendant Gram operator and a unitarily equivalent frame operator. Generic such phase twists are not cyclotomic shell profiles, yet every spectral invariant of the present construction agrees.

The negative statement is deliberately narrower than saying that the boundary modulus `|zeta(1-it)|` is analytically uninteresting. The point is source identifiability: **the infinite descendant frame adds no source-specific spectral carrier beyond that pre-existing one-shell power spectrum and the universal PC-408 conductor kernel.**

## 5. Prior-art, duplicate, and representation audit

No external novelty is claimed for the functional analysis. The implications `T` Hilbert--Schmidt `=> TT*` trace class, equality of the nonzero spectra of `TT*` and `T*T`, unitary invariance of spectrum/Fredholm determinants, and phase loss under Fourier-type magnitude data are standard. A targeted literature audit found the expected general phase-retrieval precedent: Bendory, Beinert, and Eldar, *Fourier Phase Retrieval: Uniqueness and Algorithms* (2017), reviews the nonuniqueness of one-dimensional signals from Fourier magnitude alone. That precedent supports the falsification pattern but is not load-bearing for (13)--(15), which are exact project-local identities.

The local duplicate audit also matters. PC-407 treated only the scalar weighted Hilbert energy and its polarized frequency symbol. PC-408 classified fixed-degree same-conductor products and supplied the universal two-frequency symbol used in (8)--(9). PC-414 proved finite-cutoff rank-one source factorization for arbitrary conductor tensors at fixed Mellin frequencies. The present result is their operator-level completion for the canonical positive infinite descendant frame: trace-class existence, exact full-kernel identification, trace-norm passage to infinite conductor depth, and unitary phase-gauge equivalence of the complete spectrum/Fredholm determinant.

The obstruction is representation-independent. Equation (14) is unitary equivalence on `H`, while `G_g=G_h` is exact equality on conductor space. Changing Mellin normalization, diagonalizing `G`, or representing the same frame through another orthonormal basis cannot restore the lost source phase.

## 6. Consequence for the research line

The following natural route is closed in the native trace-class regime:

\[
\boxed{
\text{PC-405 shell-2 descendants}
\;\longrightarrow\;
\text{Dirichlet-weighted full frame/Gram operator}
\;\longrightarrow\;
\text{Fredholm or ordinary spectral invariant}
\;\longrightarrow\;
\text{new Prime-Circle-specific RH carrier}.
}
\tag{18}
\]

The surviving operator frontier must escape the hypotheses used here: it must incorporate source-derived angular/chord/old-new geometry before the scalar descendant law, alter the source state/product law nonlinearly, couple source and conductor before Mellin reduction, or justify a genuinely different infinite-depth topology from intrinsic geometry rather than by analytic continuation of the universal conductor symbol.

This finding does not claim that every possible nonlocal Prime-Circle operator is phase blind. It isolates the canonical full descendant frame and shows exactly why that particular genuinely infinite-level spectralization still collapses to one-shell power data plus the already universal descendant kernel.
