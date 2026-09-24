# MC-503 — Fixed hard-mask profiles obey an effective-support conductor-start tariff

**Status:** `EXACT-DERIVED` · `CLASSICAL-FOURIER+DERIVED-APPLICATION` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-495` reduces the live incomplete repeated-residue cross-root branch to a nonnegative source weight against one fixed conductor phase, while `MC-502` shows that the complete-period lower-prime hard mask supplies only logarithmic/totient coherence. A possible remaining escape is that an **incomplete** lower-prime mask might itself correlate strongly with the conductor phase because its support is highly irregular.

For the quadratic repeated-residue phase of `MC-497`, mere irregularity of a **fixed coefficient profile** is not enough. Once the profile is fixed, averaging only its relative translation against the conductor phase gives a sharp effective-support tariff with no primorial or auxiliary-sieve dimension cost.

Let `p` be an odd prime and let

\[
F:\mathbf F_p\to\mathbf C
\]

satisfy

\[
\sum_{x\bmod p}F(x)=0
\tag{1}
\]

and, for the unnormalized additive Fourier transform

\[
\widehat F(k)=\sum_{x\bmod p}F(x)e_p(-kx),
\qquad e_p(y)=e^{2\pi i y/p},
\tag{2}
\]

the nonzero-frequency bound

\[
|\widehat F(k)|\le C\sqrt p
\qquad(k\ne0).
\tag{3}
\]

Fix `1<=H<=p` and arbitrary complex coefficients `b_1,...,b_H`. For each conductor start `x mod p`, set

\[
T_b(x)=\sum_{j=1}^H b_jF(x+j).
\tag{4}
\]

Then

\[
\boxed{
\sum_{x\bmod p}|T_b(x)|^2
\le C^2p\sum_{j=1}^H|b_j|^2.
}
\tag{5}
\]

Equivalently,

\[
\boxed{
\frac1p\sum_x|T_b(x)|^2
\le C^2\|b\|_2^2.
}
\tag{6}
\]

If the coefficients are nonnegative and not all zero, write

\[
M_b=\sum_j b_j,
\qquad
R_b=\frac{M_b^2}{\sum_jb_j^2}.
\tag{7}
\]

For every `eta>0`, the set of relative conductor starts carrying fixed normalized bias satisfies

\[
\boxed{
\frac1p\#\left\{x:\ |T_b(x)|\ge\eta M_b\right\}
\le
\frac{C^2}{\eta^2R_b}.
}
\tag{8}
\]

In particular, for an exact `0/1` hard-mask segment with `M` surviving positions,

\[
R_b=M,
\qquad
\boxed{
\frac1p\#\left\{x:\ |T_b(x)|\ge\eta M\right\}
\ll_\eta \frac1M.
}
\tag{9}
\]

The quadratic relative phase left by `MC-495` satisfies `(1)`--`(3)` with an absolute `C`, by the Fourier--Weil calculation in `MC-497`. Therefore **any fixed incomplete lower-prime mask profile, no matter how irregular or how large its auxiliary period is, can have order-one normalized correlation with that phase only on a conductor-start set priced by the profile's effective support**.

This does not yet control the actual first-exit family. The mask profile itself varies with the source labels `q,r`, and the physical source may select one exceptional conductor start for each varying profile. The surviving mechanism is consequently sharper than “incomplete hard masks may be nonuniform”: it must be a **source-forced alignment between the q-dependent mask profile and that profile's exceptional conductor start**, or else a profile with genuinely small effective support. A genuinely q-dependent signed/complex coefficient inserted before the nonnegative aggregation of `MC-495` remains a separate escape.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Weighted Fourier diagonalization

Extend the coefficient vector by zero to a function on `F_p` and define

\[
\widehat b(k)=\sum_{j=1}^Hb_je_p(kj).
\tag{10}
\]

Because `H<=p`, the positions `1,...,H` are distinct modulo `p`. Fourier inversion gives

\[
T_b(x)
=\frac1p\sum_{k\bmod p}
\widehat F(k)\widehat b(k)e_p(kx)
\tag{11}
\]

up to the harmless Fourier-sign convention. By `(1)`, the zero mode vanishes. Parseval therefore gives exactly

\[
\sum_x|T_b(x)|^2
=\frac1p\sum_{k\ne0}
|\widehat F(k)|^2|\widehat b(k)|^2.
\tag{12}
\]

Using `(3)` yields

\[
\sum_x|T_b(x)|^2
\le C^2\sum_k|\widehat b(k)|^2.
\tag{13}
\]

A second Parseval identity gives

\[
\sum_k|\widehat b(k)|^2
=p\sum_{j=1}^H|b_j|^2,
\tag{14}
\]

which proves `(5)`--`(6)`. Chebyshev applied to `(6)` and the definition `(7)` gives `(8)`.

Nothing in this argument requires `b` to be an interval, a smooth weight, a random mask, a periodic mask, or a product of local sieve factors. The whole coefficient profile is retained exactly. The only analytic input is the square-root bound `(3)` for the nonzero additive Fourier multipliers of the conductor phase.

## 2. Specialization to the MC-495 quadratic phase

For one repeated source residue `a mod p`, `MC-495` reduces the cross-root phase, after the physical first-exit reparameterization, to

\[
R_a(m)=\chi\!\left(1-\frac{h^2}{a^2m^2}\right)
\tag{15}
\]

away from its character zeros. In the quadratic case `MC-497` uses the equivalent polynomial representative

\[
R_c(m)=\chi(m^2-c^2)
\tag{16}
\]

with the exact one-point convention there, and centers it as

\[
F_c(m)=R_c(m)-\mu_c.
\tag{17}
\]

That finding proves

\[
\widehat F_c(0)=0,
\qquad
|\widehat F_c(k)|\ll\sqrt p
\quad(k\ne0)
\tag{18}
\]

uniformly in the nonzero parameter `c`. Hence `(5)`--`(9)` apply uniformly to every fixed source-derived coefficient profile against the quadratic relative phase.

For the uncentered phase, one simply writes

\[
\sum_jb_jR_c(x+j)
=\mu_cM_b+T_b(x).
\tag{19}
\]

Since `|mu_c|<=2/p` in `MC-497`, the completed mean is an explicit `O(M_b/p)` term. Any fixed order-one normalized bias for large `p` must therefore still come from the centered term controlled above.

## 3. Exact hard masks are included without a sieve approximation

Consider one fixed plus/minus first-exit pair and one physical overlap segment. Let `b_j` be the exact product of all lower-prime hard-mask indicators on the `j`th point of that segment. Then `b_j` is exactly `0` or `1`; no Selberg/beta-sieve envelope, complete-period replacement, independent-random model, or smoothing is introduced.

If the segment contains `M` actual survivors, `(9)` says that among all relative conductor translations of this **same exact mask shape**, only `O_eta(p/M)` conductor residues can support bias at least `eta M`.

More generally, after exact nonnegative source aggregation as in `MC-495`, a fixed finite profile can have unequal coefficients. Equation `(8)` then replaces cardinality by the correct participation quantity

\[
R_b=\frac{\|b\|_1^2}{\|b\|_2^2}.
\tag{20}
\]

Thus amplitude concentration, not raw interval length or the auxiliary-sieve period, is the relevant cost once the coefficient profile is frozen.

This is deliberately different from completing the hard mask modulo its primorial period. The proof never expands the mask into all auxiliary Fourier modes, so it never pays the full frequency dimension exposed by `MC-475`. The lower-prime arithmetic is retained in physical space inside the exact vector `b`.

## 4. Relation to MC-475 and MC-502

`MC-475` proves that a fixed physical interval paired with the **full auxiliary Fourier expansion** of the centered pair-sieve mask has a dual response energy of order `WH` in the sparse regime `H<W`. That result closes the cheap strategy “small mask Fourier `ell^2` norm plus Cauchy over every auxiliary frequency.”

The present estimate changes the order of operations. It freezes the actual physical coefficient vector first and averages only the **relative conductor translation**. Fourier analysis is then performed solely on the conductor group `F_p`, whose nonzero multipliers are already square-root bounded by `MC-497`. The primorial dimension never appears because no auxiliary Fourier frame is created.

There is no contradiction. `MC-475` addresses a fixed start while summing over the complete auxiliary-frequency family; `(5)` addresses a fixed coefficient profile while averaging over conductor starts. They forget different information and therefore expose different tariffs.

Likewise, `MC-502` says that complete-period plus/minus hard-mask overlap remembers source labels only through the `q+r` collision invariant, with at most logarithmic/totient enhancement. The current theorem does not use that complete-period density at all. It says that even an **incomplete** profile can beat the conductor phase only by landing on its sparse exceptional-start set when its effective support is large.

Together the two findings leave a precise residual question: can the exact first-exit source map correlate the changing lower-prime mask profile with the changing physical conductor start strongly enough to select those exceptional pairs systematically?

## 5. Representation audit

The source-to-representation map is lossless for the statement proved. A finite incomplete hard-mask segment is stored as its actual coefficient vector `b`; every zero, surviving position, and nonuniform nonnegative amplitude is retained. The theorem then varies only the relative conductor translation `x` while keeping that profile fixed.

This relative translation is a diagnostic degree of freedom, not an assertion that the physical first-exit source samples conductor starts uniformly. If the mask comes from an auxiliary period `W` coprime to `p`, CRT shows that one may vary the conductor residue while holding the same auxiliary start class, but the actual source family need not populate those CRT fibres evenly or at all.

Therefore `(8)` is an **exceptional-set theorem conditional on a fixed profile**, not a source-average theorem. To transfer it to the full first-exit family one must control how physical source labels populate conductor starts after conditioning on the relevant mask/profile information. Treating the uniform conductor average as though it were the actual source measure would erase the live alignment question and is forbidden.

## Prior art and novelty boundary

The abstract inequality `(5)` is finite Fourier analysis plus Parseval. Square-root control of the nonzero conductor multipliers is classical Weil/Stepanov theory; `MC-S55` records Cochrane--Pinner as the primary source used by this line. Moving-start character sums and sifted character sums are established subjects; a targeted audit found, among others, Adam J. Harper's *A note on character sums over short moving intervals* (J. Inst. Math. Jussieu 24 (2025), 1395--1427, DOI `10.1017/S1474748025000039`) and Jan-Christoph Schlage-Puchta's *Sifted character sums and free quotients of Bianchi groups* (Math. Proc. Camb. Phil. Soc. 141 (2006), 205--207, DOI `10.1017/S0305004106009261`). Neither is used as a black-box theorem for `(5)`.

No novelty is claimed for weighted Parseval, moving-start mean squares, or sifted character-sum language. The durable Mathia contribution is the exact frontier specialization: the lower-prime mask excluded from the endpoint-only `MC-497`/`MC-498` theorem can be retained as an arbitrary fixed coefficient profile without worsening the conductor-start second moment beyond its `ell^2` mass. This converts the live hard-mask escape into a source/profile-to-exceptional-start **alignment** problem.

## Boundaries and falsification tests

- **Quadratic relative phase for the current application.** The abstract theorem needs only `(1)`--`(3)`, but `MC-497` supplies those hypotheses here for the quadratic repeated-residue phase. Higher-order characters require their own uniform nonzero-Fourier audit.
- **Fixed profile while the conductor start varies.** If changing the source label simultaneously changes `b`, `(8)` cannot be averaged across labels without an additional conditional-participation argument.
- **Effective support can be small.** A profile concentrated on few positions has small `R_b`, and the theorem then permits a large exceptional set. Such concentration must be measured rather than assumed absent.
- **No uniform pointwise character bound.** A single adversarial conductor start may still have order-one bias; the theorem only prices how sparse such starts are for each fixed profile.
- **No auxiliary-period equidistribution assumption.** The proof neither assumes nor proves that physical source starts are uniform modulo a lower-prime period.
- **No replacement of the actual hard mask.** The strength of the result is precisely that `b` may be the exact incomplete source profile.
- **Range `H<=p`.** This keeps the coefficient support injective modulo `p`. Longer profiles require folding coefficients by residue class before applying the same Fourier argument, with the resulting `ell^2` concentration charged explicitly.
- **No collective all-pair bound.** Different `(q,r)` pairs may carry different profiles and may select different exceptional starts. Controlling that source/profile alignment is the next unresolved step.
- **No global Möbius conclusion.** There is no new bound for `M(x)`, no zero-free region, and no RH consequence.

## Consequence for the accepted clue

The accepted q-vdC clue no longer needs to treat arbitrary incomplete lower-prime irregularity as an unconstrained new phase resource. For each fixed exact profile, the quadratic conductor phase imposes the tariff `(8)`.

The hard-mask branch should therefore ask for the **conditional source participation across conductor starts at fixed or suitably controlled mask profile**. If physical first-exit labels distribute across many conductor starts while retaining enough common profile/effective support, `(8)` gives cancellation without ever completing the sieve mask. If instead each q-dependent profile is paired with one specially aligned exceptional conductor start, that profile--start dependence is itself the arithmetic resource that must be derived and bounded.

Thus the residual hard-mask route is now one of two explicit mechanisms: low effective support, or source-forced exceptional alignment. Complete-period `q+r` coherence is already logarithmic by `MC-502`, and generic fixed-profile irregularity is priced by the present conductor-start theorem. A genuinely q-dependent signed or complex coefficient before nonnegative aggregation remains separately admissible.

## Sources

- `MC-495`: reduction of incomplete repeated-residue cross-root interference to a nonnegative source profile against one relative phase.
- `MC-497`: centered quadratic relative phase and the uniform nonzero additive-Fourier square-root bound.
- `MC-502`: complete-period plus/minus hard-mask `q+r` coherence ceiling.
- `MC-S55`: Cochrane--Pinner complete mixed additive/multiplicative character-sum bound.
