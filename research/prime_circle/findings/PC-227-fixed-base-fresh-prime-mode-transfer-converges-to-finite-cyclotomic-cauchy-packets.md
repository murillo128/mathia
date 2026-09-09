# PC-227 — fixed-base fresh-prime mode transfer converges to finite cyclotomic Cauchy packets

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY` for the internal-fiber/Fourier escape left open by PC-224--PC-226. Those findings show that singular-value compression loses the internal new-prime vector and that the resulting fixed-base variance has only finitely many residue-class limits. The stronger test is to keep the individual Fourier modes of the fresh prime coordinate before any left-unitary quotient or exact-order compression.

At a fixed coarse conductor `N`, that stronger state still has a rigid limit. For primes `q \nmid N` in one residue class `r=q mod N`, every matrix coefficient from the exact-order `N` source sector through the normalized coefficient mask of `Phi_{Nq}` is either **exactly zero** or a sample of the reciprocal of the fixed polynomial `Phi_N` on a `q`-mesh. After the normalization already forced by the source mask, all nonvanishing mass concentrates near the finitely many primitive `N`-th roots. Each root contributes a shifted discrete Cauchy packet

\[
\frac{C}{j+\sigma},\qquad j\in\mathbb Z,
\]

where `sigma` is a nonzero rational with denominator `N` and `C` is an explicit cyclotomic residue depending only on `N`, `r`, and finite coarse-frequency labels. The regular part has vanishing Hilbert--Schmidt mass. Hence the **fully mode-resolved one-mask fresh-prime transfer**, not merely its positive square, has at most finitely many fixed-base accumulation models indexed by `r in U(N)`.

This is a stronger negative boundary than PC-226, but it is not a no-go for simultaneous `N,q -> infinity` or for a second source-forced operator acting on these packets before the limit. The fresh prime by itself does not generate an expanding new arithmetic spectrum at fixed base: it only refines the sampling of a fixed cyclotomic rational function and resolves its ordinary simple poles.

## 1. Exact Fourier transfer is a fixed cyclotomic quotient

Let

\[
H_m=L^2(\mathbb Z/m\mathbb Z)
\]

with normalized counting measure and Fourier characters

\[
e_k^{(m)}(x)=\zeta_m^{kx}.
\]

Fix `N>1`, let `q \nmid N` be prime, put `M=Nq`, and use the normalized cyclotomic coefficient mask from PC-224,

\[
\Phi_M(z)=\sum_x a_M(x)z^x,
\qquad
h_M=\sum_x a_M(x)^2,
\qquad
g_M(x)=\sqrt{\frac{M}{h_M}}\,a_M(x).
\tag{1}
\]

The canonical pullback `J_{N,M}` sends an exact-order source character `e_u^{(N)}`, `(u,N)=1`, to `e_{qu}^{(M)}`. Therefore the exact target Fourier matrix coefficient is

\[
\boxed{
A_{N,q}(k,u)
:=\left\langle e_k^{(M)},M_{g_M}e_{qu}^{(M)}\right\rangle
=
\frac{\Phi_M\!\left(\zeta_M^{qu-k}\right)}{\sqrt{Mh_M}}.
}
\tag{2}
\]

Now restrict to the genuinely new `q`-coordinate, so `q \nmid k`. Write

\[
r=q\bmod N,
\qquad
b=k\bmod N,
\qquad
a=b-ru\bmod N,
\tag{3}
\]

and set

\[
z:=\zeta_M^{qu-k}.
\tag{4}
\]

Then

\[
z^q=\zeta_N^{ru-b}=\zeta_N^{-a}.
\tag{5}
\]

Because `q \nmid N`, the standard prime-extension identity

\[
\Phi_{Nq}(z)=\frac{\Phi_N(z^q)}{\Phi_N(z)}
\tag{6}
\]

applies. Moreover `q \nmid k` implies `z^N\ne1`, so the denominator in (6) is nonzero. Combining (2), (5), and (6) gives the exact formula

\[
\boxed{
A_{N,q}(k,u)
=
\frac{\Phi_N(\zeta_N^{-a})}
{\sqrt{Nq\,h_{Nq}}\,\Phi_N(z)}.
}
\tag{7}
\]

The large refined-level polynomial has disappeared from the transfer except through its scalar coefficient energy. The whole internal `q`-mode vector is a root-of-unity sampling of the reciprocal of the **fixed** coarse polynomial `Phi_N`.

## 2. A stronger exact selection rule

The zeros of `Phi_N` are exactly the primitive `N`-th roots. Therefore (7) immediately implies

\[
\boxed{
A_{N,q}(k,u)=0
\quad\text{whenever}\quad
b-ru\in U(N).
}
\tag{8}
\]

This contains the pure-fresh-prime selection rule of PC-226 as the case `b=0`: since `-ru` is a unit modulo `N`, the exact-order `q` channel vanishes identically. But (8) is stronger. It removes every target coarse Fourier residue whose difference from the transported source residue is a unit.

Thus the only nonzero fresh-prime transfer is forced into coarse differences with a nontrivial gcd with `N`. No asymptotic argument is involved. In particular, at fixed base the set of allowed coarse labels is finite before one studies the `q`-mode dependence at all.

## 3. Every nonzero coarse channel becomes a finite family of shifted Cauchy packets

Assume now that `a=b-ru` is not a unit. Put

\[
\beta_a:=\zeta_N^{-a}.
\tag{9}
\]

Then `Phi_N(beta_a)\ne0`. Let

\[
\alpha_t:=\zeta_N^t,
\qquad t\in U(N),
\tag{10}
\]

be a primitive root. Since `alpha_t^q=\zeta_N^{rt}`, define the unique integer

\[
s_{a,t,r}\in\{1,\ldots,N-1\}
\]

satisfying

\[
s_{a,t,r}\equiv-(a+rt)\pmod N,
\qquad
\sigma_{a,t,r}:=\frac{s_{a,t,r}}N.
\tag{11}
\]

The residue can never be zero: `a\equiv-rt (mod N)` would make `a` a unit. The `q` roots of `z^q=beta_a` can therefore be locally numbered around `alpha_t` by

\[
\boxed{
z_{t,j}^{(q)}
=
\alpha_t\exp\!\left(\frac{2\pi i}{q}(j+\sigma_{a,t,r})\right),
\qquad j\in\mathbb Z,
}
\tag{12}
\]

with `j` understood modulo `q` at finite `q`. Every fixed bounded `j` corresponds, for all sufficiently large `q`, to a distinct target Fourier mode in the coarse residue `b` and lying in a shrinking neighborhood of `alpha_t`.

PC-226 proves that, writing

\[
q=N\ell+r,
\]

the coefficient energy has the exact affine form

\[
h_{Nq}=\ell H_r+K_r,
\tag{13}
\]

with `H_r>0`. Hence

\[
\frac{\sqrt{Nq\,h_{Nq}}}{q}\longrightarrow\sqrt{H_r}.
\tag{14}
\]

Since every primitive root is simple,

\[
q\,\Phi_N\!\left(
\alpha_t e^{2\pi i(j+\sigma)/q}
\right)
\longrightarrow
2\pi i(j+\sigma)\alpha_t\Phi_N'(\alpha_t).
\tag{15}
\]

Substitution into (7) gives the packet limit

\[
\boxed{
A_{N,q}\!\left(k_{t,j}^{(q)},u\right)
\longrightarrow
\frac{C_{N,r}(a,t)}{j+\sigma_{a,t,r}},
}
\tag{16}
\]

where

\[
\boxed{
C_{N,r}(a,t)
=
\frac{\Phi_N(\zeta_N^{-a})}
{2\pi i\,\alpha_t\Phi_N'(\alpha_t)\sqrt{H_r}}.
}
\tag{17}
\]

All dependence on the growing fresh prime has disappeared except for its residue class `r`. The packet shift is one of the finite rational values `1/N,...,(N-1)/N`, and the packet residue is ordinary cyclotomic root/derivative data at the fixed level `N`.

## 4. The Cauchy packets carry all asymptotic mass

The pointwise limit is not merely a zoomed-in curiosity. It captures the whole mode-resolved transfer in norm.

Let

\[
Z_N=\{\alpha_t:t\in U(N)\}.
\]

Because the roots are simple and finite, the continuous quotient

\[
\frac{|\Phi_N(z)|}{\operatorname{dist}(z,Z_N)}
\]

extends to a strictly positive continuous function on the unit circle. Hence there is a constant `c_N>0` such that

\[
|\Phi_N(z)|\ge c_N\operatorname{dist}(z,Z_N)
\qquad(|z|=1).
\tag{18}
\]

Away from fixed small arcs around `Z_N`, (7), (13), and (18) give

\[
|A_{N,q}(k,u)|=O_N(q^{-1}).
\tag{19}
\]

There are only `q` modes in a fixed coarse residue, so the total squared mass of this regular region is `O_N(q^{-1})`.

Inside an arc around `alpha_t`, the mesh is (12). Since every shift `sigma` stays a fixed positive distance from the integers, the same simple-zero estimate gives a uniform bound

\[
|A_{N,q}(k_{t,j}^{(q)},u)|
\le
\frac{C_N}{1+|j|}
\tag{20}
\]

through the packet range. Consequently the squared tail beyond `|j|\le J` is `O_N(J^{-1})`, uniformly for large `q`.

Equations (16), (19), and (20) imply that after the canonical local numbering by angular offset from the primitive `N`-th roots, every column converges in `ell^2` to the finite direct sum of shifted Cauchy sequences in (16). Since the source exact-order space has the fixed dimension `phi(N)`, the full mode-resolved operator converges in Hilbert--Schmidt, hence operator, norm after this packet identification.

Therefore, along primes in one residue class `q congruent r (mod N)`, there is a single fixed packet model. Across all fresh primes there are at most `phi(N)` such accumulation models.

## 5. Exact-order projectors do not recover an expanding fixed-base spectrum

The target Fourier mode `k` has a nontrivial `q` component and a coarse `N` component represented, up to the harmless CRT unit reindexing, by `b=k mod N`. If

\[
d=\frac{N}{\gcd(b,N)},
\tag{21}
\]

then its total exact order is `qd`. Thus inserting a canonical exact-order projector before positive-square compression merely selects those coarse labels `b` with the chosen `d` from the same packet family (16).

In particular:

\[
\boxed{
\text{fixed }N
\;\Longrightarrow\;
\text{every one-mask exact-order-resolved fresh-prime block}
\text{ has only finitely many Cauchy-packet limits.}
}
\tag{22}
\]

This closes the most immediate loophole in PC-224/PC-225: retaining the internal Fourier directions of a **single** cyclotomic fresh-prime mask before the left-unitary quotient does preserve more information than conditional variance, but the extra information is still only a finite packetization of the fixed polynomial `1/Phi_N`.

The source-side Gram matrices of the limiting packets are themselves classical trigonometric data. For `sigma,tau in (0,1)`, the standard partial-fraction identities give

\[
\sum_{j\in\mathbb Z}\frac1{(j+\sigma)^2}
=\pi^2\csc^2(\pi\sigma),
\tag{23}
\]

and, for `sigma\ne\tau`,

\[
\sum_{j\in\mathbb Z}
\frac1{(j+\sigma)(j+\tau)}
=
\pi\,\frac{\cot(\pi\sigma)-\cot(\pi\tau)}{\tau-\sigma}.
\tag{24}
\]

Because every shift is rational with denominator `N`, any fixed-base Gram/singular compression of the packet limit returns to finite root-of-unity trigonometric data. This is the mode-resolved analogue of the scalar finite-state limit in PC-226.

## 6. Prime coarse bases collapse even before taking a limit

The prime-base control is stronger. Let `N=p` be prime. The only nonunit residue modulo `p` is zero, so (8) says that a source mode `u in U(p)` can couple to a new target only when

\[
b\equiv ru\pmod p.
\tag{25}
\]

Distinct source modes therefore have disjoint target coarse-frequency supports. In the unique allowed block, `a=0`, so `z^q=1` and

\[
A_{p,q}(k,u)
=
\frac{p}{\sqrt{pq\,h_{pq}}\,\Phi_p(z)}.
\tag{26}
\]

As the fresh `q`-mode varies, `z` runs through the nontrivial `q`-th roots of unity; the excluded point `z=1` is exactly the old `q`-coordinate. The profile is independent of `u`. Therefore the complete new-sector transfer restricted to the exact-order `p` source satisfies the **finite-level** identity

\[
\boxed{
T_{p,q}^*T_{p,q}=\lambda_{p,q}I_{E_p},
}
\tag{27}
\]

where

\[
\boxed{
\lambda_{p,q}
=
\frac{p}{q h_{pq}}
\sum_{j=1}^{q-1}
\frac{\sin^2(\pi j/q)}{\sin^2(\pi p j/q)}.
}
\tag{28}
\]

The pure exact-order `q` block is zero, so for a prime coarse base all new leakage is in exact order `pq`; nevertheless its source singular spectrum is exactly flat for every fresh prime `q`. The internal target vector survives, but it is the same reciprocal-`Phi_p` sampling profile repeated in mutually orthogonal coarse blocks.

As an explicit composite-base control, take `N=6`, `q congruent 1 (mod 6)`, source `u=1`, target coarse residue `b=3`, and the primitive root `t=1`. Then `a=2`, `sigma=1/2`, and PC-226 gives `H_1=8`. Equations (16)--(17) reduce to

\[
\boxed{
A_{6,q}\!\left(k_{1,j}^{(q)},1\right)
\longrightarrow
-\frac{\sqrt6}{12\pi}\,\frac1{j+1/2}.
}
\tag{29}
\]

This verifies concretely that the surviving fixed-base internal vector is a standard shifted Cauchy packet rather than a growing new spectral family.

## 7. Prior-art audit and RH boundary

The ingredients exposed by the reduction are established ones. The identity `Phi_{Nq}(z)=Phi_N(z^q)/Phi_N(z)` is standard cyclotomic theory. Root values of cyclotomic polynomials and finite Fourier transforms are classical, and the line already records the broad coefficient-theory boundary in Carlo Sanna's 2022 survey in `SOURCES.md`. The shifted `1/(j+sigma)` kernels and the cotangent/cosecant partial-fraction sums (23)--(24) are classical Cauchy/Hilbert--Mittag-Leffler analysis; the related even-power expansions are already anchored in `SOURCES.md` through Gauthier--Bruckman and were used in PC-036.

A directed literature search around fixed-old-factor/one-free-prime cyclotomic families, cyclotomic values at roots of unity, root-of-unity sampling of meromorphic functions, and discrete Cauchy/Hilbert kernels found established theories for each of those ingredients, but no independent RH mechanism based on the specific transfer (2) or the packet limit (16). No novelty is claimed for the abstract Cauchy kernel, root-value formulas, or one-free-prime coefficient theory. The durable content here is the project-specific classification of the **uncompressed fresh-prime Fourier state** left open by PC-224--PC-226.

The RH consequence is negative but sharply scoped. At fixed coarse `N`, letting a fresh prime grow cannot turn a single normalized `Phi_{Nq}` multiplication into a new Hilbert--Polya carrier merely by postponing singular-value compression and retaining every `q` Fourier mode. The only singular geometry comes from the simple poles of `1/Phi_N` at the already-known primitive coarse roots, producing finitely many rationally shifted Cauchy packets. There is no intrinsic complex spectral parameter, gamma factor, `s<->1-s` symmetry, explicit-formula zero term, or fresh-prime-dependent limiting operator beyond the finite residue label `q mod N`.

The theorem deliberately leaves three escapes open: a simultaneous limit in which the coarse base `N` itself grows; two or more source-forced noncommuting operations that act on the packet coordinate before it is quotiented or compressed; and a genuinely different intrinsic operator mixing the Cauchy packets across coarse residues or refinement stages. Those candidates must show information beyond the fixed cyclotomic residues and rational shifts classified above rather than merely spectralizing the same one-mask packet family.