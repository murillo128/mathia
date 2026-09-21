# PL-413 — Away-from-p singular-series projection exactly transports to endpoint Bernoulli conditioning

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + SOURCE-TO-MODEL-BRIDGE`.

**Parent findings:** `PL-404`, `PL-411`, `PL-412`.

## Claim

The finite-prime conditioning used in `PL-412` is not merely a model-side surgery. For every odd prime `p`, it is the exact image, under the endpoint reorganization of `PL-411`, of the standard arithmetic operation of removing the `p`-local singular-series factor, equivalently restricting the Ramanujan denominator to be coprime to `p`.

Let

\[
2A_{\eta,p}^{[2]}(H)
:=
\sum_{\substack{q\ge1\\(q,p)=1}}
\frac{\mu(q)^2}{\phi(q)^2}B_{q,\eta}(H),
\tag{1}
\]

where `B_{q,eta}(H)` is the same Ramanujan-source term used in `PL-404` and `PL-411`. Let `nu` be the probability law of `PL-411`,

\[
\nu(m)=C_2\prod_{\ell\mid m}\frac1{\ell(\ell-2)}
\qquad(m\ \text{odd and square-free}),
\tag{2}
\]

with independent prime coordinates

\[
\mathbb P_\nu(\ell\mid M)=\frac1{(\ell-1)^2}.
\tag{3}
\]

Then, for every odd prime `p`,

\[
\boxed{
2A_{\eta,p}^{[2]}(H)
=
\frac{1}{1-(p-1)^{-2}}
\sum_{\substack{m\ \mathrm{odd,squarefree}\\p\nmid m}}
\nu(m)P_\eta\!\left(\frac{H}{2m}\right)
}
\tag{4}
\]

and therefore

\[
\boxed{
2A_{\eta,p}^{[2]}(H)
=
\mathbb E_\nu\!\left[
P_\eta\!\left(\frac{H}{2M}\right)
\,\middle|\,
p\nmid M
\right].
}
\tag{5}
\]

For `p=5`, the normalization is `16/15`, so the endpoint law of the source observable (1) is exactly the conditioned law `X_5=0` used in `PL-412`. Thus the `p=5` de-aliasing in `PL-412` has a canonical arithmetic source realization: use the singular series **away from 5** before taking the endpoint transform.

This closes the source-to-model bridge left open in `PL-412`. It does **not** prove RH and does not by itself transfer the model analyticity criterion to unconditional prime-pair counts.

## 1. The source operation is standard prior art

Kuperberg defines, for a modulus `r`, the singular series away from `r` by deleting the local Euler factors at primes dividing `r`:

\[
\mathfrak S_r(\mathcal H)
=
\prod_{\ell\nmid r}
\frac{1-\nu_{\mathcal H}(\ell)/\ell}{(1-1/\ell)^{|\mathcal H|}}.
\tag{6}
\]

In the accompanying Ramanujan expansion the auxiliary denominators are correspondingly restricted by `(q_i,r)=1`. This is used to study singular-series sums in arithmetic progressions; it is not an operation introduced by this research line.

For the one-denominator pair source of `PL-404`/`PL-411`, taking `r=p` is exactly the projection in (1): retain only Ramanujan denominators `q` with `(q,p)=1`. The new content here is the exact identification of what that standard source-side projection becomes after the full endpoint Möbius reorganization of `PL-411`.

Primary source: Vivian Z. Kuperberg, “Sums of singular series along arithmetic progressions and with smooth weights,” *International Journal of Number Theory* **21** (2025), no. 1, 53–74, DOI `10.1142/S1793042125500046`, arXiv: https://arxiv.org/abs/2301.06095. See in particular equations (4)–(6) in the introduction: the definition of `S_r` away from `r` and the Ramanujan denominators constrained by `(q_i,r)=1`.

## 2. Exact transport through the PL-411 reindexing

The proof requires no analytic continuation. The series in (1) is a subseries of the absolutely convergent source treated in `PL-411`, so the same divisor expansion, Fubini interchange, and primewise reindexing remain valid.

Repeat the coefficient calculation of `PL-411` for a fixed square-free endpoint divisor. At a prime `p` not contained in that divisor, the unrestricted `q`-sum contributes the local factor

\[
1-\frac1{(p-1)^2}.
\tag{7}
\]

After imposing `(q,p)=1`, the `p`-part of `q` is forced to be absent, so this local contribution becomes `1`. Hence every surviving endpoint coefficient with `p\nmid m` is multiplied by

\[
\frac1{1-(p-1)^{-2}}
=
\frac{(p-1)^2}{p(p-2)}.
\tag{8}
\]

If `p\mid m`, the relevant divisor channel requires the `p`-part that has just been removed from the Ramanujan source, and its coefficient is zero. Therefore the transformed coefficient is exactly

\[
\nu_p(m)
=
\frac{\mathbf 1_{p\nmid m}\nu(m)}{1-(p-1)^{-2}}.
\tag{9}
\]

But (3) gives

\[
\nu(p\nmid M)=1-\frac1{(p-1)^2},
\tag{10}
\]

so (9) is precisely the conditional law `nu(. | p does not divide M)`. Substitution into the endpoint formula of `PL-411` proves (4) and (5).

The normalization also provides an internal check. Summing (9) over `m` gives one, and at `p=5`

\[
\frac1{1-1/16}=\frac{16}{15},
\tag{11}
\]

which is exactly the normalization `C_{2,5}/C_2` in `PL-412`.

## 3. Consequence for the exceptional p=5 channel

`PL-412` showed that, in the continued Mellin transform of the endpoint law, `p=5` is the unique local Euler factor capable of canceling a transformed nontrivial zeta zero with `1/2<Re(rho)<1`. The repair there was to delete the Bernoulli coordinate `X_5` and use

\[
M^{(5)}=\prod_{\ell>2,\,\ell\ne5}\ell^{X_\ell}.
\tag{12}
\]

Equation (5) now shows that this random variable is not an independently chosen modification. In distribution,

\[
M^{(5)}\overset d= M\mid 5\nmid M,
\tag{13}
\]

and the latter is exactly the endpoint image of the standard away-from-5 source statistic

\[
2A_{\eta,5}^{[2]}(H)
=
\sum_{(q,5)=1}\frac{\mu(q)^2}{\phi(q)^2}B_{q,\eta}(H).
\tag{14}
\]

Consequently the Mellin transform `N_5(s)` in `PL-412` is the Mellin transform of the endpoint probability law arising from a declared arithmetic observable, not merely from finite-prime conditioning imposed after the fact. All analytic-continuation and local-cancellation statements remain those already audited in `PL-412`; (4)–(14) are exact identities in the absolutely convergent source regime and do not obtain their validity from continuing an Euler product.

This matters because the canonical research contract excludes ad hoc weights and unmotivated finite differences. The operation in (14) survives that filter: deleting a local singular-series factor at a prescribed modulus is standard arithmetic-progression machinery, and Kuperberg's formulation supplies an independent literature anchor for it.

## 4. Scope and adversarial audit

**No actual-prime theorem is claimed.** Equations (4) and (5) are identities for the singular-series/Ramanujan observable. Connecting `A_{eta,p}^{[2]}` to statistics of actual prime pairs still requires the relevant Hardy–Littlewood or arithmetic-progression remainder control. The bridge closes a model/source mismatch; it does not supply that missing prime-counting input.

**Odd primes only.** The probability law of `PL-411` lives on odd square-free `m`; the prime `2` is already separated into the parity normalization and the scale `H/(2m)`. Formula (4) is therefore stated only for odd `p`. Treating `p=2` by the same notation would conflate two different roles.

**Convergence is inherited, not guessed.** Restricting the absolutely convergent `q`-series of `PL-411` to `(q,p)=1` cannot worsen convergence. The exact reindexing is therefore justified in the same domain as the parent finding. The later meromorphic continuation of `N_5` belongs to `PL-412` and is not used to prove the source identity.

**No hidden independence assumption is introduced.** Independence of the endpoint coordinates was proved by the factorized law in `PL-411`. Conditioning on `p\nmid M` deletes one Bernoulli coordinate and leaves the others with their original product law. Equation (9) derives the same conditional measure directly from the source projection, so the two constructions meet exactly rather than heuristically.

**Novelty is deliberately narrow.** The exponent-vector picture, Ramanujan expansion, singular series away from a modulus, and the use of coprimality restrictions on Ramanujan denominators are prior art. A targeted literature audit found Kuperberg's explicit away-from-`r` construction but did not locate the specific transport identity (4)–(5) linking that source projection to the endpoint Bernoulli law of `PL-411`. The line-level contribution is therefore the derived bridge and its `p=5` consequence, not the source operation itself.

## 5. Representation assessment

The alternate representation is useful because it turns a model-side condition into a source-side arithmetic operation. The map is

\[
\{q:(q,p)=1\}
\quad\longmapsto\quad
\{m:p\nmid m\}
\tag{15}
\]

under the full divisor/Möbius endpoint transform of `PL-411`.

It preserves every local weight away from `p`, the endpoint kernel `P_eta(H/(2m))`, and the independence of all remaining prime coordinates. It changes exactly one thing: the `p`-containing source sector is discarded and the surviving measure is renormalized by `(1-(p-1)^(-2))^{-1}`. The map is therefore not invertible without retaining the complementary `p`-divisible sector; information about that discarded sector is genuinely lost.

The relevant domain is the absolutely convergent endpoint transform of `PL-411`, with `p` an odd prime. In particular, no branch choice or analytic-continuation convention enters the derivation of (4)–(5).

## 6. Research consequence

The open issue after `PL-412` was whether the exceptional local de-aliasing at `p=5` could be traced back to a natural arithmetic statistic rather than being chosen because the continued Euler product exposed `p=5` as inconvenient. Equations (5) and (14) answer that question positively: **yes, the conditioned endpoint law is exactly the transform of the singular series away from 5.**

This removes one arbitrariness objection to the repaired model criterion. The remaining bottleneck is more substantive: determine whether an away-from-5 singular-series observable with the required endpoint transform can be connected, with sufficiently strong and uniform error control, to an actual prime statistic. Without such a source theorem, the RH-equivalent analyticity statement of `PL-412` remains a model criterion rather than a mechanism proving RH.
