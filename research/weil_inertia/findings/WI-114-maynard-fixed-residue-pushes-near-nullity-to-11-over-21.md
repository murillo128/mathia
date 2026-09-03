# WI-114 — Maynard fixed-residue distribution pushes full-packed near-nullity beyond the square-root barrier

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding does **not** improve Mathia's unconditional simple-critical zero proportion and does not certify the Yang--Yang one-sided fourth-moment candidate. It strengthens WI-111--WI-113's obstruction to repairing the exact full-packing Ramanujan interface: Maynard's published fixed-residue mean-value theorem supplies the congruence pattern required by WI-111 at moduli of size `p^(11/21-epsilon)`, strictly beyond square root. Consequently, for every fixed

\[
\beta<\frac{11}{21},
\tag{1}
\]

there are simultaneous positive-defect fully packed prime interactions for which arbitrary linear pre/post-processing cannot retain both a fixed relative singular gap and a fixed normalized transmission merely by deleting `O(p^beta)` source directions.

More precisely, for every fixed `eta` with `0<eta<10/21` there are infinitely many odd source primes `p`, distinct odd target primes

\[
p<q_1<q_2<\frac{4p}{3},
\tag{2}
\]

one odd integer `ell`, and one common observation length `N` such that

\[
\boxed{\ell\asymp p^{11/21-\eta}},
\qquad
\Delta:=q_2-q_1\ll \ell\log p,
\tag{3}
\]

both `(p,q_i,N)` lie in WI-111's genuinely positive-defect exact full-packing regime, and the two left kernels contain explicit `(ell-1)`-dimensional quotient-character subspaces `W_i` with exact cross Gram

\[
\boxed{X_1^*X_2=\sqrt{\frac{t_2}{t_1}}I_{\ell-1}},
\qquad t_i=2p-q_i.
\tag{4}
\]

Hence every target-local processed concatenation

\[
B=[\,G_1C_1\;G_2C_2\,],
\qquad G_i=(U_p^{(N)})^*U_{q_i}^{(N)},
\tag{5}
\]

satisfies, with singular values padded to the source dimension `p-1`,

\[
\boxed{
\frac{\sigma_{p-\ell+1}(B)}{\sigma_1(B)}
\ll
p^{-5/21-\eta/2}\sqrt{\log p}
\longrightarrow0.
}
\tag{6}
\]

Together with WI-110/WI-111's conditioning-times-transmission product law, (6) rules out every deletion scale `O(p^beta)` with `beta<11/21`. This strictly subsumes WI-113's `sqrt(p)/log^(2+epsilon)p` deletion obstruction.

## 1. Maynard's fixed-residue theorem has exactly the absolute-error interface needed here

James Maynard, **Primes in arithmetic progressions to large moduli I: Fixed residue classes**, *Memoirs of the American Mathematical Society* 306 (2025), no. 1542, DOI `10.1090/memo/1542`, proves in Corollary 1.4 that for every fixed integer `a`, every `epsilon>0`, and every `A>0`,

\[
\boxed{
\sum_{r\le x^{1/21}\atop (r,a)=1}
\sum_{s\le x^{10/21-\epsilon}\atop (s,a)=1}
\left|
\pi(x;rs,a)-\frac{\pi(x)}{\varphi(rs)}
\right|
\ll_{a,\epsilon,A}
\frac{x}{(\log x)^A}.
}
\tag{7}
\]

The absolute value is load-bearing. It permits a Markov/finite-union selection of one factorized modulus that is simultaneously good for several fixed endpoints and both residue classes used below. Maynard explicitly records `x^(11/21-epsilon)` as the resulting modulus scale.

The congruence pattern in WI-111 looks at first sight incompatible with a theorem for a **fixed** residue because the target condition was written

\[
p\equiv1\pmod{2\ell},
\qquad
q\equiv\ell+2\pmod{2\ell}.
\tag{8}
\]

For odd `ell`, however, parity removes this apparent dependence. If `p` is an odd prime and `p=1 mod ell`, writing `p=1+k ell` forces `k` even, hence

\[
\boxed{p\equiv1\pmod\ell\quad\Longrightarrow\quad p\equiv1\pmod{2\ell}.}
\tag{9}
\]

Likewise, if `q` is an odd prime and `q=2 mod ell`, writing `q=2+k ell` forces `k` odd, hence

\[
\boxed{q\equiv2\pmod\ell\quad\Longrightarrow\quad q\equiv\ell+2\pmod{2\ell}.}
\tag{10}
\]

Thus the exact WI-111 residue geometry is supplied by the two **fixed** Maynard residues `a=1` and `a=2` modulo an odd `ell`.

## 2. One factorized odd modulus is simultaneously good for source and target intervals

Fix `eta` with `0<eta<10/21` and let `X` tend to infinity. Put

\[
R=X^{1/21},
\qquad
S=X^{10/21-\eta}.
\tag{11}
\]

Restrict the two sums in (7) to odd integers

\[
\frac R2<r\le R,
\qquad
\frac S2<s\le S.
\tag{12}
\]

There are

\[
M\asymp RS\asymp X^{11/21-\eta}
\tag{13}
\]

such ordered pairs. Set `ell=rs`; then every candidate `ell` is odd and

\[
\ell\asymp RS\asymp X^{11/21-\eta}.
\tag{14}
\]

Consider the separated source and target intervals

\[
I_s=[X,1.05X],
\qquad
I_t=[1.10X,1.15X].
\tag{15}
\]

Apply (7) at the four fixed endpoints

\[
(X,1),\quad(1.05X,1),\quad(1.10X,2),\quad(1.15X,2),
\tag{16}
\]

where the second coordinate denotes the fixed residue. The ranges (12) remain inside Maynard's permitted factor ranges after replacing `X` by any of the fixed multiples in (16). For residue `2`, the coprimality restrictions in (7) are exactly the oddness imposed in (12); for residue `1` they are automatic.

For any one endpoint/residue pair, call `(r,s)` bad if

\[
\left|
\pi(cX;rs,a)-\frac{\pi(cX)}{\varphi(rs)}
\right|
>
\kappa\frac{X}{RS\log X},
\tag{17}
\]

where `kappa>0` is a sufficiently small fixed constant. By (7), for any fixed `A>2`, the number of bad pairs is

\[
\ll
\frac{X/(\log X)^A}
{X/(RS\log X)}
=
\frac{RS}{(\log X)^{A-1}}
=o(M).
\tag{18}
\]

A finite union over the four conditions in (16) is still `o(M)`. Hence for every sufficiently large `X` there is one odd pair `(r,s)` satisfying all four endpoint bounds simultaneously.

For that pair, the prime number theorem and `phi(ell)<=ell<=RS` show that the main-term difference across either interval in (15) is bounded below by a fixed positive multiple of

\[
\frac{X}{\ell\log X}
\ge
\frac{X}{RS\log X}.
\tag{19}
\]

Choosing `kappa` smaller than that fixed interval-main constant makes the two endpoint errors harmless. Therefore

\[
\#\{p\in I_s:p\text{ prime},\ p\equiv1\pmod\ell\}
\gg\frac{X}{\ell\log X},
\tag{20}
\]

and

\[
J:=\#\{q\in I_t:q\text{ prime},\ q\equiv2\pmod\ell\}
\gg\frac{X}{\ell\log X}.
\tag{21}
\]

The right-hand side tends to infinity because `ell=X^(11/21-eta+o(1))`. Choose one source prime `p` from (20), and choose two consecutive members `q_1<q_2` of the target set in (21). Pigeonholing their gaps in the fixed-length interval gives

\[
\boxed{
\Delta=q_2-q_1\ll\ell\log X.
}
\tag{22}
\]

Equations (9)--(10) upgrade the residue conditions to exactly (8). The interval separation gives `p<q_i`, while `q_i<=1.15X<4p/3` because `p>=X`. Also `p\asymp X`, so (14) and (22) become (3).

No prime-power subtraction is needed in this argument: Maynard's theorem is stated directly for `pi(x;q,a)`, so (20)--(21) count actual primes.

## 3. WI-111's exact quotient-character geometry applies unchanged

With (8) now established, all finite geometry from WI-111 is available without a new spectral assumption. Put

\[
d_i=q_i-p,
\qquad
h_i=d_i/2,
\qquad
 t_i=2p-q_i.
\tag{23}
\]

The congruences imply

\[
d_i\equiv\ell+1\pmod{2\ell},
\qquad
h_i\equiv\frac{\ell+1}{2}\pmod\ell,
\qquad
\ell\mid t_i.
\tag{24}
\]

Because `ell=o(p)`, WI-111's common-center construction supplies a center and, by the generalized Chinese remainder theorem, one observation length `N` for which both `(p,q_i,N)` are genuinely positive-defect exact full-packed interactions. Their left kernels

\[
K_i=\ker G_i^*
\tag{25}
\]

contain quotient-character subspaces

\[
W_i\subset K_i,
\qquad
\dim W_i=\ell-1,
\tag{26}
\]

with orthonormal character bases satisfying the exact isoclinic identity (4). In particular every unit vector in either `W_i` obeys

\[
\operatorname{dist}(x,K_j)^2
\le
\frac{\Delta}{t_1}
\le
\frac{3\Delta}{2p}.
\tag{27}
\]

The last inequality uses `q_1<4p/3`, hence `t_1>2p/3`.

Allow arbitrary target-local right processing `C_i` as in (5). Since right processing preserves the original left kernels, WI-111's Courant--Fischer argument on the whole `(ell-1)`-dimensional sector gives

\[
\frac{\sigma_{p-\ell+1}(B)}{\sigma_1(B)}
\le
\sqrt{\frac{3\Delta}{2p}}.
\tag{28}
\]

Combining (3), (22), and `ell\asymp p^(11/21-eta)` yields

\[
\sqrt{\frac{\Delta}{p}}
\ll
\sqrt{\frac{\ell\log p}{p}}
\asymp
p^{-5/21-\eta/2}\sqrt{\log p},
\tag{29}
\]

which proves (6). The near-null multiplicity is simultaneously

\[
\boxed{\ell-1\asymp p^{11/21-\eta}.}
\tag{30}
\]

The gain over WI-113 is therefore not logarithmic bookkeeping: the bad singular sector itself has polynomial dimension strictly larger than `sqrt(p)` whenever `eta<1/42`, and the family can be taken with arbitrarily small positive `eta`.

## 4. Consequence for arbitrary linear rescue

Retain WI-110/WI-111's scale-sensitive formulation. For arbitrary further linear maps

\[
A=LBS,
\tag{31}
\]

and every retained index `k`, define

\[
r_k(A)=\frac{\sigma_k(A)}{\sigma_1(A)},
\qquad
\tau_B(L,S)=
\frac{\sigma_1(A)}{\|L\|_2\sigma_1(B)\|S\|_2}.
\tag{32}
\]

The singular-value ideal property gives

\[
\boxed{
r_k(A)\tau_B(L,S)
\le
\frac{\sigma_k(B)}{\sigma_1(B)}.}
\tag{33}
\]

Suppose a proposed linear rescue deletes at most

\[
d(p)=O(p^\beta)
\tag{34}
\]

source dimensions for a fixed `beta<11/21`. Choose `eta` with

\[
0<\eta<\min\left(\frac{10}{21},\frac{11}{21}-\beta\right).
\tag{35}
\]

Then (30) gives `d(p)=o(ell)`, so for all sufficiently large members of the counterfamily the retained index

\[
k=p-1-d(p)
\tag{36}
\]

still satisfies `k>=p-ell+1`. Equations (6) and (33) therefore force

\[
\boxed{
r_k(A)\tau_B(L,S)\longrightarrow0.}
\tag{37}
\]

Thus no such arbitrary linear pre/post-processing scheme can uniformly keep both `r_k(A)>=c>0` and `tau_B(L,S)>=c'>0` across the exact full-packed family. The deletion obstruction is now every fixed power strictly below `11/21`, not merely every power below `1/2` or square-root dimension with logarithmic savings.

## 5. Prior art, boundary, and falsification

The load-bearing prime-distribution input is entirely established prior art: Maynard's Corollary 1.4 is a fixed-residue, absolute-error mean theorem and is used exactly at its printed factor ranges. The new derivation is the parity reduction (9)--(10), simultaneous four-endpoint selection, and propagation of that larger modulus scale through the already exact WI-111 quotient-character/Courant--Fischer obstruction. No new theorem about distribution of primes is claimed.

A targeted audit also checked the obvious beyond-`11/21` comparison. Jared Duker Lichtman's **Primes in arithmetic progressions to large moduli, and shifted primes without large prime factors**, arXiv:2211.09641, reaches quadrilinear moduli up to `x^(17/32-epsilon)`, but its Theorem 1.4 controls a **signed weighted quadrilinear sum** rather than the sum of absolute individual progression errors in Maynard's Corollary 1.4. That interface does not by itself support the Markov/finite-union selection in (17)--(18), because cancellation between moduli may hide large individual endpoint errors. No `17/32` conclusion is therefore imported here. Maynard's later uniform-residue variants and well-factorable estimates likewise have different weight/error interfaces and are not silently substituted for (7).

Searches combining fixed-residue large-modulus distribution with Ramanujan full-packing kernels, quotient-character near-null subspaces, isoclinic defect sectors, and restricted-invertibility/deletion obstructions located no matching theorem. This negative search is not a priority claim. The durable content is the exact specialization above.

Several boundaries remain explicit. First, the argument needs `eta>0`, so it does not close deletion of order `p^(11/21)` itself. Second, it constructs an infinite exact full-packed counterfamily; it does not prove that such synchronized windows occur with positive density in a zeta-derived analytic average. Third, it constrains the auxiliary Ramanujan/full-packing linear-rescue pathway, not the whole Weil-inertia program: positive slack away from exact packing, nonlinear processing, zeta-specific arithmetic information, or an operator changed before this compression remain outside the claim. Finally, this finding neither changes the established simple-critical-zero proportion nor identifies the uncertified zero complement.

The decisive falsification point is the simultaneous-good-modulus step. To refute the claimed `11/21` strengthening it would suffice to show that Corollary 1.4 cannot be restricted and unioned as in (12)--(18), that the parity implications (9)--(10) fail under the selected prime conditions, or that one of WI-111's exact common-center hypotheses is lost when `ell` grows at scale `p^(11/21-eta)`. Each check is explicit above; none uses a conjectural prime-distribution hypothesis.

## Program consequence

WI-113 made the square-root/logarithmic endpoint look like the natural arithmetic frontier for this obstruction. It is not. The obstacle came from using an unrestricted Bombieri--Vinogradov good-modulus selection when the full-packing congruences secretly reduce, by parity, to two fixed residue classes. Maynard's stronger fixed-residue theorem therefore moves the exact near-null sector beyond square root to every exponent below `11/21`.

The next honest arithmetic question is whether a later beyond-`11/21` theorem has enough **absolute-error or otherwise selector-compatible structure** to choose one modulus simultaneously good for both fixed residues and the four interval endpoints. A larger nominal exponent alone is insufficient: the selection mechanism must survive the theorem's weighting and cancellation interface.
