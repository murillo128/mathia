# VIS-432 — binomial-tail Bernstein smoothing reduces rare-target depth to logarithmic mass

## Claim

Let (X,m) carry a measure-preserving real flow tau(u), let Y:X->[0,1], and fix 0<=a<b<=1. Put g=b-a, c=(a+b)/2, and for an integer d>=1 let M_d=ceil(d c). Define the degree-d Bernstein tail polynomial

q_d(x)=sum_(k=M_d)^d binom(d,k) x^k(1-x)^(d-k).

Then 0<=q_d<=1 on [0,1]. With epsilon_d=exp(-d g^2/2),

q_d(x)<=epsilon_d for every x<=a,

q_d(x)>=1-epsilon_d for every x>=b.

Define L_(d,rho)(x)=int_(-rho)^rho q_d(Y(x tau(u)))du and qbar_d=int_X q_d(Y)dm. If mu_b=m{Y>=b} and

D_d:=(1-epsilon_d)mu_b-epsilon_d>0,

then for every rho>0,

m{H_a>rho} <= Var(L_(d,rho)) / (Var(L_(d,rho))+4rho^2 D_d^2),

where H_a(x)=inf{|u|:Y(x tau(u))>=a}.

The positivity condition is guaranteed as soon as

d > (2/g^2) log((1+mu_b)/mu_b).

For the strict near-band Wang shells, with Y=X_N=|F_N|^2/S_N^2, the polynomial q_d(X_N) is a finite Laurent observable of depth at most d. If W_N=(sum_a |b_(N,a)|)/S_N and delta^*_(N,d) is the depth-d structural divisor from VIS-425, then

Var(L_(d,rho)) <= 4 * 9^d W_N^(4d)/(delta^*_(N,d))^2.

Using delta^*_(N,d)>=(2Y_N)^(-2d) gives

Var(L_(d,rho)) <= 4 * 9^d W_N^(4d)(2Y_N)^(4d).

Thus the mu_b^(-2) degree growth produced by the Lipschitz-ramp Bernstein estimate in VIS-431 is not intrinsic. With a pre-existing threshold gap b-a, the same hard-target hitting reduction needs only

d=O(g^(-2) log(1/mu_b))

as mu_b->0. The surviving difficulty is therefore the ability of the Wang moment/small-divisor control to remain useful at logarithmically growing Laurent depth, not the polynomial approximation of a rare target itself.

**Evidence/status:** EXACT-DERIVED + CLASSICAL HOEFFDING INPUT + REPRESENTATION-CERTIFIED + QUANTITATIVE BOUNDARY + NO-NOVELTY-CLAIM.

No optimal polynomial-approximation rate, changing-shell selector anomaly, shrinking-target law, mixing theorem, or RH consequence is claimed.

## 1. A thresholded Bernstein polynomial is a binomial tail

For K~Bin(d,x),

q_d(x)=P_x(K>=M_d).

Because the Bernstein basis is nonnegative and sums to one, 0<=q_d<=1.

If x<=a, then M_d/d>=c, so K>=M_d implies K/d-x>=c-a=g/2. Hoeffding's bounded-sum inequality therefore gives

q_d(x)<=exp(-2d(g/2)^2)=exp(-d g^2/2).

If x>=b, then

1-q_d(x)=P_x(K<=M_d-1).

Since M_d-1<dc, the event implies x-K/d>b-c=g/2, and the lower-tail Hoeffding bound gives the same estimate. This proves the separator inequalities.

The construction approximates only what the hitting argument needs: small values on [0,a] and large values on [b,1]. It does not uniformly approximate a continuous ramp across the buffer interval. That is why target rarity enters exponentially rather than through the 1/sqrt(d) Bernstein modulus bound used in VIS-431.

## 2. The occupation argument is unchanged

If H_a(x)>rho, then Y(x tau(u))<a for every |u|<=rho, hence L_(d,rho)(x)<=2rho epsilon_d. Flow invariance gives E[L_(d,rho)]=2rho qbar_d.

On {Y>=b}, the separator bound gives q_d>=1-epsilon_d, while q_d>=0 everywhere. Therefore

qbar_d >= (1-epsilon_d)mu_b

and qbar_d-epsilon_d >= D_d.

Cantelli's one-sided variance inequality applied to the lower deviation of L_(d,rho) yields the stated hitting bound whenever D_d>0.

Since D_d>0 iff epsilon_d < mu_b/(1+mu_b), the exponential separator gives the explicit sufficient depth

d > (2/g^2) log((1+mu_b)/mu_b).

For fixed g>0, rare target mass therefore costs only logarithmic polynomial depth in this certificate.

## 3. Wang specialization keeps the same Laurent tariff

The polynomial q_d is a sum of a subset of Bernstein basis terms. The monomial coefficient l1 norm of binom(d,k)x^k(1-x)^(d-k) is binom(d,k)2^(d-k). Hence the monomial coefficient l1 norm of q_d is at most 3^d.

As in VIS-431, the normalized squared shell amplitude satisfies ||X_N||_A<=W_N^2. Wiener-algebra submultiplicativity therefore gives

||q_d(X_N)||_A<=3^d W_N^(2d).

Every nonconstant character in q_d(X_N) is a sum of at most d shell-frequency differences and is consequently bounded away from zero by delta^*_(N,d). Applying the exact occupation-variance identity from VIS-430 gives

Var(L_(d,rho))
 =4 sum_(m!=0)|chat_m|^2 sin^2(rho lambda_m)/lambda_m^2
 <=4 * 9^d W_N^(4d)/(delta^*_(N,d))^2.

The explicit strict near-band divisor floor from VIS-425 then yields the arithmetic-height form in the claim.

## 4. What remains genuinely open

VIS-431 correctly identified growing approximation depth as the obstruction for rare or narrow targets, but its quantitative d~mu_b^(-2) rarity cost came from approximating an entire Lipschitz ramp. The threshold-tail construction shows that this cost is avoidable when a nonzero target buffer is already part of the test.

For fixed g, the unresolved regime is now sharper. A changing Wang family must control quantities such as [3 W_N^2 (2Y_N)^2]^d at depths d of order log(1/mu_b), together with the actual denominator D_d. Whether the true coefficient geometry provides enough cancellation or sharper structural divisors at that slowly growing depth is a separate question.

If the buffer itself shrinks, the present Hoeffding certificate pays g^(-2); no optimality is claimed. A sharper large-deviation/Chernoff treatment, a different bounded separator polynomial, or source-specific cancellation may improve constants or gap dependence. Those are independent follow-up questions rather than premises of this finding.

## 5. Prior art, representation audit, and falsification

Wassily Hoeffding's 1963 concentration inequalities give the classical exponential tail bound for sums of independent bounded random variables used in the binomial separator. Bernstein basis polynomials and their binomial-probability representation are classical; the Lorentz monograph and the Cui--Pillichshammer account already cited for VIS-431 delimit that approximation-theory background.

No novelty is claimed for Hoeffding concentration, Bernstein basis positivity, binomial tails, Cantelli, or Wiener-algebra estimates. The Mathia delta is the exact buffered-hitting specialization: replacing the ramp approximant of VIS-431 by the Bernstein polynomial of a thresholded coefficient sequence converts rare-target approximation from algebraic to exponential error while preserving the same finite Laurent-depth interface.

The representation remains intrinsic to the normalized squared shell amplitude and the actual prime-log flow. No rasterization, plotting choice, random-phase surrogate, or visually selected threshold enters the derivation.

Falsify the result by finding a violation of either Hoeffding separator bound, failure of the hard-target avoidance implication, a nonconstant character of q_d(X_N) outside depth d, failure of the Wiener coefficient bound, or failure of the VIS-425 divisor floor in the stated strict near-band regime.

## Dependencies

- VIS-425: depth-d Wang structural divisor and strict near-band floor.
- VIS-429: complementary target-rarity lower bound for quiet windows.
- VIS-430: occupation variance converts finite Fourier control into a hitting upper bound.
- VIS-431: buffered polynomial smoothing framework and the earlier Lipschitz-ramp degree certificate.

## Research consequence

For a pre-registered buffered Wang target, do not treat small mu_b alone as forcing polynomial depth of order mu_b^(-2). Use the thresholded Bernstein tail and choose a depth satisfying

d > (2/(b-a)^2) log((1+mu_b)/mu_b).

The remaining source-sensitive test is whether the Wang Wiener/small-divisor tariff stays controlled at that logarithmically growing depth. Only if it fails is a rarer/shrinking target still an independent escape from the finite-depth Haar hitting control.
