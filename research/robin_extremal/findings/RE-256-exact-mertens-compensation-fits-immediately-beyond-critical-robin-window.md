# RE-256 — Exact Mertens compensation fits immediately beyond the critical Robin window

**Status:** EXACT-DERIVED + SHARP-LOCAL-SOURCE-OBSTRUCTION + EXACT-MERTENS-FIDELITY + ALL-START-SHORT-INTERVAL-CONTROL + GENERALIZED-LABEL-BOUNDARY; independent adversarial review pending.

**Dependencies:** RE-021 (selected ordinary CA frontier), RE-169 (global Mertens/source-kernel sum rule), RE-170–RE-171 (two-/three-shell exact-Mertens compensation at bounded-multiplicative distance), RE-252–RE-253 (Guth–Maynard critical near-frontier window and triangular moment), RE-254–RE-255 (critical matched transports and joint endpoint contrast).

RE-254 shows that a source exactly matching the selected CA prefix and the uniform short-interval counting envelope can change the critical first-annulus Robin moment by order one. Its single-shell transports alter the generalized Mertens normalization. RE-169–RE-171 show that Mertens debt can be compensated in later shells of size comparable with p. The present construction closes the intervening *spatial* question: **even exact global Mertens matching can be achieved in the immediately adjacent interval of length H_star=o(p), while the earlier critical signed moment remains order one**. Neither a distant proportional shell nor a relaxed all-start counting estimate is needed.

## 1. Precise two-shell theorem

Let p tend to infinity through ordinary primes, put L=log p and
\[
e_p=\exp(-L^{1/4}),\qquad
H=H_\star(p)=\frac{p^{3/4}}{\sqrt L}\exp\left(\frac12 L^{1/4}\right),
\qquad e_pH^2=\frac{p^{3/2}}L.
\tag{1}
\]
Fix any a>0. There exists, for every sufficiently large p, a strictly increasing discrete **real-label** generalized-prime source Q_p obtained by an order-preserving finite transport of the ordinary primes P with all of the following properties:

1. Every label at or below p+H/4, and every label at or above p+7H/4, is untouched. In particular the complete ordinary-prime source through any RE-021-selected self-tangent CA state is frozen: its selector lies at X=p+O(p^{0.52})<p+H/4. No labels are created or removed, the rank and the number in each of (p,p+H] and (p+H,p+2H] are preserved, and all consecutive-gap ratios are 1+o(1).
2. For one fixed x_0 and one implied constant independent of p,
   \[
   \Pi_{Q_p}(x+y)-\Pi_{Q_p}(x)
   =\frac y{\log x}
   +O_{a,\varphi}\left(y\exp(- (\log x)^{1/4})\right)
   \quad(x\ge x_0,\quad x^{3/5}\le y\le x^{0.99}),
   \tag{2}
   \]
   uniformly for every real starting point x.
3. With Gamma defined by the generalized Mertens limit in RE-169, **the global normalization is exactly ordinary**:
   \[
   \boxed{\Gamma(Q_p)=\Gamma(P)=\gamma.}\tag{3}
   \]
4. For the triangular moment of RE-253, with its usual common centering,
   \[
   \boxed{
   \frac L{p^{3/2}}(D_{Q_p,p}(H)-D_{P,p}(H))=-a+o(1),
   \qquad
   \frac L{p^{3/2}}(D_{Q_p,p}(2H)-D_{P,p}(2H))=o(1).
   }\tag{4}
   \]
5. For the direct source-model Robin kernel I_Q defined as in RE-254,
   \[
   \boxed{
   \sqrt pL\int_p^{p+H}(I_{Q_p}-I_P)(t)\,dt=a+o(1),
   \qquad
   \sqrt pL\int_p^{p+2H}(I_{Q_p}-I_P)(t)\,dt=o(1).
   }\tag{5}
   \]

The second shell repays the first shell's Mertens/Robin debt at the first adjacent H_star-sized opportunity. The theorem asserts neither that the ordinary primes can be replaced by different ordinary primes nor that the genuine fixed CA integer changes Robin height: the ordinary divisor sum is identical throughout.

## 2. Constructing and exactly balancing the two bumps

Choose a nonnegative \(\varphi\in C_c^\infty((1/4,3/4))\) with \(\int\varphi=1\). Let
\[
\varphi_1(u)=\varphi(u),\quad
\varphi_2(u)=\varphi(u-1),\quad
s=aLe_pH,
\quad
F_\lambda(t)=t+s\varphi_1((t-p)/H)-\lambda s\varphi_2((t-p)/H).
\tag{6}
\]
For \(0\le\lambda\le2\), the maps are the identity outside two disjoint compact subintervals of (p,p+2H), and
\[
F'_\lambda(t)=1+O_{a,\varphi}(Le_p)=1+o(1).
\tag{7}
\]
They are therefore increasing homeomorphisms for sufficiently large p, with displacements much smaller than H. Put \(Q_{p,\lambda}=\{F_\lambda(q):q\in P\}\). The exterior identity, matching counts, and gap-ratio assertion follow immediately.

Set
\[
S_{j,p}=\sum_{q\in P}\varphi_j((q-p)/H)\quad(j=1,2).
\tag{8}
\]
Pointwise Guth–Maynard on the two fixed subintervals at distance O(H) from p, followed by Stieltjes integration by parts against the compact smooth bumps, yields
\[
S_{j,p}=\frac HL\bigl(1+O_\varphi(Le_p+H/p)\bigr),\qquad j=1,2.
\tag{9}
\]
Both sums are strictly positive for sufficiently large p.

Write \(f(t)=-\log(1-t^{-1})=\log(t/(t-1))\). Because Q differs from P in only finitely many labels, RE-169's normalization exists and the difference is **exactly**
\[
\mathcal M_p(\lambda)
:=\Gamma(Q_{p,\lambda})-\gamma
=\sum_{q\in P}[f(F_\lambda(q))-f(q)].
\tag{10}
\]
All terms are supported on the two bumps. Since \(f'(t)=-1/[t(t-1)]\) and every involved label is p+O(H), Taylor's integral formula, uniformly in \(0\le\lambda\le2\), gives
\[
\mathcal M_p(\lambda)
=-\frac{s}{p^2}(S_{1,p}-\lambda S_{2,p})
+O\left(\frac{sH}{p^3}(S_{1,p}+\lambda S_{2,p})\right).
\tag{11}
\]
The function \(\mathcal M_p\) is continuous and **strictly increasing**: only second-shell labels depend on \(\lambda\), and moving them left increases f. Equations (9)–(11) show \(\mathcal M_p(0)<0<\mathcal M_p(2)\) for large p. Thus there is a unique \(\lambda_p\in(0,2)\) such that \(\mathcal M_p(\lambda_p)=0\); moreover
\[
\lambda_p=1+O_\varphi(Le_p+H/p)=1+o(1).
\tag{12}
\]
Take \(Q_p=Q_{p,\lambda_p}\). This proves exact equality (3) by an actual finite atomic real-label transport, not by a signed continuous approximation. No additional distant compensation is used.

## 3. All-start counting remains uniform

Let G=F_{\lambda_p}^{-1}. The counting identity is exact:
\[
\Pi_{Q_p}(x+y)-\Pi_{Q_p}(x)=\pi(G(x+y))-\pi(G(x)).
\tag{13}
\]
If both endpoints are outside the transport support, (13) is the unchanged ordinary-prime count. Otherwise x/p=1+o(1), because y\le x^{0.99}=o(x) and at least one endpoint is p+O(H). Uniformly,
\[
G(x)=x+O(s),\qquad G(x+y)-G(x)=y(1+O_{a,\varphi}(Le_p)).
\tag{14}
\]
Take the pointwise Guth–Maynard short-interval theorem with epsilon=1/40, whose admissible lower exponent 17/30+1/40 is below 3/5. The small relative deformation in (14) stays inside its lower range. Near the upper endpoint y=x^{0.99}, splitting into two half-intervals keeps each below the theorem's upper cutoff; the change of logarithmic main terms is O(y^2/(x(log x)^2))=o(ye_p). Restoring the original x,y main term costs O(ye_p), since the length change is O(yLe_p) and the logarithmic start change is o(e_p). Therefore the common all-start bound (2) follows. The same proof works for either sign and any bounded \(\lambda\); choosing the exact Mertens root does not weaken it.

## 4. The critical moment survives, then cancels

Both bumps lie strictly inside their respective H-sized shells. At b=p+H only the positive first bump is present. In the exact triangular sum of RE-253, count and baseline agree with P, so
\[
D_{Q_p,p}(H)-D_{P,p}(H)=-sS_{1,p}.
\tag{15}
\]
Using (1), (6) and (9) proves the first limit in (4). At b=p+2H both bumps are included:
\[
D_{Q_p,p}(2H)-D_{P,p}(2H)
=-s(S_{1,p}-\lambda_pS_{2,p}).
\tag{16}
\]
Exact Mertens balance in (11) forces
\[
|S_{1,p}-\lambda_pS_{2,p}|
\ll(H/p)(S_{1,p}+\lambda_p S_{2,p}),
\tag{17}
\]
hence the second expression of (4) is O(H/p)=o(1) after multiplication by L/p^{3/2}. Both statements concern differences of finite source moments; neither estimates the unknown ordinary-prime moment D_{P,p}(H) itself.

## 5. An exact finite-kernel cross-check

For b\in\{p+H,p+2H\}, each bump is either entirely included or entirely excluded. Writing \(\Theta_Q(b)=\sum_{p<r\le b,r\in Q}\log r\), Stieltjes integration by parts of the **actual kernel** gives
\[
\boxed{
\int_p^b(I_Q-I_P)(t)\,dt
=h(b)(\Theta_Q(b)-\Theta_P(b))
-\sum_{q\in P:\ p<q\le b}[f(F(q))-f(q)].
}\tag{18}
\]
The deterministic (h-k) terms cancel, the sources agree through p, and \((\log r)h(r)=f(r)\). No frozen-kernel approximation is used here.

For both endpoints,
\[
|\Theta_Q(b)-\Theta_P(b)|
\ll\frac{s}{p}(S_{1,p}+S_{2,p})
\ll\frac{\sqrt p}{L},
\qquad
\sqrt pLh(b)|\Theta_Q(b)-\Theta_P(b)|=O(L^{-1}).
\tag{19}
\]
At b=p+H, the finite Euler-factor sum in (18) is only the first bump and equals
\(-sS_{1,p}p^{-2}(1+O(H/p))\); multiplication by \(\sqrt pL\) gives \(-a+o(1)\). Equation (18) therefore yields the first relation in (5). At b=p+2H, the finite Euler-factor sum is **exactly zero** by (10) and (12), giving the second relation in (5) with the explicit O(L^{-1}) terminal correction. This also checks the signs: pushing labels right decreases the Mertens product contribution and increases the direct Robin-kernel integral.

## 6. Prior art, falsification, and information boundary

The only external arithmetic input is Guth and Maynard, *New large value estimates for Dirichlet polynomials*, *Annals of Mathematics* **203** (2026), 623–675, Corollary 1.3, already recorded in this line's SOURCES.md. The finite Mertens identity is RE-169; generalized exact-Mertens compensation is not novel in itself (RE-170–RE-171). Smooth monotone transport, integration by parts, and the intermediate value theorem are standard. What is additional here is the **joint scale constraint**: compensation entirely within two consecutive H_star=o(p) shells, each maintaining the same full all-start Guth–Maynard envelope, with an exactly frozen CA selector, unchanged ranks/counts, and exact ordinary Mertens normalization. RE-254 did not match Gamma; RE-170–RE-171 did not impose this near-frontier window and all-start input. No claim of an independently new prime-distribution theorem is made.

Critical tests: (i) do not replace all-start pointwise counting by an almost-all theorem; (ii) choose bumps supported away from p+H so the first signed moment cannot be affected by the second compensation; (iii) use the exact finite Euler-factor sum rather than treating log weights as unit masses; (iv) exact Gamma matching at 2H does **not** make the earlier H moment small; (v) the second moment cancellation only concerns the Q-minus-P difference, not the individual prime moment; (vi) the construction is asymptotic for fixed a and is not a numerical claim at accessible p.

Most importantly, **Q_p need not have prime or even integer labels**. The ordinary divisor-sum Euler factors, primality constraints, and any selected *future* arithmetic mechanism are not reproduced. RE-172 shows that exact finite Mertens compensation is impossible for a nontrivial finite perturbation supported on ordinary primes with rational multiplicities. Thus this theorem rules out deriving a *one-sided local moment bound* from the frozen CA prefix + all-start short-interval PNT + exact global Mertens scalar **alone** in the generalized-label fidelity class. It does not rule out a genuinely prime-supported rigidity theorem, bound the remaining remote annulus for ordinary primes, or prove Robin's inequality or RH.

**Research consequence:** To make the critical H_star first-annulus moment negligible from global normalization, a new assumption must also restrict the **placement of the compensating mass** (or provide genuinely prime-specific constraints). Exact Mertens normalization can coexist with an order-one critical signed excursion whose compensation occurs already at distance O(H_star), well before any bounded-multiplicative or Korobov–Vinogradov remote-tail scale.
