# PL-412 — Prime 5 is the unique right-half local cancellation channel; conditioning it away gives an exact RH analyticity criterion

**Evidence/status:** `EXACT-DERIVED + LITERATURE-AUDITED + CORRECTION/REPAIR + RH-EQUIVALENT-MODEL-CRITERION + FINITE-PRIME-DEALIASING`.

**Parent findings:** `PL-402`, `PL-403`, `PL-404`, `PL-411`.

## Claim

The endpoint Bernoulli law isolated in `PL-411` has a sharper arithmetic structure than previously recorded. Its Mellin transform

\[
N(s)=\mathbb E(M^{-s})
=\frac{C_2}{1+2^{-s-2}}\,
  \frac{\zeta(s+2)}{\zeta(2s+4)}\,G(s+1),
\tag{1}
\]

with

\[
G(u)=\prod_{p>2}\left(1+\frac{2}{(p-2)(p^{u+1}+1)}\right),
\tag{2}
\]

contains a previously unaudited cancellation channel. At a nontrivial denominator-zero location

\[
s_\rho=\frac\rho2-2,
\qquad \zeta(\rho)=0,
\tag{3}
\]

the local factor of `G(s+1)` for a prime `p>2` vanishes exactly when

\[
\rho=\beta_p+i\gamma_{p,k},
\qquad
\beta_p=\frac{2\log(p/(p-2))}{\log p},
\qquad
\gamma_{p,k}=\frac{2(2k+1)\pi}{\log p}.
\tag{4}
\]

Among all primes, **`p=5` is the unique local Euler factor whose zero locus can meet the right half of the critical strip** `1/2<Re(rho)<1`:

\[
\beta_3=2,
\qquad
\beta_5=\frac{2\log(5/3)}{\log 5}=0.634787\ldots,
\qquad
\beta_p<\frac12\quad(p\ge7).
\tag{5}
\]

Thus the blanket inference “every off-line zeta zero gives a pole of (1)” is not justified without a cancellation audit. The only local-factor obstruction on the RH-relevant side is the single prime coordinate `p=5`; the only other possible cancellation there is the numerator zero `zeta(rho/2)=0`.

Removing that one coordinate repairs the model exactly. Let

\[
M^{(5)}=\prod_{p>2,\,p\ne5}p^{X_p},
\qquad
\mathbb P(X_p=1)=\frac1{(p-1)^2},
\tag{6}
\]

with independent `X_p`, and put

\[
N_5(s)=\mathbb E((M^{(5)})^{-s}).
\tag{7}
\]

Then

\[
\boxed{
\mathrm{RH}
\iff
N_5(s)-\frac{2}{5(s+1)}
\text{ is holomorphic in }\Re s>-\frac74.
}
\tag{8}
\]

This is an exact **model analyticity criterion**, not a proof of RH. The value `-7/4` is still only the affine image of the critical line under `s=rho/2-2`; the substantive content is that a single finite-prime conditioning removes the only local Euler-factor alias on the right side, while an elementary descent argument rules out persistent numerator cancellation.

## 1. Exact local-zero audit of the Goldston--Suriajaya factor

Goldston--Suriajaya define

\[
G(u)=\prod_{p>2}g_p(u),
\qquad
g_p(u)=1+\frac{2}{(p-2)(p^{u+1}+1)}.
\tag{9}
\]

A local zero satisfies

\[
(p-2)(p^{u+1}+1)+2=0,
\]

hence

\[
p^{u+1}=-\frac{p}{p-2}.
\tag{10}
\]

Therefore

\[
u=-1+\frac{\log(p/(p-2))}{\log p}
  +i\frac{(2k+1)\pi}{\log p}.
\tag{11}
\]

At a denominator-zero point of (1), `u=s_rho+1=rho/2-1`, which gives (4).

The real-part classification is elementary. For `p=3`, (4) gives `beta_3=2`, so this factor cannot cancel a nontrivial zeta zero. For `p=5`, `beta_5=0.634787...`, which lies strictly between `1/2` and `1`. For `p>=7`, the inequality `beta_p<1/2` is equivalent to

\[
p-2>p^{3/4}.
\tag{12}
\]

It holds at `p=7`, and `x-2-x^{3/4}` is strictly increasing for `x>=7`, so it holds for every larger prime.

There is no hidden zero of the infinite product at the transformed right-half points once the individual local factors are nonzero. If `Re(rho)>1/2`, then at `u=rho/2-1`

\[
g_p(u)-1=O(p^{-1-\Re(\rho)/2}),
\]

uniformly for large `p`, and the prime sum converges absolutely. Hence the product is nonzero exactly when no local factor vanishes.

This audit also exposes a literature-level caution. In arXiv:2007.16099v1, equation (1.9) is exactly (9), while Lemma 3.1 states a blanket lower bound `G(s) \asymp_delta 1` on `-1+delta <= Re(s) <= 2`. But already the `p=3` factor vanishes at

\[
s=i\frac{(2k+1)\pi}{\log3},
\tag{13}
\]

so that lower bound cannot hold as written on every such strip. A targeted search on 2026-09-21 found no public erratum or correction addressing this local-zero issue. This finding does **not** declare the paper's global results invalid: the RH upper-bound contour argument uses upper control, and residue formulas remain meaningful with a zero coefficient when cancellation occurs. The correction here is to this research line's earlier use of the factorization as if noncancellation of every transformed zeta zero were automatic.

Primary source: D. A. Goldston and Ade Irma Suriajaya, “A singular series average and the zeros of the Riemann zeta-function,” *Acta Arithmetica* **200** (2021), 71--90, DOI `10.4064/aa200821-24-2`, arXiv: https://arxiv.org/abs/2007.16099. Relevant displayed source formulas are their equations (1.8)--(1.9), Lemma 2.1, and Lemma 3.1.

## 2. Conditioning away the exceptional coordinate

For the endpoint law of `PL-411`, the prime coordinates are independent with

\[
\mathbb P(X_p=1)=\frac1{(p-1)^2}.
\]

Conditioning on `X_5=0` simply deletes the `p=5` coordinate and leaves every other coordinate unchanged. Its normalization is

\[
C_{2,5}
=\prod_{p>2,\,p\ne5}\left(1-\frac1{(p-1)^2}\right)
=\frac{16}{15}C_2.
\tag{14}
\]

Initially for `Re(s)>-1`, where the probability Euler product converges absolutely,

\[
N_5(s)
=C_{2,5}\prod_{p>2,\,p\ne5}
 \left(1+\frac1{(p-2)p^{s+1}}\right).
\tag{15}
\]

Using the same factorization as in `PL-411`, but deleting the `p=5` local factor, gives the meromorphic continuation

\[
\boxed{
N_5(s)=
\frac{C_{2,5}}
 {(1+2^{-s-2})(1+5^{-s-2})}
\frac{\zeta(s+2)}{\zeta(2s+4)}
G_5(s+1),
}
\tag{16}
\]

where

\[
G_5(u)=\prod_{p>2,\,p\ne5}g_p(u).
\tag{17}
\]

The finite denominators in (16) have their zeros on `Re(s)=-2`, outside the target half-plane. The local poles of the factors in `G_5` also sit on that boundary, and the product is analytic in the region used below.

The relation with the original endpoint law is especially transparent:

\[
N(s)=L_5(s)N_5(s),
\qquad
L_5(s)=\frac{15}{16}+\frac{5^{-s}}{16}.
\tag{18}
\]

Since `PL-411` established `Res_{s=-1}N(s)=1/2` and `L_5(-1)=5/4`,

\[
\boxed{\operatorname*{Res}_{s=-1}N_5(s)=\frac25.}
\tag{19}
\]

This is the only pole that must be subtracted under RH inside `Re(s)>-7/4`.

## 3. The only remaining cancellation is numerator descent

Let `rho` be a nontrivial zeta zero with `Re(rho)>1/2`, and evaluate (16) at

\[
s_\rho=\frac\rho2-2.
\]

At this point:

- `zeta(2s+4)^{-1}` has a pole unless it is canceled;
- `zeta(s+2)=zeta(rho/2)` is the only numerator factor that can vanish;
- `zeta(rho/2-1)` is irrelevant here and, in the original singular-series factorization, is nonzero because its real part lies between `-3/4` and `-1/2` and its imaginary part is nonzero;
- the finite `p=2,5` denominators are nonzero because `|p^{-rho/2}|<1`;
- `G_5(rho/2-1)` is nonzero by Section 1: `p=3` would require `Re(rho)=2`, while every `p>=7` local zero requires `Re(rho)<1/2`.

Consequently, if the transformed denominator singularity is fully removable, then necessarily

\[
\zeta(\rho/2)=0.
\tag{20}
\]

The functional equation and conjugation then imply that

\[
T(\rho):=1-\frac{\overline\rho}{2}
\tag{21}
\]

is another nontrivial zeta zero. If `rho=beta+i gamma` with `beta>1/2`, then

\[
\Re T(\rho)=1-\frac\beta2>\frac12,
\qquad
\Im T(\rho)=\frac\gamma2.
\tag{22}
\]

Thus complete numerator cancellation at one right-half zero produces another right-half zero at half the height. If cancellation persisted at every iterate,

\[
\rho_{j+1}=T(\rho_j),
\]

then

\[
\Re\rho_j\to\frac23,
\qquad
\Im\rho_j\to0.
\tag{23}
\]

The zeros are distinct because their nonzero imaginary parts are successively halved, so they would accumulate at the finite point `2/3`. This is impossible for the analytic, nonzero function `zeta(s)` in a neighborhood of `2/3`. Therefore persistent numerator cancellation cannot occur. Some iterate must produce a genuine pole of `N_5`.

The same argument is insensitive to multiplicity: holomorphy at a transformed zero of any multiplicity requires at least one numerator zero, which is enough to continue the descent. Partial cancellation already leaves a pole.

## 4. Proof of the RH-equivalent analyticity criterion

Define

\[
H_5(s)=N_5(s)-\frac{2}{5(s+1)}.
\tag{24}
\]

Assume RH. Every nontrivial zero `rho` of `zeta(2s+4)` has transformed real part

\[
\Re\left(\frac\rho2-2\right)=-\frac74,
\]

so there are no denominator-zero poles in the open half-plane `Re(s)>-7/4`. In that half-plane `zeta(s+2)` has only its pole at `s=-1`; equation (19) removes exactly its principal part. The finite factors in (16) are nonzero there and `G_5(s+1)` is analytic. Hence `H_5` is holomorphic in `Re(s)>-7/4`.

Conversely, assume `H_5` is holomorphic in that half-plane and RH is false. By the functional equation there exists a nontrivial zero `rho_0` with `Re(rho_0)>1/2`. Its transformed point lies strictly inside the half-plane. Section 3 shows that if the corresponding denominator pole is removable, then `rho_1=T(rho_0)` is another right-half zero. Holomorphy forces the same cancellation at every iterate. Equation (23) then gives an impossible finite accumulation of zeta zeros. Therefore some iterate produces a genuine pole, contradicting holomorphy. This proves (8).

The criterion is deliberately model-level. It does not transfer RH information to the actual-prime source term of the prime-lattice program, and it does not explain why RH should hold. It does, however, give an exact falsifiable statement in which the rational-prime local structure is audited rather than hidden behind a generic Euler-product factor.

## 5. Correction and supersession scope

This finding narrows three earlier findings without erasing their valid content.

`PL-402` remains correct that the denominator `zeta(2s+2)` places the formal zero layer at `s=rho/2-1`, and its cubic Mellin calculation still proves that the continuation kernel itself does not annihilate those locations. What is superseded is the unqualified inference that **every** transformed zero is necessarily a pole before arithmetic-factor cancellation is checked.

`PL-403` retains its Abel regularization and the forward implication from RH to the stated model asymptotic. Its reverse implication, insofar as it relies on every off-line denominator zero surviving as a pole, is not accepted without the cancellation repair above. `PL-404` likewise retains the exact kernel-transfer identity and its Mellin nonvanishing statement, while the inherited unqualified reverse RH-equivalence is superseded by this audit.

`PL-411` already recorded the correct caution that numerator or local-factor cancellation had not been excluded. The present finding resolves that caution on the endpoint-law side: the local right-half ambiguity is concentrated exactly at `p=5`, and deleting that coordinate plus the descent argument gives the clean criterion (8).

This correction does **not** assert that any actual zeta zero lies on the exceptional `p=5` locus (4), and it does not assert that the Goldston--Suriajaya paper as a whole is invalid. It identifies a precise local-zero obstruction and removes it in the model.

## 6. Novelty audit and boundaries

The literature part is classical/prior art: the singular-series factorization, the Euler product `G`, and the Riesz-mean framework are from Goldston--Suriajaya. The standard zeta functional equation and isolated-zero principle are also classical.

The exact local-zero classification (4)--(5), the observation that `p=5` is the unique RH-relevant local cancellation coordinate, the conditioned Bernoulli law (6)--(17), and the descent proof of (8) are derived here. Targeted searches for the paper title together with “erratum”, “correction”, “Lemma 3.1”, and its arXiv identifier found no public discussion of this exact local-factor issue as of 2026-09-21. That search is not exhaustive and no publication-level novelty claim is made.

The result stays on the **model / singular-series side** of the research mandate. It does not solve the actual-prime transfer problem, does not produce a Hilbert--Polya operator, and does not derive the functional equation from the prime lattice. Finite-prime conditioning is a diagnostic repair: it shows exactly where the naive Euler-factor pole logic aliases, but it does not itself explain the critical line.

## Falsification conditions

The finding should be withdrawn or corrected if any of the following occurs:

1. the local equation (10) is shown not to be the zero condition for the published factor (9), or the source uses a materially different `G` in the relevant continuation;
2. a prime `p != 5` is shown to have `beta_p` in `(1/2,1)`, invalidating the uniqueness argument;
3. `G_5(rho/2-1)` can vanish at a right-half nontrivial zero despite absolute convergence and nonvanishing of every local factor;
4. the factorization (16) fails to give the stated meromorphic continuation in `Re(s)>-7/4`;
5. the functional-equation descent (21) fails to preserve the nontrivial zero set or the accumulation argument has an overlooked escape;
6. a prior source is found that already gives this finite-prime cancellation classification and repair, in which case the derived part should be reclassified as prior art rather than removed.
