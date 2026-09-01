# WI-068 — Shao--Teräväinen opens the free-shift rectangle, not the fixed-shift residue square

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + CORRECTION + DECISIVE-NEGATIVE`. This finding is the corrected successor to the withdrawn `WI-067` after adversarial review. It does **not** change Mathia's current unconditional simple-critical proportion, does not weaken the exact residue-square identity of WI-066, and does not rule out a source-faithful use of shift-averaged prime-pattern technology. It corrects one load-bearing overclaim: Shao--Teräväinen Theorem 2.7 does not by itself control the four-prime rectangle at a prescribed fixed shift `h`. The theorem applies to the three-variable finite-complexity rectangle only while the shift itself remains a genuine summation variable.

## 1. Primary theorem surface: finite complexity explicitly excludes the fixed twin-prime direction

The load-bearing source is Xuancheng Shao and Joni Teräväinen, **The Bombieri--Vinogradov theorem for nilsequences**, *Discrete Analysis* 2021:21, arXiv:2006.05954v2, Theorem 2.7:

- for fixed `epsilon>0` and fixed `A,t,d,M`, with `Q<=x^(1/3-epsilon)`, all but `O(Q/(log x)^A)` moduli `q<=Q` are good;
- for every good `q`, every residue vector `a in (Z/qZ)^d`, and every **finite-complexity** tuple of nonconstant affine-linear forms of bounded size, the theorem gives the expected prime-pattern asymptotic over the full box `[1,x]^d`;
- immediately before the theorem, the source explicitly says that the finite-complexity hypothesis excludes, for example, counting twin primes or binary Goldbach representations.

Primary source:

https://arxiv.org/abs/2006.05954v2

The modulus range and the uniformity over every residue vector remain exactly as recorded in the withdrawn WI-067. The correction concerns which rectangle is represented by the theorem's summation variables.

## 2. Exact variable map: the successful reparametrization averages over `h`

Consider the fixed three-variable system

\[
\Psi(u,v,w)=(u,\ u+v,\ u+w,\ u+v+w).
\tag{1}
\]

Its homogeneous coefficient vectors

\[
(1,0,0),\ (1,1,0),\ (1,0,1),\ (1,1,1)
\tag{2}
\]

are pairwise nonproportional, so this is a finite-complexity system of the kind consumed by Theorem 2.7. For residues `(a,b,0) mod q` and theorem variables `(m_1,m_2,m_3)`, one gets

\[
\begin{aligned}
L_1(q\mathbf m+\mathbf a)&=qm_1+a,\\
L_2(q\mathbf m+\mathbf a)&=q(m_1+m_2)+a+b,\\
L_3(q\mathbf m+\mathbf a)&=q(m_1+m_3)+a,\\
L_4(q\mathbf m+\mathbf a)&=q(m_1+m_2+m_3)+a+b.
\end{aligned}
\tag{3}
\]

Renaming the four arguments as

\[
(n,\ n+h,\ n+r,\ n+h+r)
\tag{4}
\]

gives the exact relations

\[
\boxed{h=q m_2+b,\qquad r=q m_3.}
\tag{5}
\]

Thus the theorem's sum over `m_2` is a sum over a progression of shifts `h`. The residue `b` fixes only `h mod q`; it does **not** fix one value of `h`. Summing over `b mod q` fills the corresponding shift range rather than isolating a prescribed booked shift.

Schematically, after the ordinary box and residue bookkeeping, Theorem 2.7 can address an object of the form

\[
\boxed{
\sum_{h\ \mathrm{in\ a\ long\ range}}
\sum_{q\mid r}
\sum_n
\Lambda(n)\Lambda(n+h)\Lambda(n+r)\Lambda(n+r+h),
}
\tag{6}
\]

not the individual fixed-shift slice

\[
\boxed{
\sum_{q\mid r}
\sum_n
\Lambda(n)\Lambda(n+h)\Lambda(n+r)\Lambda(n+r+h)
}
\tag{7}
\]

with `h` prescribed in advance.

This distinction survives the theorem's strong quantifier “for every residue vector”: choosing `b=h mod q` selects the congruence class of `h`, but `m_2` still ranges over the whole theorem box.

## 3. Freezing `h` destroys finite complexity

If `h` is fixed before invoking the prime-pattern theorem, the natural remaining variables are `(u,w)` and the four forms become

\[
L_1=u,\qquad
L_2=u+h,\qquad
L_3=u+w,\qquad
L_4=u+w+h.
\tag{8}
\]

Their homogeneous coefficient vectors are

\[
(1,0),\ (1,0),\ (1,1),\ (1,1).
\tag{9}
\]

The first two forms have identical homogeneous parts, as do the last two. In particular the system contains the fixed twin-prime direction `(u,u+h)`. This is precisely the kind of configuration excluded by the finite-complexity hypothesis highlighted by Shao--Teräväinen themselves.

Keeping a dummy third variable does not repair the issue: if the forms are independent of that variable, the repeated homogeneous directions remain. Nor can the printed `o(x^3)` statement for the full three-dimensional box simply be restricted to one value of `m_2`: a fixed-`m_2` slice is only two-dimensional, and Theorem 2.7 supplies no such slice estimate. Any argument that localizes the free `m_2` average to one booked shift needs an additional theorem or a quantitatively stronger source-specific device.

Therefore the map (3)--(5) is valid but proves a narrower statement than WI-067 claimed:

\[
\boxed{
\text{moving }q\text{ into progression coordinates works together with a free shift variable;}\\
\text{it does not turn a fixed-shift twin-pair rectangle into finite complexity.}
}
\tag{10}
\]

## 4. Consequence for WI-066: the exact fixed-`h` residue square remains open

WI-066 proved the exact identity, for fixed nonzero booked shift `h`,

\[
\sum_{a\bmod q}|\Psi_q(a;h)|^2
=
\sum_{q\mid r}\sum_n
\Lambda(n)\Lambda(n+h)\Lambda(n+r)\Lambda(n+r+h),
\tag{11}
\]

with the physical interval restrictions understood. Nothing in the present correction changes (11), its centered expansion, or the fact that opening the residue `L^2` norm raises the correlation order from two primes to four.

The withdrawn WI-067 correctly noticed that the congruence `q|r` need not be represented as the growing coefficient `r=qs` when **both** shifts are allowed to vary. It went too far when it concluded that Theorem 2.7 therefore “addresses the first, genuinely four-prime term” in the fixed-`h` centered residue square. Equation (8) shows that the obstruction in the fixed slice is not merely where the modulus `q` is written: the prescribed prime-pair separation itself leaves an infinite-complexity/twin-prime direction.

Accordingly, the `X^{o(1)}` conductor range isolated by WI-058 is indeed far inside the nominal power-modulus range of Theorem 2.7 **for the genuinely free-shift three-variable aggregate**. That observation remains useful. It cannot be promoted to a theorem for (11) without first recovering an admissible shift average.

## 5. The Yang source does contain a shift average, but the required theorem map is not yet proved

This correction does not imply that the Shao--Teräväinen route is irrelevant to the actual Yang welding program. The residue-summed quantity introduced in WI-066 is eventually summed over a booked shift family,

\[
V_q(\mathcal H)
=\sum_{h\in\mathcal H}\sum_{a\bmod q}
|\widetilde E_q(a;h)|^2,
\tag{12}
\]

and WI-061 records that, on the booked Yang subfamily used there, the map from the source lock parameter `k` to the pair shift `h_2(k)` is injective into Mikawa's shift range. The pinned Yang paper likewise states that its intended band consumer applies Cauchy--Schwarz only in the shift variable and introduces a source welding weight

\[
w_k(n)=\sum_{m\in I(n)}\Lambda(m)\Lambda(m-rk).
\tag{13}
\]

So there is a genuine possibility that a **source-faithful weighted shift average** could restore a finite-complexity theorem interface.

But that identification is an additional proof obligation, not a consequence of Theorem 2.7. The actual Yang shift is locked to the same source parameter that controls the second prime pair, the coefficient bases, moving intervals, Mertens/source weights, collision exclusions, and the local-main subtraction. WI-042 already records that the public reproduction tree does not contain the advertised shift-first analytic consumer; its executable ledger instead uses a forbidden across-family square norm. WI-061 likewise keeps the two-leg locked geometry and moving-interval splice as explicit unresolved gates.

To rehabilitate the positive part of WI-067 for the Yang contraction one must therefore derive, before invoking Theorem 2.7, an exact or loss-controlled reduction of the **actual weighted locked shift family** to a bounded or quantitatively admissible collection of three-variable free-shift boxes. That derivation must map every theorem variable, keep the source weights and truncations, and show that the coefficient-size and exceptional-modulus losses remain within budget. No such reduction is currently established in this line.

## 6. Prior-art boundary

No novelty is claimed for finite-complexity linear equations in primes, for the fact that fixed twin-prime patterns lie outside that framework, for arithmetic-progression coordinates, or for averaging a shift parameter to create a finite-complexity system. These are established features of the Green--Tao/Shao--Teräväinen framework.

The closest already-persisted arithmetic inputs remain complementary rather than substitutes:

- Shao--Teräväinen Theorem 2.7 proves the large-modulus finite-complexity statement when the shift remains a summation variable.
- Mikawa's prime-pair-in-progressions theorem, reconstructed in WI-061, directly treats the two-prime object and averages over shifts, but opening the residue square still produces the four-prime rectangle of WI-066.
- Shao--Teräväinen Theorem 1.3, used in WI-054, controls modulus-averaged nilsequence-twisted **pair fibers** on a restricted exponent region; it does not assert the fixed-`h` four-prime asymptotic (7).

A targeted check around prime multiplets in arithmetic progressions and fixed-shift prime-pair variance did not locate a published theorem whose printed interface may simply replace Theorem 2.7 in (7) over the full `X^{o(1)}` conductor family with the Yang source weights. That bounded search is not used as a novelty, priority, or impossibility claim.

The durable Mathia contribution here is only the theorem-interface correction: the exact map (5) shows what Shao--Teräväinen actually averages, and (8)--(9) show why the fixed slice is outside the theorem's finite-complexity hypothesis.

## 7. Updated decision tree and falsification gate

The corrected arithmetic frontier is now:

1. **Fixed `h`:** WI-066's residue square remains a four-prime twin-pair rectangle not controlled by Shao--Teräväinen Theorem 2.7 as a black box.
2. **Free `h`:** the three-variable rectangle is finite complexity, and Theorem 2.7 removes the mere `X^{o(1)}` modulus-range objection for almost all conductors, subject to the theorem's local-factor, exceptional-set, box, and quantitative-error bookkeeping.
3. **Actual Yang lock:** unresolved. The source has a shift average, but it is weighted and coupled. A proof must show that this average is sufficiently close to the free theorem variable before the large-modulus result can be consumed.

Narrow or supersede this finding if either of the following is established:

- an exact source-faithful Yang regrouping turns the weighted locked shift family into the three-variable finite-complexity average of Theorem 2.7 (or a controlled finite combination of such averages), with all weights, moving domains, local factors, exceptional moduli, and errors inside the Yang budget; or
- a stronger established theorem is located that directly controls the fixed-shift system (8) in the required modulus/weight range.

Until one of those gates is passed, the valid statement is

\[
\boxed{
\text{Shao--Teräväinen opens the shift-averaged rectangle, not the fixed-shift residue square.}
}
\tag{14}
