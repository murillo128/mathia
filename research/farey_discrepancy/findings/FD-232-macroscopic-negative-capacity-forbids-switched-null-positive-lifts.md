# FD-232 — Macroscopic negative capacity forbids switched-null positive lifts

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response kernel / one-sided slack / positive-cone lifting / signed blind space / source realizability
- **Depends on:** FD-231, FD-230, FD-225
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + ONE-SIDED-SLACK + POSITIVE-LIFT-VETO + SWITCHED-BLIND-QUOTIENT`

## Claim

FD-231 shows that the signed divisor-response space contains linear-capacity profiles with uniformly first-order response. FD-230 shows that nonnegative profiles cannot retain a nonvanishing fraction of late dyadic capacity while remaining switched-subquadratic. Together they give a sharper source-realizability criterion: a signed blind correction can be lifted into one nonnegative occupancy by adding a nonnegative baseline only if its **negative part is itself aggregate-capacity sparse**.

Let

\[
(\mathscr A b)(m)
=
\sum_{d\le m} b_d M\!\left(\left\lfloor\frac md\right\rfloor\right),
\]

let

\[
B_k=[2^k,2^{k+1})\cap\mathbb N,
\]

and let the switched row orders be

\[
r_j=q_j+1=(1,4,4,1,4,4,\ldots).
\]

For a coefficient profile `v`, write

\[
\mathcal R_j(v)
:=
(E-I)^{r_j}(\mathscr A v)(2^j),
\]

where `E` shifts the dyadic sample index.

Assume a signed profile `(b_d)` satisfies

\[
|b_d|\le C_b d
\tag{1}
\]

and

\[
\mathcal R_j(b)=o(4^j).
\tag{2}
\]

A **positive lift** of `b` is a decomposition

\[
\boxed{a=b+s}
\tag{3}
\]

with

\[
a_d\ge0,\qquad s_d\ge0,
\tag{4}
\]

where `s` is the added nonnegative source slack. Suppose also that the physical occupancy has the same natural linear envelope,

\[
a_d\le C_a d.
\tag{5}
\]

Then the following implication is exact:

\[
\boxed{
\mathcal R_j(a)=o(4^j)
\quad\Longrightarrow\quad
\frac{\sum_{d\in B_k}b_d^-}
     {\sum_{d\in B_k}d}
\longrightarrow0.
}
\tag{6}
\]

In fact the added slack itself must satisfy

\[
\boxed{
\frac{\sum_{d\in B_k}s_d}
     {\sum_{d\in B_k}d}
\longrightarrow0.
}
\tag{7}
\]

Consequently, if a switched-blind signed correction has

\[
\limsup_{k\to\infty}
\frac{\sum_{d\in B_k}b_d^-}
     {\sum_{d\in B_k}d}>0,
\tag{8}
\]

then **no** positive lift with a linear capacity envelope can remain switched-subquadratic. Every such lift has

\[
\boxed{
\limsup_{j\to\infty}
\frac{|\mathcal R_j(a)|}{4^j}>0.
}
\tag{9}
\]

For the explicit signed blind profile constructed in FD-231, the obstruction is uniform on every late dyadic band. That finding proves

\[
\liminf_{k\to\infty}
\frac{\sum_{d\in B_k}b_d^-}
     {\sum_{d\in B_k}d}
\ge
\frac12\left(\frac{12}{\pi^2}-1\right)
\approx0.10793.
\tag{10}
\]

Hence any nonnegative baseline that lifts that profile must add asymptotically at least about `10.8%` of the natural aggregate linear capacity in every late band, before any further source constraints are imposed. FD-230 then forces that baseline to leak at the quadratic switched scale. The signed blind direction of FD-231 therefore cannot be converted into one physical nonnegative reservoir occupancy by adding an order-one positive offset.

The result does **not** show that the particular signed correction required to cancel the physical Mertens baseline has a macroscopic negative part. It identifies the exact one-sided obstruction that must now be tested on that affine correction class.

## 1. Positive lifting has an unavoidable cellwise slack tariff

From `a=b+s>=0` and `s>=0`, every coordinate with `b_d<0` obeys

\[
s_d=a_d-b_d=a_d+b_d^-\ge b_d^-.
\]

Thus

\[
\boxed{s_d\ge b_d^-\quad\text{for every }d.}
\tag{11}
\]

This is the pointwise source-realizability tariff. No choice of positive baseline can repair a negative correction coordinate using slack placed in another divisor cell; the occupancy constraint is coordinatewise.

The linear envelopes (1) and (5) also imply

\[
0\le s_d=a_d-b_d\le(C_a+C_b)d.
\tag{12}
\]

So the slack lies exactly in the nonnegative linear-capacity class covered by FD-230.

The distinction between `s` and `a` is important. FD-231 showed that a signed blind vector can be written abstractly as the difference of two feasible positive profiles after scaling. A physical lift is more restrictive: one starts with the signed correction that produces the needed response and adds a nonnegative baseline to make every final occupancy admissible. Equation (11) measures the irreducible amount of that baseline.

## 2. Two switched-null profiles would force the slack itself to be switched-null

The divisor-response map and every switched row are linear. Therefore (3) gives

\[
\mathcal R_j(s)
=
\mathcal R_j(a)-\mathcal R_j(b).
\tag{13}
\]

If both the signed correction and its positive lift are switched-subquadratic, (2) and (13) imply

\[
\boxed{\mathcal R_j(s)=o(4^j).}
\tag{14}
\]

Now apply FD-230 to the nonnegative profile `s`. Its hypotheses are exactly (12) and (14), so

\[
\frac{\sum_{d\in B_k}s_d}
     {\sum_{d\in B_k}d}
\longrightarrow0.
\tag{15}
\]

This proves (7). Combining (11) and (15) gives

\[
0\le
\frac{\sum_{d\in B_k}b_d^-}
     {\sum_{d\in B_k}d}
\le
\frac{\sum_{d\in B_k}s_d}
     {\sum_{d\in B_k}d}
\longrightarrow0,
\]

which is (6).

The contrapositive proves (8)--(9). Because the linear envelopes make every normalized switched response bounded, failure of `o(4^j)` is equivalently a strictly positive limsup after division by `4^j`.

This argument uses no new estimate for the Mertens function. The coercive input is exactly the positivity theorem of FD-230, whose proof ultimately comes from the immediate dyadic band entering the divisor response with `M(1)=1` and dominating the absolute older-band tail.

## 3. FD-231 pays a fixed one-sided slack fraction

For the FD-231 profile, both positive and negative parts carry a fixed fraction of aggregate capacity. In particular (10) holds. Applying the pointwise tariff (11) to any positive lift gives

\[
\liminf_{k\to\infty}
\frac{\sum_{d\in B_k}s_d}
     {\sum_{d\in B_k}d}
\ge
\frac12\left(\frac{12}{\pi^2}-1\right).
\tag{16}
\]

So the issue is not that one needs an arbitrarily tiny correction to a mostly positive signed profile. The explicit blind direction forces a genuinely macroscopic positive baseline on every late band.

At the same time FD-231 gives

\[
|\mathcal R_j(b)|=O(2^j)=o(4^j).
\]

If a positive lift `a=b+s` also had `mathcal R_j(a)=o(4^j)`, then `s` would satisfy (14), contradicting FD-230 and (16). Therefore every positive lift leaks at quadratic scale as stated in (9).

The same conclusion survives multiplication of `b` by any fixed positive scalar `lambda`. The required slack fraction in (16) is multiplied by `lambda`, but remains nonzero relative to that chosen correction scale. This is the source-side normalization relevant to the scale-adapted prime reservoirs of FD-226: shrinking the whole construction does not turn a capacity-comparable signed direction into a positive switched-null one after normalization by its own scale.

## 4. The remaining problem is an affine distance to the positive cone

FD-232 changes the useful search variable. The size of a signed correction in total variation is not decisive; FD-231 already disproves that. What matters is whether the **specific response-equivalence class** needed to cancel the physical baseline contains a representative whose negative part is aggregate-capacity sparse.

Let `N_sw` denote the signed linear-envelope profiles `h` satisfying

\[
\mathcal R_j(h)=o(4^j).
\]

If `c` is one correction producing the desired physical switched response, then replacing it by `c+h` with `h in N_sw` changes that response only below the quadratic scale. FD-232 gives the following necessary condition for a positive switched-subquadratic realization:

\[
\boxed{
\text{there must exist }h\in N_{\rm sw}
\text{ such that }
\frac{\sum_{d\in B_k}(c_d+h_d)^-}
     {\sum_{d\in B_k}d}
\longrightarrow0.
}
\tag{17}
\]

Thus the live quantity is a **one-sided cone distance after quotienting by the signed blind space**. A macroscopic total-variation norm can be harmless, but a macroscopic negative part that cannot be moved away inside the switched-null affine class is fatal to source realizability.

Condition (17) is only necessary. Vanishing negative band density does not imply that the remaining slack has small switched response, nor does it automatically fit the finite prime counts in every reservoir. The theorem therefore does not claim that the FD-226 bottleneck has been solved.

For the physical Mertens correction, the next decisive test is now precise: start from the exact FD-225 divisor inversion of the required baseline cancellation, allow the legitimate signed switched-null adjustments, and determine whether the negative part can be made aggregate-capacity sparse. A positive lower bound for (17)'s negative-band fraction would prove an intrinsic one-sided capacity obstruction; an explicit representative with vanishing negative fraction would reopen the constructive route.

## 5. Prior-art boundary and verdict

The external literature search found only the expected general material on Dirichlet convolution, divisor transforms and related convolution problems; no external theorem is needed for the lifting statement. No novelty is claimed for the elementary fact that a positive majorant must cover the negative part of a signed vector. The research-specific content is the combination of that cellwise cone constraint with the exact divisor-response representation and the nonnegative switched coercivity theorem FD-230.

No new source anchor is required in `SOURCES.md`. The proof depends only on persisted line results and linearity.

**Verdict.** The large signed blind space exposed by FD-231 is not itself a route around the physical capacity obstruction. Any switched-blind signed correction with a macroscopic negative capacity fraction requires a macroscopic nonnegative slack, and FD-230 forces that slack to become switched-visible. The remaining constructive question is therefore narrower: the actual Mertens correction, modulo legitimate signed blind directions, must approach the positive cone one-sidedly in late dyadic capacity. Total-variation smallness is irrelevant; negative-capacity sparsity is the necessary currency.